const header = document.querySelector('[data-header]');
const menuToggle = document.querySelector('[data-menu-toggle]');
const siteNav = document.querySelector('[data-site-nav]');
const quoteForm = document.querySelector('[data-quote-form]');
const emailQuoteButton = document.querySelector('[data-email-quote]');
const formOutput = document.querySelector('[data-form-output]');
const serviceSelect = document.querySelector('[data-service-select]');
const yearEl = document.querySelector('[data-year]');
const businessPhone = '+17068976177';
const businessPhoneDisplay = '706-897-6177';
const businessEmail = 'bopeepsdetail@gmail.com';

if (yearEl) yearEl.textContent = new Date().getFullYear();

function setHeaderState() {
  if (!header) return;
  header.classList.toggle('is-scrolled', window.scrollY > 12);
}
setHeaderState();
window.addEventListener('scroll', setHeaderState, { passive: true });

if (menuToggle && siteNav) {
  menuToggle.addEventListener('click', () => {
    const isOpen = siteNav.classList.toggle('is-open');
    menuToggle.setAttribute('aria-expanded', String(isOpen));
    header?.classList.toggle('nav-open', isOpen);
  });

  siteNav.addEventListener('click', (event) => {
    if (event.target.matches('a')) {
      siteNav.classList.remove('is-open');
      menuToggle.setAttribute('aria-expanded', 'false');
      header?.classList.remove('nav-open');
    }
  });
}

const observer = 'IntersectionObserver' in window
  ? new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 })
  : null;

document.querySelectorAll('.reveal').forEach((el) => {
  if (observer) observer.observe(el);
  else el.classList.add('is-visible');
});

document.querySelectorAll('[data-service-request]').forEach((link) => {
  link.addEventListener('click', () => {
    if (!serviceSelect) return;
    const requestedService = link.getAttribute('data-service-request');
    const option = [...serviceSelect.options].find((item) => item.textContent.trim() === requestedService);
    if (option) serviceSelect.value = option.textContent.trim();
    else serviceSelect.value = 'Not sure yet';
  });
});

function getQuoteLines(data) {
  return [
    'Hi BoPeePs, I would like a detailing quote.',
    `Name: ${data.get('name') || ''}`,
    `My phone: ${data.get('customerPhone') || ''}`,
    `Vehicle: ${data.get('vehicle') || ''}`,
    `Service: ${data.get('service') || ''}`,
    `Notes: ${data.get('notes') || 'No extra notes yet.'}`
  ];
}

function validateQuoteForm() {
  if (!quoteForm) return false;
  if (!quoteForm.checkValidity()) {
    quoteForm.reportValidity();
    return false;
  }
  return true;
}

if (quoteForm) {
  quoteForm.addEventListener('submit', (event) => {
    event.preventDefault();

    if (!validateQuoteForm()) return;

    const data = new FormData(quoteForm);
    const body = encodeURIComponent(getQuoteLines(data).join('\n'));
    const smsLink = `sms:${businessPhone}?body=${body}`;

    if (formOutput) {
      formOutput.textContent = `Opening your text app. If it does not open, call ${businessPhoneDisplay} or email ${businessEmail}.`;
    }

    window.location.href = smsLink;
  });
}

if (emailQuoteButton && quoteForm) {
  emailQuoteButton.addEventListener('click', () => {
    if (!validateQuoteForm()) return;

    const data = new FormData(quoteForm);
    const subject = encodeURIComponent('Detailing Quote Request');
    const body = encodeURIComponent(getQuoteLines(data).join('\n'));
    const emailLink = `mailto:${businessEmail}?subject=${subject}&body=${body}`;

    if (formOutput) {
      formOutput.textContent = `Opening your email app. If it does not open, email ${businessEmail} or call ${businessPhoneDisplay}.`;
    }

    window.location.href = emailLink;
  });
}
