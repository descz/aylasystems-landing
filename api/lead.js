"use strict";

const tls = require("node:tls");

const SEGMENTS = new Set([
  "Clínica / Odontologia",
  "Advocacia",
  "Imobiliária",
  "Serviços de alto ticket",
  "Outro"
]);

const RATE_LIMIT = { windowMs: 60 * 60 * 1000, max: 5 };
const hits = new Map();

function clientIp(req) {
  const header = req.headers["x-forwarded-for"];
  if (typeof header === "string" && header.length) return header.split(",")[0].trim();
  return (req.socket && req.socket.remoteAddress) || "desconhecido";
}

function limited(ip) {
  const now = Date.now();
  const entry = hits.get(ip);
  if (!entry || now - entry.start > RATE_LIMIT.windowMs) {
    hits.set(ip, { start: now, count: 1 });
    return false;
  }
  entry.count += 1;
  if (hits.size > 5000) hits.clear();
  return entry.count > RATE_LIMIT.max;
}

function clean(value, max) {
  if (typeof value !== "string") return "";
  return value.replace(/[\u0000-\u001f\u007f]/g, " ").trim().slice(0, max);
}

function validPhone(value) {
  const digits = String(value || "").replace(/\D/g, "");
  return digits.length >= 10 && digits.length <= 13 ? digits : "";
}

function formatPhone(digits) {
  if (digits.length === 13 && digits.startsWith("55")) {
    return "+55 (" + digits.slice(2, 4) + ") " + digits.slice(4, 9) + "-" + digits.slice(9);
  }
  if (digits.length === 12 && digits.startsWith("55")) {
    return "+55 (" + digits.slice(2, 4) + ") " + digits.slice(4, 8) + "-" + digits.slice(8);
  }
  if (digits.length === 11) {
    return "(" + digits.slice(0, 2) + ") " + digits.slice(2, 7) + "-" + digits.slice(7);
  }
  if (digits.length === 10) {
    return "(" + digits.slice(0, 2) + ") " + digits.slice(2, 6) + "-" + digits.slice(6);
  }
  return digits;
}

function base64Lines(text) {
  const encoded = Buffer.from(text, "utf8").toString("base64");
  return encoded.match(/.{1,76}/g).join("\r\n");
}

function encodeSubject(text) {
  return "=?UTF-8?B?" + Buffer.from(text, "utf8").toString("base64") + "?=";
}

function buildMessage({ from, to, subject, body }) {
  const date = new Date().toUTCString();
  return [
    'From: "Ayla Systems" <' + from + ">",
    "To: <" + to + ">",
    "Subject: " + encodeSubject(subject),
    "Date: " + date,
    "MIME-Version: 1.0",
    "Content-Type: text/plain; charset=UTF-8",
    "Content-Transfer-Encoding: base64",
    "Message-ID: <" + Date.now() + "." + Math.random().toString(36).slice(2) + "@aylasystems.com>",
    "",
    base64Lines(body)
  ].join("\r\n");
}

function smtpSend({ host, port, user, pass, from, to, message, timeoutMs = 20000 }) {
  return new Promise((resolve, reject) => {
    const socket = tls.connect({ host, port, servername: host });
    const lines = [];
    const waiters = [];
    let buffer = "";
    let finished = false;
    let timer = null;

    function finish(error) {
      if (finished) return;
      finished = true;
      if (timer) clearTimeout(timer);
      try { socket.destroy(); } catch (_) {}
      if (error) reject(error);
      else resolve();
    }

    function arm(ms) {
      if (timer) clearTimeout(timer);
      timer = setTimeout(function () {
        finish(new Error("smtp_timeout"));
      }, ms);
    }

    function nextLine() {
      if (lines.length) return Promise.resolve(lines.shift());
      return new Promise(function (res) { waiters.push(res); });
    }

    socket.on("data", function (chunk) {
      buffer += chunk.toString("utf8");
      let index;
      while ((index = buffer.indexOf("\r\n")) !== -1) {
        const line = buffer.slice(0, index);
        buffer = buffer.slice(index + 2);
        if (/^\d{3}-/.test(line)) continue;
        const waiter = waiters.shift();
        if (waiter) waiter(line);
        else lines.push(line);
      }
    });

    socket.on("error", function (error) { finish(error); });
    socket.setTimeout(timeoutMs, function () { finish(new Error("smtp_socket_timeout")); });

    socket.on("secureConnect", async function () {
      try {
        arm(timeoutMs);
        async function command(line, accepted) {
          if (line !== null) socket.write(line + "\r\n");
          const reply = await nextLine();
          const code = parseInt(reply.slice(0, 3), 10);
          if (!accepted.includes(code)) throw new Error("smtp_" + reply.slice(0, 90));
          return reply;
        }
        await command(null, [220]);
        await command("EHLO aylasystems.com", [250]);
        await command("AUTH LOGIN", [334]);
        await command(Buffer.from(user, "utf8").toString("base64"), [334]);
        await command(Buffer.from(pass, "utf8").toString("base64"), [235]);
        await command("MAIL FROM:<" + from + ">", [250]);
        await command("RCPT TO:<" + to + ">", [250, 251]);
        await command("DATA", [354]);
        socket.write(message + "\r\n.\r\n");
        await command(null, [250]);
        await command("QUIT", [221]);
        arm(1000);
        finish(null);
      } catch (error) {
        finish(error);
      }
    });
  });
}

async function handler(req, res) {
  res.setHeader("Cache-Control", "no-store");
  if (req.method !== "POST") {
    res.status(405).json({ ok: false, error: "method_not_allowed" });
    return;
  }

  const ip = clientIp(req);
  if (limited(ip)) {
    res.status(429).json({ ok: false, error: "too_many_requests" });
    return;
  }

  let body = req.body;
  if (typeof body === "string") {
    try { body = JSON.parse(body); } catch (_) { body = null; }
  }
  if (!body || typeof body !== "object") {
    res.status(400).json({ ok: false, error: "invalid_body" });
    return;
  }
  if (JSON.stringify(body).length > 8000) {
    res.status(413).json({ ok: false, error: "too_large" });
    return;
  }
  if (clean(body.website, 80)) {
    res.status(200).json({ ok: true });
    return;
  }

  const name = clean(body.name, 80);
  const company = clean(body.company, 80);
  const segment = SEGMENTS.has(body.segment) ? body.segment : "Outro";
  const phoneRaw = clean(body.phone, 24);
  const phone = validPhone(phoneRaw);

  if (name.length < 2 || !phone) {
    res.status(400).json({ ok: false, error: "invalid_fields" });
    return;
  }

  const user = process.env.ZOHO_SMTP_USER;
  const pass = process.env.ZOHO_SMTP_PASS;
  const from = process.env.LEAD_FROM_EMAIL || user;
  const to = process.env.LEAD_TO_EMAIL || user;

  if (!user || !pass || !to) {
    console.error("lead: variaveis de SMTP ausentes");
    res.status(500).json({ ok: false, error: "not_configured" });
    return;
  }

  const when = new Intl.DateTimeFormat("pt-BR", {
    dateStyle: "short",
    timeStyle: "long",
    timeZone: "America/Sao_Paulo"
  }).format(new Date());

  const subject = "Novo lead no site: " + name + " - " + segment;
  const text = [
    "Novo pedido de demonstração no site da Ayla Systems.",
    "",
    "Nome: " + name,
    "Empresa: " + (company || "não informada"),
    "Segmento: " + segment,
    "WhatsApp: " + formatPhone(phone),
    "Recebido em: " + when + " (Brasília)",
    "",
    "Origem: " + clean(req.headers.origin, 120),
    "IP: " + ip,
    "Navegador: " + clean(req.headers["user-agent"], 200),
    "",
    "Atenda este contato pelo WhatsApp."
  ].join("\n");

  try {
    await smtpSend({
      host: "smtp.zoho.com",
      port: 465,
      user: user,
      pass: pass,
      from: from,
      to: to,
      message: buildMessage({ from: from, to: to, subject: subject, body: text })
    });
    res.status(200).json({ ok: true });
  } catch (error) {
    console.error("lead: falha no envio", error && error.message ? error.message : error);
    res.status(502).json({ ok: false, error: "send_failed" });
  }
}

module.exports = handler;
module.exports._smtpSend = smtpSend;
module.exports._buildMessage = buildMessage;
