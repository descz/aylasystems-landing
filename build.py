#!/usr/bin/env python3
"""Gera as páginas estáticas do site da Ayla Systems.

Edite o conteúdo neste arquivo e rode `python3 build.py`.
Os arquivos HTML gerados são o que vai para a Vercel.
"""

from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parent
SITE = "https://aylasystems.com"
YEAR = "2026"


def asset_version(filename: str) -> str:
    return hashlib.sha256((ROOT / filename).read_bytes()).hexdigest()[:10]


def nav_link(href: str, label: str, active: str, slug: str) -> str:
    cls = ' class="is-active" aria-current="page"' if active == slug else ""
    return f'<a href="{href}"{cls} data-label="{label}"><span>{label}</span></a>'


def header(active: str) -> str:
    links = [
        ("/custo-da-demora", "Custo"),
        ("/mecanica", "Como funciona"),
        ("/segmentos", "Segmentos"),
        ("/demonstracao", "Demonstração"),
    ]
    nav = "\n        ".join(nav_link(href, label, active, href.strip("/")) for href, label in links)
    return f"""<a class="skip-link" href="#main">Pular para o conteúdo</a>
<div class="progress" aria-hidden="true"><span id="scrollProgress"></span></div>
<header class="site-header">
  <div class="container nav-wrap">
    <a class="brand" href="/" aria-label="Ayla Systems, página inicial">
      <img class="brand-mark" src="/assets/logo-header.png?v=[[CSSV]]" alt="" width="18" height="18">
      <span class="brand-type">AYLA<span>SYSTEMS</span></span>
    </a>
    <button class="nav-toggle" id="navToggle" type="button" aria-expanded="false" aria-controls="siteNav" aria-label="Abrir menu">
      <span></span><span></span>
    </button>
    <nav class="site-nav" id="siteNav" aria-label="Navegação principal">
        {nav}
        <a class="btn btn-primary btn-small nav-cta" href="/demonstracao">Testar a Ayla</a>
    </nav>
  </div>
</header>"""


FOOTER = f"""<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-brand">
      <a class="brand" href="/" aria-label="Ayla Systems, página inicial">
        <img class="brand-mark" src="/assets/logo-header.png?v=[[CSSV]]" alt="" width="38" height="38">
        <span class="brand-type">AYLA<span>SYSTEMS</span></span>
      </a>
      <p>Triagem, qualificação e agendamento no WhatsApp oficial. Atendimento 24/7 para empresas locais.</p>
      <a class="footer-mail" href="mailto:business@aylasystems.com">business@aylasystems.com</a>
    </div>
    <div class="footer-col">
      <h2>Plataforma</h2>
      <a href="/custo-da-demora">Custo da demora</a>
      <a href="/mecanica">Como funciona</a>
      <a href="/demonstracao">Demonstração</a>
      <a href="/segmentos">Segmentos</a>
    </div>
    <div class="footer-col">
      <h2>Segurança e legal</h2>
      <a href="/lgpd">LGPD</a>
      <a href="/seguranca">Segurança</a>
      <a href="/termos">Termos de uso</a>
      <a href="/privacidade">Privacidade</a>
    </div>
  </div>
  <div class="container footer-bottom">
    <span>© {YEAR} Ayla Systems. Todos os direitos reservados.</span>
    <span>LGPD · Lei nº 13.709/2018</span>
  </div>
</footer>"""


BASE = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>[[TITLE]]</title>
<meta name="description" content="[[DESC]]">
<link rel="canonical" href="{SITE}[[PATH]]">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="Ayla Systems">
<meta property="og:title" content="[[TITLE]]">
<meta property="og:description" content="[[DESC]]">
<meta property="og:url" content="{SITE}[[PATH]]">
<meta property="og:image" content="https://aylasystems.com/assets/icon-512.png">
<meta name="theme-color" content="#08090b">
<link rel="icon" href="/assets/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png">
<link rel="icon" type="image/png" sizes="48x48" href="/assets/favicon-48.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/styles.css?v=[[CSSV]]">
<script async src="https://www.googletagmanager.com/gtm.js?id=GTM-W75SXPVL"></script>
<script src="/analytics.js?v=[[ANV]]" defer></script>
<script src="/script.js?v=[[JSV]]" defer></script>
</head>
<body>
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-W75SXPVL" height="0" width="0" style="display:none;visibility:hidden" title="Google Tag Manager"></iframe></noscript>
[[HEADER]]
<main id="main">
[[BODY]]
</main>
[[FOOTER]]
</body>
</html>
"""


# ---------------------------------------------------------------------------
# Home
# ---------------------------------------------------------------------------

HOME = """
<section class="hero">
  <div class="container hero-inner">
    <span class="pill reveal"><span class="pill-dot" aria-hidden="true"></span>Atendimento 24/7 no WhatsApp oficial</span>
    <h1 class="reveal">Seu próximo cliente chega às 22h.<br><span class="metal">Sua equipe responde amanhã?</span></h1>
    <p class="lead reveal">A Ayla atende, qualifica e agenda no WhatsApp da sua empresa em segundos, inclusive fora do horário comercial, nos fins de semana e feriados.</p>
    <div class="actions reveal">
      <a class="btn btn-primary btn-large" href="/demonstracao">Ver demonstração</a>
      <a class="btn btn-ghost btn-large" href="/custo-da-demora">Calcular o custo da demora</a>
    </div>
    <p class="micro reveal">No mesmo número que você já usa · Implantação em até 72 horas</p>
  </div>
  <div class="container">
    <div class="stat-strip reveal">
      <div class="stat"><strong>&lt; 10s</strong><span>primeira resposta</span></div>
      <div class="stat"><strong>24/7</strong><span>todos os dias</span></div>
      <div class="stat"><strong>72h</strong><span>para entrar no ar</span></div>
      <div class="stat"><strong>100%</strong><span>API oficial do WhatsApp</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <span class="kicker">O vazamento</span>
      <h2>O anúncio funciona.<br>O atendimento perde o cliente.</h2>
      <p>Você paga por cada conversa. Se ninguém responde rápido, o lead esfria e fecha com quem respondeu primeiro.</p>
    </div>
    <div class="grid grid-3">
      <article class="card card-problem reveal">
        <span class="card-metric">Segundos</span>
        <h3>Primeira resposta</h3>
        <p>A Ayla responde no mesmo instante, a qualquer hora, sem fila e sem depender de quem está de plantão.</p>
      </article>
      <article class="card card-problem reveal">
        <span class="card-metric">24/7</span>
        <h3>Fora do horário comercial</h3>
        <p>À noite, nos fins de semana e em feriados, o contato continua sendo atendido e qualificado.</p>
      </article>
      <article class="card card-problem reveal">
        <span class="card-metric">Sem fila</span>
        <h3>Recepção sobrecarregada</h3>
        <p>Horário, preço, endereço e convênio saem do telefone da equipe e passam a ser respondidos pela Ayla.</p>
      </article>
    </div>
    <p class="note reveal">Referências de mercado usadas para dimensionar o problema. Resultados variam por operação.</p>
    <div class="center reveal"><a class="text-link" href="/custo-da-demora">Entender o custo real <span aria-hidden="true">→</span></a></div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head reveal">
      <span class="kicker">Como funciona</span>
      <h2>Três passos. Nenhuma mudança no seu número.</h2>
      <p>A Ayla entra no WhatsApp que sua empresa já usa, aprende suas regras e assume a triagem.</p>
    </div>
    <ol class="steps">
      <li class="step reveal">
        <span class="step-index">01</span>
        <h3>Mapeamos</h3>
        <p>Procedimentos, critérios de triagem, agenda e tom de voz. Nada de resposta genérica.</p>
      </li>
      <li class="step reveal">
        <span class="step-index">02</span>
        <h3>Homologamos</h3>
        <p>Conectamos ao seu número oficial e testamos cada caminho do fluxo em até 72 horas.</p>
      </li>
      <li class="step reveal">
        <span class="step-index">03</span>
        <h3>Atendemos</h3>
        <p>A Ayla responde, qualifica e agenda. Quando o caso exige, chama um humano com o histórico.</p>
      </li>
    </ol>
    <div class="center reveal"><a class="text-link" href="/mecanica">Ver a implantação em detalhe <span aria-hidden="true">→</span></a></div>
  </div>
</section>

<section class="section" id="simulador">
  <div class="container">
    <div class="section-head reveal">
      <span class="kicker">Demonstração</span>
      <h2>Domingo, 22h47.<br>A Ayla está acordada.</h2>
      <p>Um contato vindo de anúncio pede atendimento de urgência. Acompanhe o fluxo.</p>
    </div>
    <div class="sim reveal" data-sim="home">
      <div class="sim-head">
        <span class="sim-title">WhatsApp · atendimento em tempo real</span>
        <span class="sim-time">DOM 22:47</span>
      </div>
      <div class="sim-chat" id="chatStream" aria-live="polite" aria-label="Simulação de conversa no WhatsApp"></div>
      <div class="sim-foot">
        <span id="simStatus" class="sim-status">Preparando conversa…</span>
        <button class="btn btn-ghost btn-small" id="restartSimulatorBtn" type="button">Repetir</button>
      </div>
    </div>
    <div class="center reveal"><a class="text-link" href="/demonstracao">Abrir demonstração completa <span aria-hidden="true">→</span></a></div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head reveal">
      <span class="kicker">Segmentos</span>
      <h2>Para quem o tempo de resposta é receita.</h2>
      <p>A mesma infraestrutura, calibrada para o protocolo de cada setor.</p>
    </div>
    <div class="tabs reveal" role="tablist" aria-label="Segmentos de atendimento">
      <button class="tab is-active" type="button" role="tab" aria-selected="true" aria-controls="panel-clinicas" id="tab-clinicas" data-tab="clinicas">Clínicas</button>
      <button class="tab" type="button" role="tab" aria-selected="false" aria-controls="panel-advocacia" id="tab-advocacia" data-tab="advocacia" tabindex="-1">Advocacia</button>
      <button class="tab" type="button" role="tab" aria-selected="false" aria-controls="panel-imobiliarias" id="tab-imobiliarias" data-tab="imobiliarias" tabindex="-1">Imobiliárias</button>
      <button class="tab" type="button" role="tab" aria-selected="false" aria-controls="panel-ticket" id="tab-ticket" data-tab="ticket" tabindex="-1">Alto ticket</button>
    </div>
    <div class="tab-panels reveal">
      <div class="tab-panel is-active" role="tabpanel" id="panel-clinicas" aria-labelledby="tab-clinicas" data-panel="clinicas">
        <h3>Clínicas e consultórios</h3>
        <p>Triagem de especialidade, convênio e urgência. Agendamento na grade de cada profissional e confirmação para reduzir faltas.</p>
        <ul class="checklist">
          <li>Pré-triagem de urgência</li>
          <li>Agendamento por profissional</li>
          <li>Confirmação e lembrete</li>
        </ul>
      </div>
      <div class="tab-panel" role="tabpanel" id="panel-advocacia" aria-labelledby="tab-advocacia" data-panel="advocacia" hidden>
        <h3>Escritórios de advocacia</h3>
        <p>Pré-qualificação por área, coleta de dados e agendamento da consulta inicial. Contatos fora do perfil são filtrados.</p>
        <ul class="checklist">
          <li>Triagem por área de atuação</li>
          <li>Coleta inicial de documentos</li>
          <li>Agenda da equipe jurídica</li>
        </ul>
      </div>
      <div class="tab-panel" role="tabpanel" id="panel-imobiliarias" aria-labelledby="tab-imobiliarias" data-panel="imobiliarias" hidden>
        <h3>Imobiliárias e corretores</h3>
        <p>Resposta imediata aos contatos de portais e anúncios. Bairro, faixa de orçamento e metragem coletados antes da visita.</p>
        <ul class="checklist">
          <li>Atendimento a leads de portais</li>
          <li>Ficha técnica do imóvel</li>
          <li>Visita na agenda do corretor</li>
        </ul>
      </div>
      <div class="tab-panel" role="tabpanel" id="panel-ticket" aria-labelledby="tab-ticket" data-panel="ticket" hidden>
        <h3>Serviços de alto ticket</h3>
        <p>Qualificação de orçamento antes do especialista, atendimento simultâneo e transbordo para o fechamento humano.</p>
        <ul class="checklist">
          <li>Filtro de orçamento</li>
          <li>Vários atendimentos ao mesmo tempo</li>
          <li>Transbordo com contexto</li>
        </ul>
      </div>
    </div>
    <div class="center reveal"><a class="text-link" href="/segmentos">Ver todos os segmentos <span aria-hidden="true">→</span></a></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <span class="kicker">Confiança</span>
      <h2>Tecnologia oficial. Operação responsável.</h2>
      <p>Sem automação irregular, sem número novo e sem dados além do necessário.</p>
    </div>
    <div class="grid grid-3">
      <article class="card reveal">
        <h3>API oficial do WhatsApp</h3>
        <p>Operação pela API corporativa. Sem risco de bloqueio por automação irregular.</p>
      </article>
      <article class="card reveal">
        <h3>LGPD desde o desenho</h3>
        <p>Dados mínimos, acesso restrito e registro auditável de cada atendimento.</p>
      </article>
      <article class="card reveal">
        <h3>Humano no comando</h3>
        <p>Quando o caso foge do roteiro, a equipe assume com o histórico completo.</p>
      </article>
    </div>
    <div class="center reveal"><a class="text-link" href="/seguranca">Segurança e conformidade <span aria-hidden="true">→</span></a></div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head reveal">
      <span class="kicker">Perguntas frequentes</span>
      <h2>Perguntas diretas.</h2>
      <p>O que todo empresário pergunta antes de testar.</p>
    </div>
    <div class="accordion reveal">
      <div class="acc-item">
        <button class="acc-btn" type="button" aria-expanded="false"><span>Preciso trocar o número de WhatsApp?</span><span class="acc-icon" aria-hidden="true"></span></button>
        <div class="acc-panel"><div class="acc-inner"><p>Não. A integração usa o número que sua empresa já divulga. Você não perde o histórico nem precisa comprar outro chip.</p></div></div>
      </div>
      <div class="acc-item">
        <button class="acc-btn" type="button" aria-expanded="false"><span>A Ayla substitui minha equipe?</span><span class="acc-icon" aria-hidden="true"></span></button>
        <div class="acc-panel"><div class="acc-inner"><p>Não. Ela assume o repetitivo e os horários sem equipe. Sua recepção fica livre para casos complexos, negociação e atendimento presencial.</p></div></div>
      </div>
      <div class="acc-item">
        <button class="acc-btn" type="button" aria-expanded="false"><span>E se a pergunta fugir do roteiro?</span><span class="acc-icon" aria-hidden="true"></span></button>
        <div class="acc-panel"><div class="acc-inner"><p>A Ayla não inventa. Ela registra a solicitação, avisa o cliente e encaminha o caso para um humano com o histórico da conversa.</p></div></div>
      </div>
      <div class="acc-item">
        <button class="acc-btn" type="button" aria-expanded="false"><span>A solução respeita a LGPD?</span><span class="acc-icon" aria-hidden="true"></span></button>
        <div class="acc-panel"><div class="acc-inner"><p>Sim. O tratamento segue a Lei nº 13.709/2018, com coleta mínima, acesso restrito e direitos do titular garantidos. Veja os detalhes na <a href="/lgpd">página de LGPD</a>.</p></div></div>
      </div>
      <div class="acc-item">
        <button class="acc-btn" type="button" aria-expanded="false"><span>Quanto tempo leva para entrar no ar?</span><span class="acc-icon" aria-hidden="true"></span></button>
        <div class="acc-panel"><div class="acc-inner"><p>Até 72 horas após a validação das regras de negócio e da tabela de serviços.</p></div></div>
      </div>
      <div class="acc-item">
        <button class="acc-btn" type="button" aria-expanded="false"><span>Como funciona a demonstração?</span><span class="acc-icon" aria-hidden="true"></span></button>
        <div class="acc-panel"><div class="acc-inner"><p>Você recebe um fluxo de teste no seu WhatsApp e conversa com a Ayla como um cliente. Sem reunião e sem instalação.</p></div></div>
      </div>
    </div>
  </div>
</section>

<section class="section cta-section">
  <div class="container">
    <div class="cta-box reveal">
      <span class="kicker">Teste antes de decidir</span>
      <h2>Converse com a Ayla no seu próprio WhatsApp.</h2>
      <p>Sem reunião e sem instalação. Você recebe o fluxo, testa e decide.</p>
      <div class="actions">
        <a class="btn btn-primary btn-large" href="/demonstracao">Solicitar demonstração</a>
        <a class="btn btn-ghost btn-large" href="mailto:business@aylasystems.com">Falar por e-mail</a>
      </div>
      <p class="micro">Atendimento para empresas no Brasil.</p>
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Custo da demora
# ---------------------------------------------------------------------------

CUSTO = """
<section class="page-hero">
  <div class="container">
    <span class="kicker reveal">Diagnóstico</span>
    <h1 class="reveal">Quanto custa deixar um cliente esperando?</h1>
    <p class="lead reveal">O prejuízo não aparece no extrato. Ele aparece na agenda vazia e no anúncio que parece caro.</p>
  </div>
</section>

<section class="section section-tight">
  <div class="container">
    <div class="calculator reveal">
      <div class="calc-controls">
        <h2>Faça a conta do seu mês.</h2>
        <p>Ajuste os três números. A simulação usa apenas o que você informar.</p>
        <div class="calc-field">
          <div class="calc-label"><label for="lostContacts">Contatos perdidos por mês</label><output id="lostContactsOut" for="lostContacts">40</output></div>
          <input type="range" id="lostContacts" min="10" max="200" step="5" value="40" data-calc="contacts">
        </div>
        <div class="calc-field">
          <div class="calc-label"><label for="avgTicket">Ticket médio</label><output id="avgTicketOut" for="avgTicket">R$ 800</output></div>
          <input type="range" id="avgTicket" min="200" max="5000" step="50" value="800" data-calc="ticket">
        </div>
        <div class="calc-field">
          <div class="calc-label"><label for="recoveryRate">Taxa de recuperação com a Ayla</label><output id="recoveryRateOut" for="recoveryRate">40%</output></div>
          <input type="range" id="recoveryRate" min="20" max="80" step="5" value="40" data-calc="rate">
        </div>
      </div>
      <div class="calc-result" aria-live="polite">
        <span class="kicker">Receita recuperável</span>
        <strong id="calcMonth">R$ 12.800</strong>
        <span class="calc-period">por mês</span>
        <div class="calc-year"><span id="calcYear">R$ 153.600</span> em 12 meses</div>
        <p class="calc-note">Simulação com taxa de recuperação de <span id="calcRateLabel">40%</span>. Não é promessa de resultado.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head reveal">
      <span class="kicker">As três falhas</span>
      <h2>Onde o dinheiro vaza.</h2>
      <p>Não é falta de lead. É falta de resposta no momento em que o lead está pronto.</p>
    </div>
    <div class="grid grid-3">
      <article class="card card-problem reveal">
        <span class="card-metric">Segundos</span>
        <h3>Resposta lenta</h3>
        <p>Cada minuto de espera esfria o contato. A Ayla responde no mesmo instante, antes que ele procure outra empresa.</p>
      </article>
      <article class="card card-problem reveal">
        <span class="card-metric">24/7</span>
        <h3>Vácuo noturno</h3>
        <p>À noite e nos fins de semana, o contato chega e ninguém responde. A Ayla atende e qualifica fora do expediente.</p>
      </article>
      <article class="card card-problem reveal">
        <span class="card-metric">Sem fila</span>
        <h3>Recepção sobrecarregada</h3>
        <p>Horário, preço, endereço e convênio consomem o expediente. A Ayla assume essas respostas e libera a equipe.</p>
      </article>
    </div>
    <p class="note reveal">Referências de mercado usadas para dimensionar o problema. Resultados variam por operação.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <span class="kicker">Antes e depois</span>
      <h2>A diferença está no primeiro minuto.</h2>
    </div>
    <div class="grid grid-2">
      <article class="card card-compare reveal">
        <span class="compare-tag">Sem a Ayla</span>
        <ul class="compare-list">
          <li>O contato das 22h fica para amanhã.</li>
          <li>A triagem depende de quem está na recepção.</li>
          <li>O horário é confirmado por telefone, depois.</li>
          <li>Os dados ficam espalhados em papel e planilha.</li>
        </ul>
      </article>
      <article class="card card-compare card-compare-good reveal">
        <span class="compare-tag">Com a Ayla</span>
        <ul class="compare-list">
          <li>Resposta em segundos, a qualquer hora.</li>
          <li>Triagem padronizada com as suas regras.</li>
          <li>Horário bloqueado na agenda na hora.</li>
          <li>Um registro único por atendimento.</li>
        </ul>
      </article>
    </div>
    <div class="center reveal"><a class="btn btn-primary btn-large" href="/demonstracao">Testar a Ayla no WhatsApp</a></div>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Mecânica
# ---------------------------------------------------------------------------

MECANICA = """
<section class="page-hero">
  <div class="container">
    <span class="kicker reveal">Implantação</span>
    <h1 class="reveal">Do primeiro ajuste ao atendimento no ar em 72 horas.</h1>
    <p class="lead reveal">Sem trocar de número, sem parar a operação e sem projeto de seis meses.</p>
  </div>
</section>

<section class="section section-tight">
  <div class="container">
    <ol class="timeline">
      <li class="timeline-item reveal">
        <span class="timeline-dot" aria-hidden="true"></span>
        <span class="timeline-time">Dia 0 · Diagnóstico</span>
        <h2>Entendemos a sua operação.</h2>
        <p>Serviços, critérios de triagem, agenda, objeções e tom de voz. O fluxo nasce das suas regras, não de um modelo genérico.</p>
      </li>
      <li class="timeline-item reveal">
        <span class="timeline-dot" aria-hidden="true"></span>
        <span class="timeline-time">Dia 1 · Desenho</span>
        <h2>Escrevemos o fluxo.</h2>
        <p>Você valida cada caminho: saudação, qualificação, valores, agendamento, imprevistos e transbordo humano.</p>
      </li>
      <li class="timeline-item reveal">
        <span class="timeline-dot" aria-hidden="true"></span>
        <span class="timeline-time">Dia 2 · Homologação</span>
        <h2>Conectamos ao número oficial.</h2>
        <p>Testamos as perguntas reais, os horários da agenda e as situações de exceção. Nada entra no ar sem passar pelo teste.</p>
      </li>
      <li class="timeline-item reveal">
        <span class="timeline-dot" aria-hidden="true"></span>
        <span class="timeline-time">Dia 3 · Go live</span>
        <h2>A Ayla assume 24/7.</h2>
        <p>Sua equipe acompanha os atendimentos e pode intervir a qualquer momento. O número continua o mesmo.</p>
      </li>
    </ol>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head reveal">
      <span class="kicker">O que fica pronto</span>
      <h2>Sem obra, sem chip novo, sem aplicativo.</h2>
    </div>
    <ul class="checklist checklist-grid reveal">
      <li>Seu número atual, sem troca</li>
      <li>Histórico de conversas preservado</li>
      <li>Nenhum aplicativo para instalar</li>
      <li>Sem menu de "digite 1 ou 2"</li>
      <li>Transbordo humano com contexto</li>
      <li>Registro de cada atendimento</li>
    </ul>
    <div class="callout reveal">
      <p><strong>A implantação não para sua operação.</strong> O número continua funcionando normalmente enquanto o fluxo é testado.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="cta-box reveal">
      <span class="kicker">Próximo passo</span>
      <h2>Veja o fluxo funcionando antes de contratar.</h2>
      <p>A demonstração é gratuita e chega no seu WhatsApp.</p>
      <div class="actions"><a class="btn btn-primary btn-large" href="/demonstracao">Solicitar demonstração</a></div>
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Demonstração
# ---------------------------------------------------------------------------

DEMO = """
<section class="page-hero">
  <div class="container">
    <span class="kicker reveal">Demonstração</span>
    <h1 class="reveal">Converse com a Ayla antes de contratar.</h1>
    <p class="lead reveal">Um fluxo real no seu WhatsApp. Sem reunião, sem slides e sem instalação.</p>
  </div>
</section>

<section class="section section-tight">
  <div class="container">
    <div class="sim sim-large reveal" data-sim="full">
      <div class="sim-head">
        <span class="sim-title">WhatsApp · fluxo de triagem</span>
        <span class="sim-time">DOM 22:47</span>
      </div>
      <div class="sim-chat" id="chatStream" aria-live="polite" aria-label="Simulação de conversa no WhatsApp"></div>
      <div class="sim-foot">
        <span id="simStatus" class="sim-status">Preparando conversa…</span>
        <button class="btn btn-ghost btn-small" id="restartSimulatorBtn" type="button">Repetir</button>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="split">
      <div class="split-copy reveal">
        <span class="kicker">Receber o teste</span>
        <h2>Quero testar no meu WhatsApp.</h2>
        <p>Preencha os dados. A equipe recebe seu contato e responde pelo WhatsApp informado.</p>
        <ul class="checklist">
          <li>Demonstração gratuita</li>
          <li>Sem reunião e sem instalação</li>
          <li>Você testa como um cliente</li>
        </ul>
        <p class="note">Prefere escrever direto? <a href="mailto:business@aylasystems.com">business@aylasystems.com</a></p>
      </div>
      <form class="form-card reveal" id="leadForm" novalidate>
        <div class="field">
          <label for="leadName">Nome</label>
          <input id="leadName" name="name" type="text" autocomplete="name" placeholder="Seu nome" required>
        </div>
        <div class="field">
          <label for="leadCompany">Empresa</label>
          <input id="leadCompany" name="company" type="text" autocomplete="organization" placeholder="Nome da empresa">
        </div>
        <div class="field">
          <label for="leadSegment">Segmento</label>
          <select id="leadSegment" name="segment">
            <option>Clínica / Odontologia</option>
            <option>Advocacia</option>
            <option>Imobiliária</option>
            <option>Serviços de alto ticket</option>
            <option>Outro</option>
          </select>
        </div>
        <div class="field">
          <label for="leadPhone">WhatsApp com DDD</label>
          <input id="leadPhone" name="phone" type="tel" inputmode="tel" autocomplete="tel" placeholder="(19) 99999-9999" required>
        </div>
        <div class="hp-field" aria-hidden="true">
          <label for="leadWebsite">Não preencha este campo</label>
          <input id="leadWebsite" name="website" type="text" tabindex="-1" autocomplete="off">
        </div>
        <button class="btn btn-primary btn-large" type="submit">Solicitar demonstração</button>
        <p class="form-note">Ao enviar, você autoriza o contato pelo WhatsApp informado. Seus dados são usados apenas para este atendimento.</p>
        <p class="form-status" id="formStatus" role="status" aria-live="polite"></p>
      </form>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <span class="kicker">Antes do teste</span>
      <h2>O que você precisa saber.</h2>
    </div>
    <div class="grid grid-3">
      <article class="card reveal"><h3>É gratuito?</h3><p>Sim. A demonstração existe para você avaliar o fluxo antes de qualquer contratação.</p></article>
      <article class="card reveal"><h3>Preciso instalar algo?</h3><p>Não. Você conversa pelo WhatsApp, no mesmo celular que já usa.</p></article>
      <article class="card reveal"><h3>Vou falar com um robô?</h3><p>Com a Ayla. Se o caso fugir do roteiro, um humano assume com o histórico.</p></article>
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Segmentos
# ---------------------------------------------------------------------------

SEGMENTOS = """
<section class="page-hero">
  <div class="container">
    <span class="kicker reveal">Segmentos</span>
    <h1 class="reveal">Cada setor tem seu protocolo. A Ayla aprende o seu.</h1>
    <p class="lead reveal">A mesma infraestrutura, calibrada para a triagem e a agenda da sua empresa.</p>
  </div>
</section>

<section class="section section-tight">
  <div class="container">
    <div class="tabs reveal" role="tablist" aria-label="Segmentos de atendimento">
      <button class="tab is-active" type="button" role="tab" aria-selected="true" aria-controls="panel-clinicas" id="tab-clinicas" data-tab="clinicas">Clínicas</button>
      <button class="tab" type="button" role="tab" aria-selected="false" aria-controls="panel-advocacia" id="tab-advocacia" data-tab="advocacia" tabindex="-1">Advocacia</button>
      <button class="tab" type="button" role="tab" aria-selected="false" aria-controls="panel-imobiliarias" id="tab-imobiliarias" data-tab="imobiliarias" tabindex="-1">Imobiliárias</button>
      <button class="tab" type="button" role="tab" aria-selected="false" aria-controls="panel-ticket" id="tab-ticket" data-tab="ticket" tabindex="-1">Alto ticket</button>
    </div>
    <div class="tab-panels reveal">
      <div class="tab-panel tab-panel-large is-active" role="tabpanel" id="panel-clinicas" aria-labelledby="tab-clinicas" data-panel="clinicas">
        <span class="kicker">Saúde e odontologia</span>
        <h2>O paciente com dor não espera até amanhã.</h2>
        <p>Triagem de especialidade, convênio e urgência. A Ayla identifica o caso, mostra os horários disponíveis e bloqueia a consulta na agenda do profissional certo.</p>
        <h3>O que ela resolve</h3>
        <ul class="checklist">
          <li>Pré-triagem de urgência e especialidade</li>
          <li>Agendamento na grade de cada profissional</li>
          <li>Confirmação e lembrete para reduzir faltas</li>
        </ul>
        <p class="result-line">Resultado: menos contatos perdidos e agenda mais cheia.</p>
      </div>
      <div class="tab-panel tab-panel-large" role="tabpanel" id="panel-advocacia" aria-labelledby="tab-advocacia" data-panel="advocacia" hidden>
        <span class="kicker">Jurídico</span>
        <h2>O caso certo, na mesa do advogado certo.</h2>
        <p>Pré-qualificação por área, coleta de dados e agendamento da consulta inicial. Contatos fora do perfil são filtrados antes de consumir tempo da equipe.</p>
        <h3>O que ela resolve</h3>
        <ul class="checklist">
          <li>Triagem por área de atuação</li>
          <li>Coleta inicial de documentos e dados</li>
          <li>Agenda da equipe jurídica</li>
        </ul>
        <p class="result-line">Resultado: menos curiosos e mais reuniões qualificadas.</p>
      </div>
      <div class="tab-panel tab-panel-large" role="tabpanel" id="panel-imobiliarias" aria-labelledby="tab-imobiliarias" data-panel="imobiliarias" hidden>
        <span class="kicker">Mercado imobiliário</span>
        <h2>O lead do portal não pode esfriar.</h2>
        <p>Resposta imediata aos contatos de portais e anúncios. A Ayla coleta bairro, faixa de orçamento e metragem antes de agendar a visita com o corretor.</p>
        <h3>O que ela resolve</h3>
        <ul class="checklist">
          <li>Atendimento a leads de portais</li>
          <li>Ficha técnica do imóvel</li>
          <li>Visita na agenda do corretor</li>
        </ul>
        <p class="result-line">Resultado: menos visitas improdutivas e mais propostas.</p>
      </div>
      <div class="tab-panel tab-panel-large" role="tabpanel" id="panel-ticket" aria-labelledby="tab-ticket" data-panel="ticket" hidden>
        <span class="kicker">Serviços de alto ticket</span>
        <h2>O especialista só entra quando vale a pena.</h2>
        <p>Qualificação de orçamento antes do atendimento humano, vários contatos ao mesmo tempo e transbordo com contexto para o fechamento.</p>
        <h3>O que ela resolve</h3>
        <ul class="checklist">
          <li>Filtro de orçamento e perfil</li>
          <li>Atendimento simultâneo sem fila</li>
          <li>Transbordo com histórico para o humano</li>
        </ul>
        <p class="result-line">Resultado: menos tempo perdido e mais negociação.</p>
      </div>
    </div>
    <div class="center reveal"><a class="btn btn-primary btn-large" href="/demonstracao">Testar no meu segmento</a></div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="cta-box reveal">
      <span class="kicker">Outro setor</span>
      <h2>Se o seu cliente chega pelo WhatsApp, a lógica é a mesma.</h2>
      <p>Conte como a sua operação funciona. A gente desenha a triagem.</p>
      <div class="actions"><a class="btn btn-primary btn-large" href="mailto:business@aylasystems.com">Falar com a Ayla</a></div>
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Segurança
# ---------------------------------------------------------------------------

SEGURANCA = """
<section class="page-hero">
  <div class="container">
    <span class="kicker reveal">Segurança</span>
    <h1 class="reveal">Tecnologia oficial. Operação responsável.</h1>
    <p class="lead reveal">A Ayla opera pela API corporativa do WhatsApp e trata cada conversa como dado sensível.</p>
  </div>
</section>

<section class="section section-tight">
  <div class="container">
    <div class="grid grid-3">
      <article class="card reveal"><h3>API oficial</h3><p>Operação pela API corporativa do WhatsApp. Sem automação irregular e sem risco de bloqueio por uso indevido.</p></article>
      <article class="card reveal"><h3>Criptografia em trânsito</h3><p>Todo o tráfego entre navegador, servidores e API usa TLS. Credenciais ficam fora do código e do navegador.</p></article>
      <article class="card reveal"><h3>Dados mínimos</h3><p>Coletamos apenas o necessário para triagem, agendamento e suporte. Nada de formulário com campo sobrando.</p></article>
      <article class="card reveal"><h3>Acesso restrito</h3><p>Conversas e credenciais ficam limitadas à operação. Cada acesso é feito por pessoa autorizada.</p></article>
      <article class="card reveal"><h3>Registro auditável</h3><p>Cada atendimento gera histórico para revisão, correção e comprovação do que foi combinado.</p></article>
      <article class="card reveal"><h3>Transbordo humano</h3><p>Casos fora do roteiro vão para a equipe com o contexto completo. A automação não decide sozinha.</p></article>
    </div>
    <div class="callout reveal">
      <p><strong>Transparência técnica:</strong> a criptografia ponta a ponta do WhatsApp se aplica às conversas entre usuários. Na API Business, a integração usa TLS entre os sistemas envolvidos.</p>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head reveal">
      <span class="kicker">LGPD</span>
      <h2>Privacidade não é rodapé.</h2>
      <p>Coleta mínima, finalidade definida e direitos do titular garantidos. A política completa está na página de LGPD.</p>
    </div>
    <div class="center reveal"><a class="text-link" href="/lgpd">Ler a política de LGPD <span aria-hidden="true">→</span></a></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="cta-box reveal">
      <span class="kicker">Dúvida técnica</span>
      <h2>Quer entender como a integração funciona?</h2>
      <p>Pergunte antes de contratar. A resposta é direta, sem apresentação de vendas.</p>
      <div class="actions"><a class="btn btn-primary btn-large" href="mailto:business@aylasystems.com">Falar por e-mail</a></div>
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# LGPD
# ---------------------------------------------------------------------------

LGPD = """
<section class="page-hero">
  <div class="container">
    <span class="kicker reveal">Privacidade</span>
    <h1 class="reveal">Conformidade com a LGPD.</h1>
    <p class="lead reveal">Como a Ayla Systems trata dados pessoais no site e na operação de atendimento.</p>
  </div>
</section>

<section class="section section-tight">
  <div class="container legal">
    <p class="legal-meta">Última atualização: 21 de novembro de 2026</p>

    <h2>1. Quem é o controlador</h2>
    <p>A Ayla Systems é a controladora dos dados pessoais tratados neste site e na prestação do serviço de triagem e agendamento. O contato do encarregado de dados é <a href="mailto:business@aylasystems.com">business@aylasystems.com</a>.</p>

    <h2>2. Dados que podem ser tratados</h2>
    <p>No site, coletamos apenas os dados que você envia voluntariamente: nome, empresa, segmento, WhatsApp e o conteúdo da mensagem. Na operação, podem ser tratados nome, telefone, e-mail, empresa, histórico de conversa, preferências de horário e dados necessários ao agendamento.</p>
    <p>Dados sensíveis, como informações de saúde, só são tratados quando indispensáveis ao atendimento e com base legal adequada. A Ayla não pede CPF no site e não solicita dados que não sejam necessários ao fluxo.</p>

    <h2>3. Para que usamos</h2>
    <ul>
      <li>Responder contatos e enviar a demonstração solicitada.</li>
      <li>Realizar triagem, qualificação e agendamento.</li>
      <li>Prestar suporte e manter o histórico do atendimento.</li>
      <li>Cumprir obrigações legais e regulatórias.</li>
      <li>Melhorar o serviço com base em dados agregados, quando possível.</li>
    </ul>

    <h2>4. Base legal</h2>
    <p>O tratamento pode se apoiar em execução de contrato ou procedimentos preliminares, consentimento do titular, cumprimento de obrigação legal, legítimo interesse para segurança e melhoria do serviço, e proteção da vida ou da saúde quando aplicável.</p>

    <h2>5. Compartilhamento</h2>
    <p>Os dados podem ser compartilhados com a Meta/WhatsApp, para operar o canal oficial, e com provedores de infraestrutura e hospedagem estritamente necessários à prestação do serviço. Não vendemos dados pessoais.</p>

    <h2>6. Retenção</h2>
    <p>Mantemos os dados pelo tempo necessário à finalidade, ao contrato e aos prazos legais. Depois disso, os registros são eliminados ou anonimizados, salvo quando a lei exigir guarda.</p>

    <h2>7. Direitos do titular</h2>
    <p>Você pode solicitar confirmação de tratamento, acesso, correção, anonimização, bloqueio, eliminação, portabilidade, informação sobre compartilhamento e revogação do consentimento. Para exercer, escreva para <a href="mailto:business@aylasystems.com">business@aylasystems.com</a>.</p>

    <h2>8. Segurança</h2>
    <p>Adotamos controle de acesso, criptografia em trânsito e registro de operações. Nenhum sistema é imune a incidentes; se ocorrer um incidente relevante, comunicaremos os titulares e a ANPD conforme a lei.</p>

    <h2>9. Alterações</h2>
    <p>Esta política pode ser atualizada. A data no topo indica a versão vigente. Mudanças relevantes serão comunicadas nos canais oficiais.</p>

    <p class="legal-note">Este documento é a política institucional da Ayla Systems para o site e o serviço. Contratos específicos podem trazer regras adicionais de tratamento e retenção.</p>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Termos
# ---------------------------------------------------------------------------

TERMOS = """
<section class="page-hero">
  <div class="container">
    <span class="kicker reveal">Legal</span>
    <h1 class="reveal">Termos de uso.</h1>
    <p class="lead reveal">Regras para uso deste site e da demonstração da Ayla Systems.</p>
  </div>
</section>

<section class="section section-tight">
  <div class="container legal">
    <p class="legal-meta">Última atualização: 21 de novembro de 2026</p>

    <h2>1. Uso do site</h2>
    <p>Este site é institucional. Ao navegar, você concorda em usá-lo de forma lícita, sem tentar interferir na segurança, na disponibilidade ou no funcionamento dos sistemas.</p>

    <h2>2. Demonstração</h2>
    <p>A demonstração é gratuita e serve para apresentar o fluxo de triagem. Ela não cria, por si só, obrigação de contratação. As condições comerciais são definidas em proposta ou contrato específico.</p>

    <h2>3. Propriedade intelectual</h2>
    <p>Marca, textos, layout, código e materiais deste site pertencem à Ayla Systems ou são usados com autorização. É proibida a reprodução comercial sem consentimento prévio por escrito.</p>

    <h2>4. Conteúdo e links de terceiros</h2>
    <p>Links para sites de terceiros são oferecidos por conveniência. Não controlamos o conteúdo, as práticas ou a disponibilidade desses sites.</p>

    <h2>5. Limitação de responsabilidade</h2>
    <p>As informações do site têm caráter informativo. A Ayla Systems não responde por decisões tomadas exclusivamente com base nelas, nem por indisponibilidades causadas por terceiros, caso fortuito ou força maior.</p>

    <h2>6. Resultados</h2>
    <p>Estimativas e simulações apresentadas no site são ilustrativas. Resultados variam conforme volume de contatos, ticket médio, operação e mercado. Não há promessa de faturamento ou de número de vendas.</p>

    <h2>7. Alterações</h2>
    <p>Estes termos podem ser atualizados a qualquer momento. A versão vigente é sempre a publicada nesta página.</p>

    <h2>8. Legislação e contato</h2>
    <p>Aplica-se a legislação brasileira. Dúvidas sobre estes termos podem ser enviadas para <a href="mailto:business@aylasystems.com">business@aylasystems.com</a>.</p>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Privacidade
# ---------------------------------------------------------------------------

PRIVACIDADE = """
<section class="page-hero">
  <div class="container">
    <span class="kicker reveal">Privacidade</span>
    <h1 class="reveal">Política de privacidade do site.</h1>
    <p class="lead reveal">O que este site coleta, para que serve e como você pode exercer seus direitos.</p>
  </div>
</section>

<section class="section section-tight">
  <div class="container legal">
    <p class="legal-meta">Última atualização: 21 de novembro de 2026</p>

    <h2>1. Dados coletados</h2>
    <p>Este site não possui cadastro, login ou área de cliente. Os dados enviados são apenas os que você digita no formulário de demonstração ou envia por e-mail: nome, empresa, segmento e WhatsApp.</p>

    <h2>2. Cookies e analytics</h2>
    <p>O site usa o Google Tag Manager para carregar tags de medição, entre elas o Google Analytics 4. A ferramenta grava cookies próprios (como <code>_ga</code> e <code>_ga_</code>) e envia dados de navegação — páginas visitadas, origem do acesso, tipo de dispositivo e localização aproximada — para servidores do Google, que podem estar fora do Brasil. Não usamos esses dados para identificar você individualmente nem para publicidade.</p>
    <p>Para recusar, bloqueie cookies de terceiros no navegador ou instale o complemento de desativação do Google Analytics em <a href="https://tools.google.com/dlpage/gaoptout" rel="noopener" target="_blank">tools.google.com/dlpage/gaoptout</a>. O bloqueio não impede o uso do site.</p>

    <h2>3. Finalidade</h2>
    <p>Os dados do formulário são usados para responder à solicitação de demonstração e dar continuidade ao contato comercial. Ao enviar, nome, empresa, segmento e WhatsApp são transmitidos ao servidor do site e encaminhados por e-mail para a equipe comercial. O site não mantém banco de dados próprio; o registro fica na caixa de e-mail <a href="mailto:business@aylasystems.com">business@aylasystems.com</a>, pelo tempo necessário ao atendimento.</p>

    <h2>4. Compartilhamento</h2>
    <p>Não vendemos dados. O compartilhamento ocorre apenas com provedores necessários à operação do site e do atendimento, ou por obrigação legal.</p>

    <h2>5. Segurança</h2>
    <p>O site usa HTTPS, cabeçalhos de segurança e fontes locais. O acesso aos dados recebidos é restrito às pessoas envolvidas no atendimento.</p>

    <h2>6. Retenção</h2>
    <p>Mensagens e dados de contato são mantidos pelo tempo necessário ao atendimento e aos prazos legais. Depois disso, são eliminados ou anonimizados.</p>

    <h2>7. Direitos</h2>
    <p>Você pode solicitar acesso, correção, eliminação, portabilidade, informação sobre compartilhamento e revogação de consentimento. Escreva para <a href="mailto:business@aylasystems.com">business@aylasystems.com</a>.</p>

    <h2>8. Contato</h2>
    <p>Encarregado de dados: <a href="mailto:business@aylasystems.com">business@aylasystems.com</a>. Para detalhes sobre o tratamento na operação, consulte a <a href="/lgpd">página de LGPD</a>.</p>

    <h2>9. Alterações</h2>
    <p>Esta política pode ser atualizada. A data no topo indica a versão vigente.</p>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# 404
# ---------------------------------------------------------------------------

NOT_FOUND = """
<section class="page-hero page-hero-404">
  <div class="container">
    <span class="kicker reveal">Erro 404</span>
    <h1 class="reveal">Essa página não existe.</h1>
    <p class="lead reveal">O link pode ter mudado. Volte para o início ou fale com a gente.</p>
    <div class="actions reveal">
      <a class="btn btn-primary btn-large" href="/">Voltar ao início</a>
      <a class="btn btn-ghost btn-large" href="mailto:business@aylasystems.com">Falar por e-mail</a>
    </div>
  </div>
</section>
"""


PAGES = [
    {
        "slug": "index",
        "path": "/",
        "title": "Ayla Systems",
        "desc": "A Ayla atende, qualifica e agenda no WhatsApp da sua empresa em segundos, 24 horas por dia. Sem trocar o número e sem menu numérico.",
        "body": HOME,
        "active": "",
    },
    {
        "slug": "custo-da-demora",
        "path": "/custo-da-demora",
        "title": "Ayla Systems - Custo da demora",
        "desc": "Calcule quanto a demora no atendimento custa por mês e veja onde o dinheiro vaza no WhatsApp da sua empresa.",
        "body": CUSTO,
        "active": "custo-da-demora",
    },
    {
        "slug": "mecanica",
        "path": "/mecanica",
        "title": "Ayla Systems - Como funciona",
        "desc": "Do diagnóstico ao atendimento no ar em até 72 horas, sem trocar o número de WhatsApp da sua empresa.",
        "body": MECANICA,
        "active": "mecanica",
    },
    {
        "slug": "demonstracao",
        "path": "/demonstracao",
        "title": "Ayla Systems - Demonstração",
        "desc": "Converse com a Ayla no seu WhatsApp antes de contratar. Demonstração gratuita, sem reunião e sem instalação.",
        "body": DEMO,
        "active": "demonstracao",
    },
    {
        "slug": "segmentos",
        "path": "/segmentos",
        "title": "Ayla Systems - Segmentos",
        "desc": "Atendimento 24/7 para clínicas, advocacia, imobiliárias e serviços de alto ticket.",
        "body": SEGMENTOS,
        "active": "segmentos",
    },
    {
        "slug": "seguranca",
        "path": "/seguranca",
        "title": "Ayla Systems - Segurança",
        "desc": "API oficial do WhatsApp, criptografia em trânsito, dados mínimos e transbordo humano.",
        "body": SEGURANCA,
        "active": "",
    },
    {
        "slug": "lgpd",
        "path": "/lgpd",
        "title": "Ayla Systems - LGPD",
        "desc": "Como a Ayla Systems trata dados pessoais e como o titular pode exercer seus direitos.",
        "body": LGPD,
        "active": "",
    },
    {
        "slug": "termos",
        "path": "/termos",
        "title": "Ayla Systems - Termos de uso",
        "desc": "Regras para uso do site e da demonstração da Ayla Systems.",
        "body": TERMOS,
        "active": "",
    },
    {
        "slug": "privacidade",
        "path": "/privacidade",
        "title": "Ayla Systems - Privacidade",
        "desc": "Política de privacidade do site da Ayla Systems.",
        "body": PRIVACIDADE,
        "active": "",
    },
    {
        "slug": "404",
        "path": "/404",
        "title": "Ayla Systems - Página não encontrada",
        "desc": "A página que você procura não existe.",
        "body": NOT_FOUND,
        "active": "",
    },
]


def build() -> None:
    cssv = asset_version("styles.css")
    jsv = asset_version("script.js")
    anv = asset_version("analytics.js")
    for page in PAGES:
        html = BASE
        html = html.replace("[[TITLE]]", page["title"])
        html = html.replace("[[DESC]]", page["desc"])
        html = html.replace("[[PATH]]", page["path"])
        html = html.replace("[[HEADER]]", header(page["active"]))
        html = html.replace("[[BODY]]", page["body"].strip())
        html = html.replace("[[FOOTER]]", FOOTER)
        html = html.replace("[[CSSV]]", cssv)
        html = html.replace("[[JSV]]", jsv)
        html = html.replace("[[ANV]]", anv)
        filename = "index.html" if page["slug"] == "index" else f"{page['slug']}.html"
        (ROOT / filename).write_text(html, encoding="utf-8")
        print(f"gerado: {filename}")

    sitemap_urls = "\n".join(
        f"  <url><loc>{SITE}{p['path']}</loc><lastmod>2026-11-21</lastmod></url>"
        for p in PAGES
        if p["slug"] != "404"
    )
    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{sitemap_urls}
</urlset>
"""
    (ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8")

    robots = f"""User-agent: *
Allow: /

Sitemap: {SITE}/sitemap.xml
"""
    (ROOT / "robots.txt").write_text(robots, encoding="utf-8")
    print("gerado: sitemap.xml, robots.txt")


if __name__ == "__main__":
    build()
