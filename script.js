document.addEventListener('DOMContentLoaded', () => {
  initStickyHeader();
  initFaqAccordion();
  initDialogueSimulator();
  initLeadForms();
  initModal();
});
// Header hairline transition on scroll
function initStickyHeader() {
  const header = document.querySelector('.site-header');
  if (!header) return;
  window.addEventListener('scroll', () => {
    if (window.scrollY > 20) {
      header.style.borderColor = 'rgba(255, 255, 255, 0.16)';
      header.style.backgroundColor = 'rgba(9, 10, 12, 0.95)';
    } else {
      header.style.borderColor = 'var(--hairline)';
      header.style.backgroundColor = 'rgba(9, 10, 12, 0.85)';
    }
  }, { passive: true });
}
// FAQ Accordion
function initFaqAccordion() {
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach((item) => {
    const questionBtn = item.querySelector('.faq-question');
    if (!questionBtn) return;
    questionBtn.addEventListener('click', () => {
      const isActive = item.classList.contains('active');
      // Close all other items for a clean single-open behavior
      faqItems.forEach((other) => {
        if (other !== item) {
          other.classList.remove('active');
          const btn = other.querySelector('.faq-question');
          if (btn) btn.setAttribute('aria-expanded', 'false');
        }
      });
      if (isActive) {
        item.classList.remove('active');
        questionBtn.setAttribute('aria-expanded', 'false');
      } else {
        item.classList.add('active');
        questionBtn.setAttribute('aria-expanded', 'true');
      }
    });
  });
}
// Interactive Dialogue Simulator for Section 4
function initDialogueSimulator() {
  const restartBtn = document.getElementById('restartSimulatorBtn');
  const chatStream = document.getElementById('chatStream');
  if (!restartBtn || !chatStream) return;
  const scriptSteps = [
    {
      author: 'Paciente',
      type: 'patient',
      time: '22:47:12',
      meta: 'Via Anúncio Instagram',
      text: 'Olá, vi o anúncio de vocês. Estou com uma dor forte no dente de trás e preciso saber se vocês atendem amanhã cedo.',
      delay: 500
    },
    {
      author: 'Ayla Systems',
      type: 'ayla',
      time: '22:47:19',
      meta: 'WhatsApp Oficial API',
      latency: '7s latência',
      text: 'Olá. Atendemos sim. Para casos com dor aguda, priorizamos os primeiros horários da manhã na unidade central. Você já é paciente da clínica ou será sua primeira consulta?',
      delay: 1500
    },
    {
      author: 'Paciente',
      type: 'patient',
      time: '22:47:45',
      meta: 'Resposta Direta',
      text: 'Primeira vez. Moro aqui perto.',
      delay: 1200
    },
    {
      author: 'Ayla Systems',
      type: 'ayla',
      time: '22:47:52',
      meta: 'WhatsApp Oficial API',
      latency: '7s latência',
      text: 'Perfeito. Temos dois horários emergenciais disponíveis para amanhã, segunda-feira: às 08h30 ou às 09h15, com o Dr. Marcos. Qual dessas opções fica melhor para você?',
      delay: 1500
    },
    {
      author: 'Paciente',
      type: 'patient',
      time: '22:48:10',
      meta: 'Opção Selecionada',
      text: '08h30 fica ótimo.',
      delay: 1200
    },
    {
      author: 'Ayla Systems',
      type: 'ayla',
      time: '22:48:17',
      meta: 'WhatsApp Oficial API',
      latency: '7s latência',
      text: 'Horário pré-agendado para amanhã, às 08h30. Por favor, informe apenas seu nome completo e CPF para emitirmos sua ficha de recepção e bloquearmos o horário na agenda.',
      delay: 1500
    },
    {
      author: 'Paciente',
      type: 'patient',
      time: '22:48:38',
      meta: 'Dados Fornecidos',
      text: 'Carlos Eduardo Mendes, CPF 123.456.789-00.',
      delay: 1200
    },
    {
      author: 'Ayla Systems',
      type: 'ayla',
      time: '22:48:44',
      meta: 'WhatsApp Oficial API',
      latency: '6s latência',
      text: 'Confirmado, Carlos. Sua consulta está agendada para amanhã às 08h30 na Rua Augusta, 1200. Enviamos o comprovante e as instruções de estacionamento aqui abaixo. Tenha uma boa noite.',
      delay: 1500
    }
  ];
  let currentTimeout = null;
  function renderStep(index) {
    if (index >= scriptSteps.length) {
      restartBtn.disabled = false;
      restartBtn.innerText = 'Replay da Simulação';
      return;
    }
    const step = scriptSteps[index];
    const bubble = document.createElement('div');
    bubble.className = `chat-bubble ${step.type}`;
    const head = document.createElement('div');
    head.className = 'bubble-head';
    const authorSpan = document.createElement('span');
    authorSpan.className = 'author';
    authorSpan.textContent = step.author;
    const metaSpan = document.createElement('span');
    metaSpan.textContent = `${step.time} · ${step.meta}`;
    head.appendChild(authorSpan);
    if (step.latency) {
      const latSpan = document.createElement('span');
      latSpan.className = 'latency-tag';
      latSpan.textContent = step.latency;
      head.appendChild(latSpan);
    }
    head.appendChild(metaSpan);
    const body = document.createElement('div');
    body.textContent = step.text;
    bubble.appendChild(head);
    bubble.appendChild(body);
    chatStream.appendChild(bubble);
    // Smooth scroll inside chat container
    chatStream.scrollTop = chatStream.scrollHeight;
    currentTimeout = setTimeout(() => {
      renderStep(index + 1);
    }, step.delay);
  }
  function startReplay() {
    if (currentTimeout) clearTimeout(currentTimeout);
    chatStream.innerHTML = '';
    restartBtn.disabled = true;
    restartBtn.innerText = 'Executando Fluxo...';
    renderStep(0);
  }
  restartBtn.addEventListener('click', startReplay);
}
// Modal handling
function initModal() {
  const modal = document.getElementById('demoModal');
  const closeBtn = document.getElementById('modalCloseBtn');
  const triggerBtns = document.querySelectorAll('.trigger-modal');
  if (!modal || !closeBtn) return;
  function openModal() {
    modal.classList.add('open');
    document.body.style.overflow = 'hidden';
    const firstInput = modal.querySelector('input');
    if (firstInput) firstInput.focus();
  }
  function closeModal() {
    modal.classList.remove('open');
    document.body.style.overflow = '';
  }
  triggerBtns.forEach((btn) => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      openModal();
    });
  });
  closeBtn.addEventListener('click', closeModal);
  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      closeModal();
    }
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.classList.contains('open')) {
      closeModal();
    }
  });
}
// Lead capture & WhatsApp redirection
function initLeadForms() {
  const forms = [
    document.getElementById('sectionLeadForm'),
    document.getElementById('modalLeadForm')
  ];
  forms.forEach((form) => {
    if (!form) return;
    const phoneInput = form.querySelector('input[type="tel"]');
    if (phoneInput) {
      applyPhoneMask(phoneInput);
    }
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = form.querySelector('[name="name"]')?.value.trim() || '';
      const company = form.querySelector('[name="company"]')?.value.trim() || '';
      const segment = form.querySelector('[name="segment"]')?.value || 'Não informado';
      const phone = phoneInput ? phoneInput.value.trim() : '';
      if (!name || !phone) {
        alert('Por favor, preencha seu nome e número de WhatsApp.');
        return;
      }
      // Format WhatsApp payload
      const officialSupportNumber = '5511999999999'; // Número institucional de triagem Ayla
      const textMessage = `Olá! Gostaria de receber a demonstração interativa da Ayla Systems no meu WhatsApp.\n\n` +
        `*Nome:* ${name}\n` +
        `*Empresa:* ${company || 'Não informada'}\n` +
        `*Segmento:* ${segment}\n` +
        `*WhatsApp:* ${phone}`;
      const waUrl = `https://api.whatsapp.com/send?phone=${officialSupportNumber}&text=${encodeURIComponent(textMessage)}`;
      // Show immediate feedback
      const submitBtn = form.querySelector('button[type="submit"]');
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = 'Conectando ao WhatsApp...';
      }
      setTimeout(() => {
        window.open(waUrl, '_blank', 'noopener,noreferrer');
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerHTML = 'Demonstração Solicitada!';
          setTimeout(() => {
            submitBtn.innerHTML = 'Receber Demonstração no WhatsApp';
          }, 3500);
        }
      }, 400);
    });
  });
}
// Input mask for Brazilian Phone: (XX) 9XXXX-XXXX
function applyPhoneMask(input) {
  input.addEventListener('input', (e) => {
    let val = e.target.value.replace(/\D/g, '');
    if (val.length > 11) val = val.substring(0, 11);
    if (val.length > 10) {
      e.target.value = `(${val.substring(0, 2)}) ${val.substring(2, 7)}-${val.substring(7, 11)}`;
    } else if (val.length > 6) {
      e.target.value = `(${val.substring(0, 2)}) ${val.substring(2, 6)}-${val.substring(6, 10)}`;
    } else if (val.length > 2) {
      e.target.value = `(${val.substring(0, 2)}) ${val.substring(2)}`;
    } else if (val.length > 0) {
      e.target.value = `(${val}`;
    } else {
      e.target.value = '';
    }
  });
}