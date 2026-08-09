import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';


class FakeClassList {
  constructor() { this.values = new Set(); }
  add(...names) { names.forEach(name => this.values.add(name)); }
  remove(...names) { names.forEach(name => this.values.delete(name)); }
  contains(name) { return this.values.has(name); }
  toggle(name, force) {
    const next = force === undefined ? !this.values.has(name) : force;
    if (next) this.values.add(name); else this.values.delete(name);
    return next;
  }
}


class FakeElement {
  constructor(attrs = {}) {
    this.attrs = new Map(Object.entries(attrs));
    this.listeners = new Map();
    this.classList = new FakeClassList();
    this.style = {};
    this.textContent = '';
    this.src = attrs.src || '';
    this.alt = attrs.alt || '';
  }

  addEventListener(type, handler) {
    if (!this.listeners.has(type)) this.listeners.set(type, []);
    this.listeners.get(type).push(handler);
  }

  dispatch(type, extra = {}) {
    const event = {
      clientX: 0,
      clientY: 0,
      pointerId: 1,
      pointerType: 'mouse',
      defaultPrevented: false,
      preventDefault() { this.defaultPrevented = true; },
      ...extra,
    };
    for (const handler of this.listeners.get(type) || []) handler(event);
    return event;
  }

  getAttribute(name) { return this.attrs.has(name) ? this.attrs.get(name) : null; }
  setAttribute(name, value) { this.attrs.set(name, String(value)); }
  hasPointerCapture() { return false; }
  setPointerCapture() {}
  releasePointerCapture() {}
  getBoundingClientRect() { return { left: 0, top: 0, width: 800, height: 500 }; }
  closest() { return null; }
}


function buildHarness({ withWidget = true } = {}) {
  const contextCalls = { clearRect: 0, fillRect: 0, widgetClicks: 0 };
  const ctx = {
    beginPath() {}, arc() {}, fill() {}, lineTo() {}, moveTo() {}, restore() {}, save() {}, setTransform() {}, stroke() {},
    createLinearGradient() { return { addColorStop() {} }; },
    clearRect() { contextCalls.clearRect += 1; },
    fillRect() { contextCalls.fillRect += 1; },
  };

  const stage = new FakeElement();
  const canvas = new FakeElement();
  canvas.getContext = () => ctx;
  const image = new FakeElement({ src: 'assets-v3/scrub-photo-6.webp', alt: 'RV detailing example' });
  const status = new FakeElement();
  const reset = new FakeElement();
  const reveal = new FakeElement();
  const tip = new FakeElement();
  const choices = [
    new FakeElement({ 'data-scrub-choice': 'rv', 'data-scrub-src': 'assets-v3/scrub-photo-6.webp', 'data-scrub-alt': 'RV detailing example' }),
    new FakeElement({ 'data-scrub-choice': 'white-truck', 'data-scrub-src': 'assets-v3/scrub-photo-10.webp', 'data-scrub-alt': 'White truck detailing example' }),
  ];
  const bookingLink = new FakeElement();
  const widgetButton = new FakeElement();
  widgetButton.click = () => { contextCalls.widgetClicks += 1; };
  const widgetHost = new FakeElement();
  widgetHost.querySelector = () => withWidget ? widgetButton : null;

  const selectorMap = new Map([
    ['[data-menu-toggle]', null],
    ['[data-site-nav]', null],
    ['[data-scrub-stage]', stage],
    ['[data-scrub-canvas]', canvas],
    ['[data-scrub-image]', image],
    ['[data-scrub-status]', status],
    ['[data-scrub-reset]', reset],
    ['[data-scrub-reveal]', reveal],
    ['[data-scrub-tip]', tip],
    ['[data-booksy-widget-host]', widgetHost],
  ]);
  const document = {
    querySelector: selector => selectorMap.get(selector) ?? null,
    querySelectorAll: selector => {
      if (selector === '[data-scrub-choice]') return choices;
      if (selector === '[data-booksy-open]') return [bookingLink];
      return [];
    },
    addEventListener() {},
  };
  const window = { devicePixelRatio: 1, addEventListener() {} };
  const context = {
    document,
    window,
    console,
    MutationObserver: class { constructor(callback) { this.callback = callback; } observe() {} disconnect() {} },
    ResizeObserver: class { constructor(callback) { this.callback = callback; } observe() { this.callback(); } },
  };
  vm.createContext(context);
  vm.runInContext(fs.readFileSync(new URL('../script-v3.js', import.meta.url), 'utf8'), context);
  return { bookingLink, choices, contextCalls, image, reset, reveal, stage, status };
}


{
  const harness = buildHarness();
  harness.choices[1].dispatch('click');
  assert.equal(harness.image.src, 'assets-v3/scrub-photo-10.webp');
  assert.equal(harness.image.alt, 'White truck detailing example');
  assert.equal(harness.choices[1].getAttribute('aria-pressed'), 'true');
  assert.equal(harness.status.textContent, '0% revealed');

  harness.reveal.dispatch('click');
  assert.equal(harness.status.textContent, '100% revealed');
  assert.equal(harness.stage.classList.contains('is-complete'), true);
  assert.ok(harness.contextCalls.clearRect > 0);

  harness.reset.dispatch('click');
  assert.equal(harness.status.textContent, '0% revealed');
  assert.equal(harness.stage.classList.contains('is-complete'), false);
}

{
  const harness = buildHarness({ withWidget: true });
  const event = harness.bookingLink.dispatch('click');
  assert.equal(event.defaultPrevented, true);
  assert.equal(harness.contextCalls.widgetClicks, 1);
}

{
  const harness = buildHarness({ withWidget: false });
  const event = harness.bookingLink.dispatch('click');
  assert.equal(event.defaultPrevented, false);
  assert.equal(harness.contextCalls.widgetClicks, 0);
}

console.log('script behavior contract passed');
