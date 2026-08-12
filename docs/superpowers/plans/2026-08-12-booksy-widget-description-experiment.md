# Booksy Widget Description Expansion Experiment Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Determine whether Booksy service descriptions inside the website booking modal can be safely expanded from the BoPeeps host page without altering booking behavior.

**Architecture:** Add a query-gated development diagnostic to `dev/booksy-widget-description`. The diagnostic observes only host-page DOM structure after the Booksy widget opens, classifies the widget as same-document, brittle, or cross-origin-isolated, and never reads booking form/customer/payment data. Only a verified same-document stable description surface would qualify for a CSS-only expansion test.

**Tech Stack:** Static HTML5, vanilla JavaScript, existing Booksy embed, GitHub branch preview.

## Global Constraints

- Work only on `dev/booksy-widget-description`.
- Do not modify `main`, GitHub Pages settings, DNS, Booksy account settings, pricing, services, payments, or booking logic.
- Treat Booksy as third-party software; do not intercept network requests or replace Booksy markup.
- Diagnostics activate only when the URL contains `?booksydebug=1`.
- Collect only structural DOM metadata: iframe origins, Booksy container existence, candidate description-element CSS properties, and accessibility classification.
- Do not collect names, contact details, appointment selections, account information, or payment information.
- Stop if content is cross-origin/isolated or only brittle generated selectors are available.

---

### Task 1: Add diagnostic regression checks

**Files:**
- Create: `tests/test_booksy_widget_diagnostic.py`

**Interfaces:**
- Consumes: `index.html` and `booksy-widget-diagnostic.js`.
- Produces: static assertions that the diagnostic is development-query-gated, does not run by default, and does not modify Booksy booking actions.

- [ ] **Step 1:** Add a failing test that expects `index.html` to load `booksy-widget-diagnostic.js` only as a passive script and expects the diagnostic source to require `booksydebug=1`.
- [ ] **Step 2:** Assert the diagnostic does not call `fetch`, `XMLHttpRequest`, `localStorage`, `sessionStorage`, or inspect form input values.
- [ ] **Step 3:** Run `pytest -q tests/test_booksy_widget_diagnostic.py` and confirm failure because the diagnostic script does not exist yet.

### Task 2: Implement the query-gated structural diagnostic

**Files:**
- Create: `booksy-widget-diagnostic.js`
- Modify: `index.html`

**Interfaces:**
- Consumes: Booksy-generated host-page elements after the existing widget opens.
- Produces: a small fixed diagnostic panel and console object `window.__bopeepsBooksyDiagnostic` containing only structural results.

- [ ] **Step 1:** Add `<script defer src="booksy-widget-diagnostic.js"></script>` after the existing site script on the development branch.
- [ ] **Step 2:** In the diagnostic script, exit immediately unless `new URLSearchParams(location.search).get('booksydebug') === '1'`.
- [ ] **Step 3:** Observe the document for Booksy containers and iframes using `MutationObserver`.
- [ ] **Step 4:** For each iframe, record only its `src`, parsed origin, and whether `contentDocument` can be accessed without a security exception.
- [ ] **Step 5:** Search the host document—not iframe contents—for Booksy-owned nodes and candidate description text; inspect `lineClamp`, `webkitLineClamp`, `maxHeight`, `overflow`, and `display` only.
- [ ] **Step 6:** Classify the result as `B1`, `B2`, or `B3` using the stop conditions in the design spec.
- [ ] **Step 7:** Render the classification and structural facts in a compact development-only panel; do not alter the widget.

### Task 3: Verify the diagnostic itself

**Files:**
- Verify: `index.html`
- Verify: `booksy-widget-diagnostic.js`
- Verify: `tests/test_booksy_widget_diagnostic.py`

**Interfaces:**
- Consumes: diagnostic implementation.
- Produces: evidence that the diagnostic is isolated and non-invasive.

- [ ] **Step 1:** Run `pytest -q tests/test_booksy_widget_diagnostic.py` and require zero failures.
- [ ] **Step 2:** Run a JavaScript syntax check with `node --check booksy-widget-diagnostic.js`.
- [ ] **Step 3:** Compare `main...dev/booksy-widget-description` and confirm only the experiment spec/plan/test/diagnostic and intended `index.html` script reference changed.
- [ ] **Step 4:** Confirm the diagnostic source contains no booking-button replacements, network interception, storage reads, or form-value reads.

### Task 4: Determine the Booksy architecture result

**Files:**
- Read-only runtime inspection of the branch preview and public Booksy embed architecture.

**Interfaces:**
- Consumes: diagnostic output plus Booksy's actual modal structure.
- Produces: final B1/B2/B3 recommendation.

- [ ] **Step 1:** Open the development branch with `?booksydebug=1`, trigger the Booksy modal, and record only the diagnostic classification and iframe/container facts.
- [ ] **Step 2:** If the service rows are directly accessible with stable semantic structure, test a temporary CSS-only clamp removal and re-check Book/close/navigation behavior.
- [ ] **Step 3:** If the modal uses a cross-origin iframe or unstable internals, do not add expansion CSS; classify B3/B2 and stop.
- [ ] **Step 4:** Report the result to the user with a recommendation; do not merge anything.
