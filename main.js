/* ---------- Jazyk / Language ---------- */
const LANG_KEY = 'pubpodzemi-lang';

function getStoredLang() {
  try { return localStorage.getItem(LANG_KEY); } catch (e) { return null; }
}
function storeLang(lang) {
  try { localStorage.setItem(LANG_KEY, lang); } catch (e) { /* bez úložiště */ }
}

// Každý prvek s data-en má anglický text; český originál si uložíme do data-cs.
// Atributy: data-en-alt, data-en-aria-label, data-en-content, data-en-title.
const ATTRS = ['alt', 'aria-label', 'content', 'title', 'placeholder'];

function applyLang(lang) {
  document.documentElement.lang = lang;
  document.querySelectorAll('[data-en]').forEach(el => {
    if (el.dataset.cs === undefined) el.dataset.cs = el.innerHTML;
    el.innerHTML = lang === 'en' ? el.dataset.en : el.dataset.cs;
  });
  ATTRS.forEach(attr => {
    const enKey = 'data-en-' + attr, csKey = 'data-cs-' + attr;
    document.querySelectorAll('[' + enKey + ']').forEach(el => {
      if (!el.hasAttribute(csKey)) el.setAttribute(csKey, el.getAttribute(attr) || '');
      el.setAttribute(attr, lang === 'en' ? el.getAttribute(enKey) : el.getAttribute(csKey));
    });
  });
  document.querySelectorAll('.lang__btn').forEach(b => {
    const active = b.dataset.lang === lang;
    b.classList.toggle('is-active', active);
    b.setAttribute('aria-pressed', active);
  });
}

let currentLang = getStoredLang() === 'en' ? 'en' : 'cs';

/* ---------- Rezervační okno ---------- */
const PHONE = '+420602211362';
const PHONE_LABEL = '+420 602 211 362';

const dialog = document.createElement('dialog');
dialog.className = 'modal';
dialog.innerHTML = `
  <button class="modal__close" type="button" aria-label="Zavřít" data-en-aria-label="Close">×</button>
  <div class="modal__step" data-step="choose">
    <p class="eyebrow" data-en="Book a table">Rezervace</p>
    <h2 class="modal__title" data-en="How would you like to book?">Jak si chcete rezervovat?</h2>
    <div class="modal__options">
      <a class="option" href="tel:${PHONE}">
        <span class="option__icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg></span>
        <span class="option__text">
          <span class="option__title" data-en="Call us">Zavolat</span>
          <span class="option__desc">${PHONE_LABEL}</span>
        </span>
      </a>
      <button class="option" type="button" data-action="online">
        <span class="option__icon" aria-hidden="true"><svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M16 3v4M8 3v4M3 10h18"/></svg></span>
        <span class="option__text">
          <span class="option__title" data-en="Book online">Online rezervace</span>
          <span class="option__desc" data-en="Reservation system">Rezervační systém</span>
        </span>
      </button>
    </div>
  </div>
  <div class="modal__step" data-step="sorry" hidden>
    <p class="eyebrow" data-en="Online booking">Online rezervace</p>
    <h2 class="modal__title" data-en="We're sorry">Omlouváme se</h2>
    <p class="modal__text" data-en="Our online reservation system isn't up and running yet. Please book your table by phone – we'll be happy to help.">Online rezervační systém zatím nemáme spuštěný. Rezervujte si prosím stůl telefonicky, rádi vám pomůžeme.</p>
    <div class="modal__actions">
      <a class="btn" href="tel:${PHONE}" data-en="Call ${PHONE_LABEL}">Zavolat ${PHONE_LABEL}</a>
      <button class="btn btn--ghost" type="button" data-action="back" data-en="Back">Zpět</button>
    </div>
  </div>`;
document.body.appendChild(dialog);

function showStep(name) {
  dialog.querySelectorAll('.modal__step').forEach(s => { s.hidden = s.dataset.step !== name; });
}
function openReservation() {
  showStep('choose');
  if (typeof dialog.showModal === 'function') dialog.showModal();
  else dialog.setAttribute('open', '');
}
function closeReservation() {
  if (typeof dialog.close === 'function') dialog.close();
  else dialog.removeAttribute('open');
}

dialog.addEventListener('click', e => {
  if (e.target === dialog) return closeReservation();            // klik mimo okno
  if (e.target.closest('.modal__close')) return closeReservation();
  const action = e.target.closest('[data-action]');
  if (action && action.dataset.action === 'online') showStep('sorry');
  if (action && action.dataset.action === 'back') showStep('choose');
});

document.querySelectorAll('.js-reserve').forEach(btn => btn.addEventListener('click', e => {
  e.preventDefault();
  closeMenu();
  openReservation();
}));

/* ---------- Mobilní menu ---------- */
const toggle = document.querySelector('.nav__toggle');
const links = document.querySelector('.nav__links');
function closeMenu() {
  if (!links) return;
  links.classList.remove('open');
  if (toggle) toggle.setAttribute('aria-expanded', 'false');
}
if (toggle && links) {
  toggle.addEventListener('click', () => {
    const open = links.classList.toggle('open');
    toggle.setAttribute('aria-expanded', open);
  });
}

/* ---------- Přepínač jazyka ---------- */
document.querySelectorAll('.lang__btn').forEach(b => b.addEventListener('click', () => {
  currentLang = b.dataset.lang;
  storeLang(currentLang);
  applyLang(currentLang);
}));
applyLang(currentLang);

/* ---------- Posouvání: web se vždy otevře nahoře ---------- */
// Prohlížeč si jinak pamatuje, kde jste naposledy byli, a po otevření sjede dolů.
if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
const SCROLL_KEY = 'pubpodzemi-scroll-to';

function scrollToId(id, smooth) {
  const target = document.getElementById(id);
  if (target) target.scrollIntoView({ behavior: smooth ? 'smooth' : 'instant' });
}

// Odkazy na sekce: posuneme se, ale do adresy nepřidáváme #kotvu,
// takže znovu otevřený web začne vždy na úvodu.
document.addEventListener('click', e => {
  const a = e.target.closest('a[href*="#"]');
  if (!a || a.target === '_blank') return;
  const url = new URL(a.href, location.href);
  const id = url.hash.slice(1);
  if (!id) return;
  e.preventDefault();
  closeMenu();
  const samePage = p => p.replace(/index\.html$/, '');
  if (samePage(url.pathname) === samePage(location.pathname)) {
    scrollToId(id, true);
  } else {
    try { sessionStorage.setItem(SCROLL_KEY, id); } catch (err) { /* nic */ }
    location.href = url.pathname + url.search;
  }
});

let pendingId = null;
try { pendingId = sessionStorage.getItem(SCROLL_KEY); sessionStorage.removeItem(SCROLL_KEY); } catch (e) { /* nic */ }
if (location.hash) history.replaceState(null, '', location.pathname + location.search);

function initialScroll() {
  if (pendingId) scrollToId(pendingId, false);
  else window.scrollTo({ top: 0, behavior: 'instant' });
}
initialScroll();
// Po načtení obrázků a mapy ještě jednou, aby nic stránku neposunulo –
// ale jen pokud host mezitím sám nezačal posouvat.
let userScrolled = false;
['wheel', 'touchstart', 'keydown', 'mousedown'].forEach(ev =>
  window.addEventListener(ev, () => { userScrolled = true; }, { once: true, passive: true }));
window.addEventListener('load', () => { if (!userScrolled) initialScroll(); });

/* ---------- Rok v patičce ---------- */
document.querySelectorAll('.year').forEach(el => { el.textContent = new Date().getFullYear(); });

/* ---------- Menu přes úvodní fotku: průhledné nahoře, plné po odrolování ---------- */
const navEl = document.querySelector('.nav--overlay');
if (navEl) {
  const updateNav = () => {
    const menuOpen = links && links.classList.contains('open');
    navEl.classList.toggle('is-solid', window.scrollY > 40 || menuOpen);
  };
  window.addEventListener('scroll', updateNav, { passive: true });
  if (toggle) toggle.addEventListener('click', updateNav);
  if (links) links.addEventListener('click', () => setTimeout(updateNav, 0));
  updateNav();
}

/* ---------- Otevřeno / zavřeno: malé okénko v rohu podle českého času ---------- */
// Otevírací doba: každý den 15:00 – 01:00.
const OPEN_HOUR = 15, CLOSE_HOUR = 1;
const TOAST_KEY = 'pubpodzemi-status-closed';

function pragueHour() {
  const parts = new Intl.DateTimeFormat('en-GB', { timeZone: 'Europe/Prague', hour: '2-digit', hour12: false })
    .formatToParts(new Date());
  return Number(parts.find(p => p.type === 'hour').value) % 24;
}

const toast = document.createElement('div');
toast.className = 'status-toast';
toast.setAttribute('role', 'status');
toast.innerHTML = `
  <span class="status-toast__dot"></span>
  <span class="status-toast__text"></span>
  <button type="button" class="status-toast__close" aria-label="Zavřít" data-en-aria-label="Close">×</button>`;
document.body.appendChild(toast);
const toastText = toast.querySelector('.status-toast__text');

function renderOpenStatus() {
  const h = pragueHour();
  const open = h >= OPEN_HOUR || h < CLOSE_HOUR;
  const msg = {
    cs: open ? 'Právě otevřeno, do 01:00' : 'Právě zavřeno, otevíráme v 15:00',
    en: open ? 'Open now, until 1 am' : 'Closed now, opens at 3 pm'
  };
  toast.classList.toggle('is-closed', !open);
  // Obě jazykové verze, aby je přepínač jazyka správně vystřídal.
  toastText.dataset.cs = msg.cs;
  toastText.dataset.en = msg.en;
  toastText.textContent = msg[currentLang];
}
renderOpenStatus();
applyLang(currentLang);
setInterval(renderOpenStatus, 60 * 1000);

let toastDismissed = false;
try { toastDismissed = sessionStorage.getItem(TOAST_KEY) === '1'; } catch (e) { /* nic */ }
if (!toastDismissed) setTimeout(() => toast.classList.add('is-visible'), 1200);
toast.querySelector('.status-toast__close').addEventListener('click', () => {
  toast.classList.remove('is-visible');
  try { sessionStorage.setItem(TOAST_KEY, '1'); } catch (e) { /* nic */ }
});
