# Booksy Widget Description Expansion Experiment Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Determine whether Booksy service descriptions inside the website booking modal can be safely expanded from the BoPeeps host page without altering booking behavior.

**Architecture:** Create a standalone development-only diagnostic page on `dev/booksy-widget-description` that loads the same Booksy embed used by BoPeeps without modifying `index.html`. The diagnostic observes only host-page DOM structure after the Booksy widget opens, classifies the widget as same-document, brittle, or cross-origin-isolated, and never reads booking form/customer/payment data. Only a verified same-document stable description surface would qualify for a CSS-only expansion test.

**Tech Stack:** Static HTML5, vanilla JavaScript, existing Booksy embed, GitHub branch preview.

## Global Constraints

- Work only on `dev/booksy-widget-description`.
- Do not modify `main`, `index.html`, GitHub Pages settings, DNS, Booksy account settings, pricing, services, payments, or booking logic.
- Treat Booksy as third-party software; do not intercept network requests or replace Booksy markup.
- The diagnostic is reachable only through the standalone `booksy-widget-diagnostic.html` page.
- Collect only structural DOM metadata: iframe origins, Booksy container existence, candidate description-element CSS properties, and accessibility classification.
- Do not collect names, contact details, appointment selections, account information, or payment information.
- Stop if content is cross-origin/isolated or only brittle generated selectors are available.

---

### Task 1: Add diagnostic regression checks

**Files:**
- Create: `tests/test_booksy_widget_diagnostic.py`

**Interfaces:**
- Consumes: `booksy-widget-diagnostic.html` and `booksy-widget-diagnostic.js`.
- Produces: static assertions that the experiment is isolated from the production homepage and does not modify Booksy booking actions.

- [ ] **Step 1:** Add a failing test that expects `booksy-widget-diagnostic.html` and `booksy-widget-diagnostic.js` to exist while asserting `index.html` does not reference the diagnostic script.
- [ ] **Step 2:** Assert the diagnostic source does not call `fetch`, `XMLHttpRequest`, `localStorage`, `sessionStorage`, or read input values.
- [ ] **Step 3:** Assert the diagnostic page embeds the same Booksy business ID `1808686`, country `us`, and language `en` as production.
- [ ] **Step 4:** Run `pytest -q tests/test_booksy_widget_diagnostic.py` and confirm failure because the standalone diagnostic files do not exist yet.

### Task 2: Implement the standalone structural diagnostic

**Files:**
- Create: `booksy-widget-diagnostic.html`
- Create: `booksy-widget-diagnostic.js`

**Interfaces:**
- Consumes: Booksy-generated host-page elements after the real widget opens.
- Produces: a small fixed diagnostic panel and console object `window.__bopeepsBooksyDiagnostic` containing only structural results.

- [ ] **Step 1:** Create a minimal BoPeeps-branded diagnostic page that explains it is development-only and loads `booksy-widget-diagnostic.js` plus the same Booksy widget embed as production.
- [ ] **Step 2:** Observe the document for Booksy containers and iframes using `MutationObserver`.
- [ ] **Step 3:** For each iframe, record only its `src`, parsed origin, and whether `contentDocument` can be accessed without a security exception.
- [ ] **Step 4:** Search the host document—not inaccessible iframe contents—for Booksy-owned nodes and candidate description text; inspect `lineClamp`, `webkitLineClamp`, `maxHeight`, `overflow`, and `display` only.
- [ ] **Step 5:** Classify the result as `B1`, `B2`, or `B3` using the stop conditions in the design spec.
- [ ] **Step 6:** Render the classification and structural facts in a compact diagnostic panel; do not alter the widget.

### Task 3: Verify the diagnostic itself

**Files:**
- Verify: `index.html`
- Verify: `booksy-widget-diagnostic.html`
- Verify: `booksy-widget-diagnostic.js`
- Verify: `tests/test_booksy_widget_diagnostic.py`

**Interfaces:**
- Consumes: diagnostic implementation.
- Produces: evidence that the diagnostic is isolated and non-invasive.

- [ ] **Step 1:** Run `pytest -q tests/test_booksy_widget_diagnostic.py` and require zero failures.
- [ ] **Step 2:** Run `node --check booksy-widget-diagnostic.js` and require exit code 0.
- [ ] **Step 3:** Compare `main...dev/booksy-widget-description` and confirm `index.html` is unchanged and only the experiment spec/plan/test/diagnostic files were added.
- [ ] **Step 4:** Confirm the diagnostic source contains no booking-button replacements, network interception, storage reads, or form-value reads.

### Task 4: Determine the Booksy architecture result

**Files:**
- Read-only runtime inspection of the standalone branch diagnostic and public Booksy embed architecture.

**Interfaces:**
- Consumes: diagnostic architecture plus Booksy's real modal implementation evidence.
- Produces: final B1/B2/B3 recommendation.

- [ ] **Step 1:** Trigger the real Booksy modal from the standalone diagnostic when browser-network access is available and record only iframe/container facts.
- [ ] **Step 2:** Cross-check the runtime result against Booksy's documented embed behavior and current public implementation evidence.
- [ ] **Step 3:** If the service rows are directly accessible with stable semantic structure, test a temporary CSS-only clamp removal and re-check Book/close/navigation behavior.
- [ ] **Step 4:** If the modal uses a cross-origin iframe or unstable internals, do not add expansion CSS; classify B3/B2 and stop.
- [ ] **Step 5:** Report the result to the user with any runtime limitation stated explicitly; do not merge anything.
