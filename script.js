/* Ayla Systems — interações do site. Sem dependências externas. */

document.documentElement.classList.add("js");

(function () {
  "use strict";

  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* Header, progresso de leitura e menu ---------------------------------- */

  function initHeader() {
    const header = document.querySelector(".site-header");
    const progress = document.getElementById("scrollProgress");
    if (!header) return;

    let ticking = false;

    function update() {
      const y = window.scrollY || window.pageYOffset;
      header.classList.toggle("is-scrolled", y > 12);
      if (progress) {
        const max = document.documentElement.scrollHeight - window.innerHeight;
        const pct = max > 0 ? Math.min(100, (y / max) * 100) : 0;
        progress.style.width = pct + "%";
      }
      ticking = false;
    }

    window.addEventListener(
      "scroll",
      function () {
        if (!ticking) {
          window.requestAnimationFrame(update);
          ticking = true;
        }
      },
      { passive: true }
    );

    update();
  }

  function initNav() {
    const toggle = document.getElementById("navToggle");
    const nav = document.getElementById("siteNav");
    if (!toggle || !nav) return;

    function close() {
      nav.classList.remove("is-open");
      toggle.setAttribute("aria-expanded", "false");
      toggle.setAttribute("aria-label", "Abrir menu");
    }

    toggle.addEventListener("click", function () {
      const open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", String(open));
      toggle.setAttribute("aria-label", open ? "Fechar menu" : "Abrir menu");
    });

    nav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", close);
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && nav.classList.contains("is-open")) {
        close();
        toggle.focus();
      }
    });
  }

  /* Entrada suave dos blocos --------------------------------------------- */

  function initReveal() {
    const items = Array.prototype.slice.call(document.querySelectorAll(".reveal"));
    if (!items.length) return;

    if (!("IntersectionObserver" in window)) {
      items.forEach(function (el) {
        el.classList.add("is-visible");
      });
      return;
    }

    const observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
    );

    items.forEach(function (el) {
      observer.observe(el);
    });
  }

  /* FAQ ------------------------------------------------------------------- */

  function initAccordion() {
    document.querySelectorAll(".accordion").forEach(function (group) {
      const items = Array.prototype.slice.call(group.querySelectorAll(".acc-item"));

      items.forEach(function (item) {
        const button = item.querySelector(".acc-btn");
        if (!button) return;

        button.addEventListener("click", function () {
          const isOpen = item.classList.contains("is-open");

          items.forEach(function (other) {
            other.classList.remove("is-open");
            const otherButton = other.querySelector(".acc-btn");
            if (otherButton) otherButton.setAttribute("aria-expanded", "false");
          });

          if (!isOpen) {
            item.classList.add("is-open");
            button.setAttribute("aria-expanded", "true");
          }
        });
      });
    });
  }

  /* Abas ------------------------------------------------------------------ */

  function initTabs() {
    document.querySelectorAll(".tabs").forEach(function (tabList) {
      const tabs = Array.prototype.slice.call(tabList.querySelectorAll("[data-tab]"));
      if (!tabs.length) return;

      const keys = tabs.map(function (tab) {
        return tab.dataset.tab;
      });

      const panels = Array.prototype.slice
        .call(document.querySelectorAll(".tab-panel"))
        .filter(function (panel) {
          return keys.indexOf(panel.dataset.panel) !== -1;
        });

      function activate(key, focus) {
        tabs.forEach(function (tab) {
          const active = tab.dataset.tab === key;
          tab.classList.toggle("is-active", active);
          tab.setAttribute("aria-selected", String(active));
          tab.tabIndex = active ? 0 : -1;
          if (active && focus) tab.focus();
        });

        panels.forEach(function (panel) {
          const active = panel.dataset.panel === key;
          panel.classList.toggle("is-active", active);
          panel.hidden = !active;
        });
      }

      tabs.forEach(function (tab, index) {
        tab.addEventListener("click", function () {
          activate(tab.dataset.tab, false);
        });

        tab.addEventListener("keydown", function (event) {
          let target = null;
          if (event.key === "ArrowRight") target = tabs[(index + 1) % tabs.length];
          if (event.key === "ArrowLeft") target = tabs[(index - 1 + tabs.length) % tabs.length];
          if (event.key === "Home") target = tabs[0];
          if (event.key === "End") target = tabs[tabs.length - 1];
          if (!target) return;
          event.preventDefault();
          activate(target.dataset.tab, true);
        });
      });
    });
  }

  /* Simulador de conversa -------------------------------------------------- */

  const HOME_MESSAGES = [
    {
      from: "user",
      time: "22:47",
      text: "Oi, vi o anúncio de vocês. Estou com uma dor forte no dente de trás. Vocês atendem amanhã cedo?"
    },
    {
      from: "ayla",
      time: "22:47",
      text: "Olá. Atendemos sim. Casos com dor aguda têm prioridade nos primeiros horários da manhã. É sua primeira consulta?"
    },
    {
      from: "user",
      time: "22:48",
      text: "Sim, primeira vez."
    },
    {
      from: "ayla",
      time: "22:48",
      text: "Perfeito. Tenho 08h30 ou 09h15 com o Dr. Marcos. Qual fica melhor?"
    },
    {
      from: "user",
      time: "22:48",
      text: "08h30."
    },
    {
      from: "ayla",
      time: "22:48",
      text: "Reservei 08h30. Para adiantar a ficha, me confirma seu nome completo?"
    },
    {
      from: "user",
      time: "22:49",
      text: "Carlos Eduardo Mendes."
    },
    {
      from: "ayla",
      time: "22:49",
      text: "Pronto, Carlos. Consulta confirmada para amanhã, 08h30, com o Dr. Marcos. Vou te enviar o endereço e as orientações por aqui."
    },
    {
      from: "user",
      time: "22:49",
      text: "Perfeito, obrigado."
    },
    {
      from: "ayla",
      time: "22:50",
      text: "Às ordens. Se a dor piorar durante a noite, responda esta mensagem. A equipe acompanha por aqui. Até amanhã."
    }
  ];

  const FULL_MESSAGES = [
    {
      from: "user",
      time: "22:47",
      text: "Olá. Vi o anúncio de vocês. Estou com uma dor forte no dente de trás. Vocês atendem amanhã cedo?"
    },
    {
      from: "ayla",
      time: "22:47",
      text: "Olá. Atendemos sim. Para casos com dor aguda, priorizamos os primeiros horários da manhã. Você já é paciente da clínica ou será a primeira consulta?"
    },
    {
      from: "user",
      time: "22:48",
      text: "Primeira vez. Moro aqui perto."
    },
    {
      from: "ayla",
      time: "22:48",
      text: "Perfeito. Temos 08h30 ou 09h15 com o Dr. Marcos. Qual fica melhor para você?"
    },
    {
      from: "user",
      time: "22:49",
      text: "08h30 fica ótimo."
    },
    {
      from: "ayla",
      time: "22:49",
      text: "Reservei o horário. Para adiantar a ficha, me confirma seu nome completo e se o atendimento será particular ou por convênio."
    },
    {
      from: "user",
      time: "22:49",
      text: "Carlos Eduardo Mendes. Particular."
    },
    {
      from: "ayla",
      time: "22:50",
      text: "Obrigada, Carlos. A consulta está confirmada para amanhã, 08h30, com o Dr. Marcos. O CPF e a ficha são preenchidos na recepção."
    },
    {
      from: "ayla",
      time: "22:50",
      text: "A consulta é de avaliação: o profissional examina e explica as opções com você."
    },
    {
      from: "user",
      time: "22:50",
      text: "Entendi. Preciso levar algum documento?"
    },
    {
      from: "ayla",
      time: "22:50",
      text: "Sim, um documento com foto. A recepção confere seus dados na chegada."
    },
    {
      from: "user",
      time: "22:51",
      text: "E se a dor piorar antes da consulta?"
    },
    {
      from: "ayla",
      time: "22:51",
      text: "Responda esta mensagem. A equipe é avisada e orienta o próximo passo."
    },
    {
      from: "user",
      time: "22:51",
      text: "Combinado, obrigado."
    },
    {
      from: "ayla",
      time: "22:51",
      text: "Às ordens, Carlos. Até amanhã."
    }
  ];

  function initSimulator() {
    const sim = document.querySelector(".sim");
    if (!sim) return;

    const chat = sim.querySelector(".sim-chat");
    const status = sim.querySelector(".sim-status");
    const restart = sim.querySelector("#restartSimulatorBtn");
    if (!chat) return;

    const messages = sim.dataset.sim === "full" ? FULL_MESSAGES : HOME_MESSAGES;
    let run = 0;
    let started = false;

    function scrollChat() {
      chat.scrollTop = chat.scrollHeight;
    }

    function addMessage(message) {
      const bubble = document.createElement("div");
      bubble.className = "msg msg-" + message.from;

      const head = document.createElement("div");
      head.className = "msg-head";

      if (message.from === "ayla") {
        const logo = document.createElement("img");
        logo.src = "/assets/logo.png";
        logo.alt = "";
        logo.width = 14;
        logo.height = 14;
        head.appendChild(logo);
      }

      const author = document.createElement("span");
      author.className = "msg-author";
      author.textContent = message.from === "ayla" ? "Ayla" : "Você";
      head.appendChild(author);

      const time = document.createElement("span");
      time.className = "msg-time";
      time.textContent = message.time;
      head.appendChild(time);

      const body = document.createElement("p");
      body.className = "msg-body";
      body.textContent = message.text;

      bubble.appendChild(head);
      bubble.appendChild(body);
      chat.appendChild(bubble);
      scrollChat();
    }

    function addTyping() {
      const typing = document.createElement("div");
      typing.className = "msg-typing";
      typing.setAttribute("aria-label", "Ayla está digitando");
      for (let i = 0; i < 3; i += 1) typing.appendChild(document.createElement("i"));
      chat.appendChild(typing);
      scrollChat();
      return typing;
    }

    function finish() {
      if (status) {
        const toMinutes = function (value) {
          const parts = value.split(":");
          return Number(parts[0]) * 60 + Number(parts[1]);
        };
        const total = toMinutes(messages[messages.length - 1].time) - toMinutes(messages[0].time);
        status.textContent =
          "Fluxo concluído. Atendimento resolvido em " +
          (total > 0 ? total + " min." : "menos de 1 min.");
      }
      if (restart) restart.disabled = false;
    }

    function play(index, id) {
      if (id !== run) return;

      if (index >= messages.length) {
        finish();
        return;
      }

      const message = messages[index];

      if (message.from === "ayla") {
        if (status) status.textContent = "Ayla está digitando…";
        const typing = addTyping();
        window.setTimeout(function () {
          if (id !== run) return;
          typing.remove();
          addMessage(message);
          if (status) status.textContent = "Mensagem " + (index + 1) + " de " + messages.length;
          window.setTimeout(function () {
            play(index + 1, id);
          }, 1000);
        }, 900);
      } else {
        addMessage(message);
        if (status) status.textContent = "Mensagem " + (index + 1) + " de " + messages.length;
        window.setTimeout(function () {
          play(index + 1, id);
        }, 850);
      }
    }

    function start() {
      run += 1;
      const id = run;
      chat.innerHTML = "";
      if (restart) restart.disabled = true;
      if (status) status.textContent = "Conectando…";

      if (reduceMotion) {
        messages.forEach(addMessage);
        finish();
        return;
      }

      window.setTimeout(function () {
        play(0, id);
      }, 450);
    }

    if (restart) {
      restart.addEventListener("click", start);
    }

    if (reduceMotion) {
      messages.forEach(addMessage);
      finish();
      return;
    }

    if (!("IntersectionObserver" in window)) {
      start();
      return;
    }

    const observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting && !started) {
            started = true;
            start();
            observer.disconnect();
          }
        });
      },
      { threshold: 0.35 }
    );

    observer.observe(sim);
  }

  /* Calculadora ------------------------------------------------------------ */

  function initCalculator() {
    const calculator = document.querySelector(".calculator");
    if (!calculator) return;

    const contacts = calculator.querySelector('[data-calc="contacts"]');
    const ticket = calculator.querySelector('[data-calc="ticket"]');
    const rate = calculator.querySelector('[data-calc="rate"]');
    const contactsOut = calculator.querySelector("#lostContactsOut");
    const ticketOut = calculator.querySelector("#avgTicketOut");
    const rateOut = calculator.querySelector("#recoveryRateOut");
    const monthOut = calculator.querySelector("#calcMonth");
    const yearOut = calculator.querySelector("#calcYear");
    const rateLabel = calculator.querySelector("#calcRateLabel");

    if (!contacts || !ticket || !rate || !monthOut || !yearOut) return;

    const brl = new Intl.NumberFormat("pt-BR", {
      style: "currency",
      currency: "BRL",
      maximumFractionDigits: 0
    });

    function update() {
      const c = Number(contacts.value);
      const t = Number(ticket.value);
      const r = Number(rate.value);
      const month = c * t * (r / 100);

      if (contactsOut) contactsOut.textContent = String(c);
      if (ticketOut) ticketOut.textContent = brl.format(t);
      if (rateOut) rateOut.textContent = r + "%";
      if (rateLabel) rateLabel.textContent = r + "%";
      monthOut.textContent = brl.format(month);
      yearOut.textContent = brl.format(month * 12);
    }

    [contacts, ticket, rate].forEach(function (input) {
      input.addEventListener("input", update);
    });

    update();
  }

  /* Formulário ------------------------------------------------------------- */

  function applyPhoneMask(input) {
    input.addEventListener("input", function () {
      let value = input.value.replace(/\D/g, "");
      if (value.length > 11) value = value.slice(0, 11);

      if (value.length > 10) {
        input.value = "(" + value.slice(0, 2) + ") " + value.slice(2, 7) + "-" + value.slice(7, 11);
      } else if (value.length > 6) {
        input.value = "(" + value.slice(0, 2) + ") " + value.slice(2, 6) + "-" + value.slice(6);
      } else if (value.length > 2) {
        input.value = "(" + value.slice(0, 2) + ") " + value.slice(2);
      } else if (value.length > 0) {
        input.value = "(" + value;
      } else {
        input.value = "";
      }
    });
  }

  function initLeadForm() {
    const form = document.getElementById("leadForm");
    if (!form) return;

    const status = form.querySelector("#formStatus");
    const phone = form.querySelector('input[type="tel"]');
    if (phone) applyPhoneMask(phone);

    form.addEventListener("submit", function (event) {
      event.preventDefault();

      const name = (form.querySelector('[name="name"]').value || "").trim();
      const company = (form.querySelector('[name="company"]').value || "").trim();
      const segment = form.querySelector('[name="segment"]').value || "Não informado";
      const digits = phone ? phone.value.replace(/\D/g, "") : "";

      if (!name || digits.length < 10) {
        if (status) status.textContent = "Informe seu nome e um WhatsApp válido com DDD.";
        if (!name && form.querySelector('[name="name"]')) {
          form.querySelector('[name="name"]').focus();
        } else if (phone) {
          phone.focus();
        }
        return;
      }

      const submit = form.querySelector('button[type="submit"]');
      const originalLabel = submit ? submit.textContent : "";
      const honeypot = form.querySelector('[name="website"]');
      const controller = typeof AbortController !== "undefined" ? new AbortController() : null;
      const timer = window.setTimeout(function () {
        if (controller) controller.abort();
      }, 15000);

      if (status) status.textContent = "Enviando…";
      if (submit) {
        submit.disabled = true;
        submit.textContent = "Enviando…";
      }

      fetch("/api/lead", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name: name,
          company: company,
          segment: segment,
          phone: phone ? phone.value : "",
          website: honeypot ? honeypot.value : ""
        }),
        signal: controller ? controller.signal : undefined
      })
        .then(function (response) {
          return response.json().catch(function () { return {}; }).then(function (data) {
            return { ok: response.ok && data && data.ok };
          });
        })
        .then(function (result) {
          if (!result.ok) throw new Error("send_failed");
          if (status) status.textContent = "Recebido. Vamos chamar você no WhatsApp informado.";
          form.reset();
          if (submit) submit.textContent = "Enviado";
          try {
            window.dataLayer = window.dataLayer || [];
            window.dataLayer.push({ event: "lead_form_submit", segment: segment });
          } catch (error) {
            // Sem impacto no envio.
          }
          window.setTimeout(function () {
            if (submit) {
              submit.disabled = false;
              submit.textContent = originalLabel;
            }
            if (status) status.textContent = "";
          }, 6000);
        })
        .catch(function () {
          if (status) {
            status.textContent =
              "Não foi possível enviar agora. Tente de novo ou escreva para business@aylasystems.com.";
          }
          if (submit) {
            submit.disabled = false;
            submit.textContent = originalLabel;
          }
        })
        .then(function () {
          window.clearTimeout(timer);
        });
    });
  }

  /* Inicialização segura --------------------------------------------------- */

  function boot() {
    // Fallback: se alguna animação não disparar, o conteúdo aparece mesmo assim.
    window.setTimeout(function () {
      document.querySelectorAll(".reveal:not(.is-visible)").forEach(function (el) {
        el.classList.add("is-visible");
      });
    }, 700);

    [initHeader, initNav, initReveal, initAccordion, initTabs, initSimulator, initCalculator, initLeadForm].forEach(
      function (init) {
        try {
          init();
        } catch (error) {
          // Um bloco com problema não pode esconder o restante da página.
          console.error("Falha ao iniciar bloco do site:", error);
        }
      }
    );
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
