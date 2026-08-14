(() => {
  const menuButton = document.querySelector('[data-menu-toggle]');
  const nav = document.querySelector('[data-site-nav]');

  if (menuButton && nav) {
    const menuLabel = menuButton.querySelector('.sr-only');
    const setMenuState = open => {
      menuButton.setAttribute('aria-expanded', String(open));
      nav.classList.toggle('is-open', open);
      if (menuLabel) menuLabel.textContent = open ? 'Close menu' : 'Open menu';
    };

    const closeMenu = () => setMenuState(false);

    menuButton.addEventListener('click', () => {
      const open = menuButton.getAttribute('aria-expanded') === 'true';
      setMenuState(!open);
    });

    nav.addEventListener('click', event => {
      if (event.target.closest('a')) closeMenu();
    });

    document.addEventListener('keydown', event => {
      if (event.key === 'Escape') closeMenu();
    });
  }

  const widgetHost = document.querySelector('[data-booksy-widget-host]');
  let booksyLoadPromise = null;

  const findBooksyTrigger = () => widgetHost?.querySelector('.booksy-widget-button, button, a');

  const loadBooksyWidget = () => {
    if (!widgetHost) return Promise.resolve(false);
    if (findBooksyTrigger()) return Promise.resolve(true);
    if (booksyLoadPromise) return booksyLoadPromise;

    const src = widgetHost.dataset.booksyWidgetSrc;
    if (!src) return Promise.resolve(false);

    booksyLoadPromise = new Promise(resolve => {
      const script = document.createElement('script');
      script.src = src;
      script.async = true;
      script.addEventListener('load', () => {
        window.setTimeout(() => resolve(Boolean(findBooksyTrigger())), 0);
      }, { once: true });
      script.addEventListener('error', () => resolve(false), { once: true });
      widgetHost.appendChild(script);
    });

    return booksyLoadPromise;
  };

  document.querySelectorAll('[data-booksy-open]').forEach(link => {
    const warmBooksy = () => { void loadBooksyWidget(); };
    link.addEventListener('pointerenter', warmBooksy, { once: true });
    link.addEventListener('focus', warmBooksy, { once: true });

    link.addEventListener('click', async event => {
      const existingTrigger = findBooksyTrigger();
      if (existingTrigger) {
        event.preventDefault();
        existingTrigger.click();
        return;
      }

      if (!widgetHost?.dataset.booksyWidgetSrc) return;

      event.preventDefault();
      const fallbackUrl = link.href;
      const loaded = await loadBooksyWidget();
      const trigger = findBooksyTrigger();

      if (loaded && trigger) {
        trigger.click();
        return;
      }

      window.location.href = fallbackUrl;
    });
  });

  const stage = document.querySelector('[data-scrub-stage]');
  const image = document.querySelector('[data-scrub-image]');
  const canvas = document.querySelector('[data-scrub-canvas]');
  const status = document.querySelector('[data-scrub-status]');
  const resetButton = document.querySelector('[data-scrub-reset]');
  const revealButton = document.querySelector('[data-scrub-reveal]');
  const choices = [...document.querySelectorAll('[data-scrub-choice]')];

  if (!stage || !image || !canvas) return;
  const ctx = canvas.getContext('2d');
  if (!ctx) return;

  let drawing = false;
  let completed = false;
  let lastPoint = null;
  const cols = 28;
  const rows = 18;
  const visited = new Set();

  const paintGrime = (width, height) => {
    ctx.globalCompositeOperation = 'source-over';
    const gradient = ctx.createLinearGradient(0, 0, width, height);
    gradient.addColorStop(0, 'rgba(82,73,62,.78)');
    gradient.addColorStop(.5, 'rgba(56,52,48,.72)');
    gradient.addColorStop(1, 'rgba(112,101,81,.72)');
    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, width, height);

    const seedDots = Math.round((width * height) / 2200);
    for (let i = 0; i < seedDots; i++) {
      const x = ((Math.sin(i * 12.9898) * 43758.5453 % 1) + 1) % 1 * width;
      const y = ((Math.sin(i * 78.233) * 24634.6345 % 1) + 1) % 1 * height;
      const radius = 2 + ((i * 17) % 12);
      ctx.fillStyle = i % 4 === 0 ? 'rgba(205,194,164,.18)' : 'rgba(25,23,21,.16)';
      ctx.beginPath();
      ctx.arc(x, y, radius, 0, Math.PI * 2);
      ctx.fill();
    }
  };

  const resetGrime = () => {
    const rect = stage.getBoundingClientRect();
    if (!rect.width || !rect.height) return;
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    canvas.width = Math.max(1, Math.round(rect.width * dpr));
    canvas.height = Math.max(1, Math.round(rect.height * dpr));
    canvas.style.width = `${rect.width}px`;
    canvas.style.height = `${rect.height}px`;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    paintGrime(rect.width, rect.height);
    visited.clear();
    completed = false;
    stage.classList.remove('is-complete', 'is-started');
    if (status) status.textContent = '0% revealed';
  };

  const revealAll = () => {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    completed = true;
    stage.classList.add('is-started', 'is-complete');
    if (status) status.textContent = '100% revealed';
  };

  choices.forEach(choice => {
    choice.addEventListener('click', () => {
      choices.forEach(item => item.setAttribute('aria-pressed', String(item === choice)));
      image.src = choice.getAttribute('data-scrub-src');
      image.alt = choice.getAttribute('data-scrub-alt');
      resetGrime();
    });
  });

  resetButton?.addEventListener('click', resetGrime);
  revealButton?.addEventListener('click', revealAll);

  const pointFromEvent = event => {
    const rect = canvas.getBoundingClientRect();
    return { x: event.clientX - rect.left, y: event.clientY - rect.top, rect };
  };

  const markGrid = (x, y, width, height) => {
    const col = Math.max(0, Math.min(cols - 1, Math.floor((x / width) * cols)));
    const row = Math.max(0, Math.min(rows - 1, Math.floor((y / height) * rows)));
    const radius = 2;
    for (let yy = row - radius; yy <= row + radius; yy++) {
      for (let xx = col - radius; xx <= col + radius; xx++) {
        if (xx >= 0 && xx < cols && yy >= 0 && yy < rows) visited.add(`${xx}:${yy}`);
      }
    }
  };

  const updateProgress = () => {
    const percent = Math.min(100, Math.round((visited.size / (cols * rows)) * 100));
    if (status) status.textContent = `${percent}% revealed`;
    if (!completed && percent >= 48) {
      completed = true;
      stage.classList.add('is-complete');
      if (status) status.textContent = 'Nice work - ready to book?';
    }
  };

  const eraseAt = (point, previous = null) => {
    const brush = Math.max(42, Math.min(82, point.rect.width * .13));
    ctx.save();
    ctx.globalCompositeOperation = 'destination-out';
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';
    ctx.lineWidth = brush;
    ctx.strokeStyle = 'rgba(0,0,0,1)';
    ctx.beginPath();
    if (previous) ctx.moveTo(previous.x, previous.y);
    else ctx.moveTo(point.x, point.y);
    ctx.lineTo(point.x, point.y);
    ctx.stroke();
    ctx.restore();
    markGrid(point.x, point.y, point.rect.width, point.rect.height);
    updateProgress();
  };

  canvas.addEventListener('pointerdown', event => {
    drawing = true;
    stage.classList.add('is-started');
    canvas.setPointerCapture(event.pointerId);
    lastPoint = pointFromEvent(event);
    eraseAt(lastPoint);
  });

  canvas.addEventListener('pointermove', event => {
    if (!drawing) return;
    const point = pointFromEvent(event);
    eraseAt(point, lastPoint);
    lastPoint = point;
  });

  const endDrawing = event => {
    if (!drawing) return;
    drawing = false;
    lastPoint = null;
    if (canvas.hasPointerCapture(event.pointerId)) canvas.releasePointerCapture(event.pointerId);
  };

  canvas.addEventListener('pointerup', endDrawing);
  canvas.addEventListener('pointercancel', endDrawing);
  canvas.addEventListener('pointerleave', event => {
    if (event.pointerType === 'mouse') drawing = false;
  });

  if ('ResizeObserver' in window) {
    const resizeObserver = new ResizeObserver(resetGrime);
    resizeObserver.observe(stage);
  } else {
    window.addEventListener('resize', resetGrime);
    resetGrime();
  }
})();
