# BoPeeps v3 Modern Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the approved mobile-first black/red BoPeeps Details & More website on `bopeeps-v3-modern` without changing `main`.

**Architecture:** Keep the site static and GitHub Pages compatible. Replace the branch root homepage with a focused `index.html`, `styles-v3.css`, and `script-v3.js`, reuse existing brand assets, add a small set of optimized real BoPeeps photos from the uploaded photo pack, and link all booking actions to the public Booksy profile.

**Tech Stack:** HTML5, CSS3, vanilla JavaScript, GitHub Pages.

## Global Constraints

- Customer-facing name: **BoPeeps Details & More**.
- Phone: **706-897-6177**.
- Email: **hello@bopeepsdetails.com**.
- Address: **1516 US-64, Hayesville, NC 28904**.
- Hours: **Monday-Saturday 7:00 AM-5:00 PM; Sunday closed**.
- Booksy: `https://booksy.com/en-us/1808686_bopeeps-detail-more_other_26564_hayesville`.
- Facebook: `https://www.facebook.com/people/BoPeeps-Detail/61591634832181/`.
- Service cards: Express Wash And Spray Wax $60+ / ~1 hr; Deluxe Detail Package $85+ / ~2 hr; Jacky Jones Premium Detail $150+ / ~4 hr.
- No secrets or account credentials in public code.
- Mobile-first from 320px upward; no page-level horizontal overflow.
- No autoplay audio.
- `main` and `hybrid-preview` remain unchanged.

---

### Task 1: Establish launch page structure and verified business content

**Files:**
- Modify: `index.html`
- Create: `styles-v3.css`
- Create: `script-v3.js`

**Interfaces:**
- Consumes: confirmed business details and Booksy/Facebook URLs from the approved design spec.
- Produces: semantic page sections and stable class/data hooks used by Tasks 2-4.

- [ ] **Step 1:** Replace branch-root `index.html` with semantic sections: header, hero, trust strip, services, work, benefits, contact/map, footer, and mobile sticky actions.
- [ ] **Step 2:** Wire Booksy, phone, email, Facebook, and directions URLs directly in HTML so core actions work without JavaScript.
- [ ] **Step 3:** Add LocalBusiness/AutomotiveBusiness JSON-LD with confirmed 706 phone, email, address, and hours.
- [ ] **Step 4:** Reference `styles-v3.css` and deferred `script-v3.js` only; remove stale quote-form dependencies from the new root page.
- [ ] **Step 5:** Validate that all visible business copy contains no 828 number and no `bopeepsdetail@gmail.com` address.

### Task 2: Implement the approved responsive black/red visual system

**Files:**
- Modify: `styles-v3.css`

**Interfaces:**
- Consumes: semantic classes from Task 1.
- Produces: mobile-first visual layout, desktop expansion, accessible focus states, service card carousel, compact map/contact layout, sticky mobile actions.

- [ ] **Step 1:** Define black/charcoal surfaces, red accent tokens, readable white/gray text, spacing, borders, and responsive typography.
- [ ] **Step 2:** Build the hero to match the approved mockup: dark photographic treatment, bold `DETAILING DONE RIGHT.` headline, Booksy primary CTA and call secondary CTA.
- [ ] **Step 3:** Style the trust strip and three service cards; use horizontal scroll-snap below tablet widths and a three-column grid on larger screens.
- [ ] **Step 4:** Style the work/gallery area for touch-first use and the benefits section with concise icon-like visual marks implemented in CSS/inline SVG.
- [ ] **Step 5:** Build the contact area with details and a small map card beside the address on wide screens and immediately below on phones.
- [ ] **Step 6:** Add bottom safe-area padding and a sticky mobile Call / Directions / Book bar that never covers content.
- [ ] **Step 7:** Respect `prefers-reduced-motion` and preserve clear keyboard focus indicators.

### Task 3: Add real BoPeeps imagery and touch/mouse interactions

**Files:**
- Create: `assets-v3/hero.webp`
- Create: `assets-v3/detail-interior.webp`
- Create: `assets-v3/detail-exterior.webp`
- Create: `assets-v3/before-interior.webp`
- Create: `assets-v3/after-interior.webp`
- Create: `assets-v3/gallery-1.webp`
- Create: `assets-v3/gallery-2.webp`
- Modify: `index.html`
- Modify: `script-v3.js`
- Modify: `styles-v3.css`

**Interfaces:**
- Consumes: selected uploaded BoPeeps photos.
- Produces: optimized launch imagery, a clean-reveal interaction, mobile menu behavior, and a simple genuine before/after control.

- [ ] **Step 1:** Select 6-7 real images from the uploaded Bopeeps photo archive and export mobile-friendly WebP variants with bounded dimensions.
- [ ] **Step 2:** Add width/height or fixed aspect-ratio containers in HTML to prevent layout shift.
- [ ] **Step 3:** Implement pointer/touch clean-reveal using a canvas overlay that draws a simulated grime veil and erases it under pointer movement to reveal the real finished photo.
- [ ] **Step 4:** Add progress/completion handling and a subtle shine state after enough area is revealed; no autoplay sound.
- [ ] **Step 5:** Add a lightweight real before/after comparison using matching dirty/clean interior photos and a native range input.
- [ ] **Step 6:** Implement mobile navigation toggle and ensure the menu closes on navigation and Escape.
- [ ] **Step 7:** Ensure all interactive features remain usable if JavaScript fails: gallery images and booking/contact links still display and work.

### Task 4: Verification and launch-readiness review

**Files:**
- Modify as required: `index.html`, `styles-v3.css`, `script-v3.js`

**Interfaces:**
- Consumes: Tasks 1-3 complete branch implementation.
- Produces: verified `bopeeps-v3-modern` candidate ready for visual approval before domain cutover.

- [ ] **Step 1:** Run static checks for required strings/links and forbidden stale strings (`828-`, `bopeepsdetail@gmail.com`).
- [ ] **Step 2:** Parse HTML locally and verify stylesheet/script/image references resolve in a reconstructed branch workspace.
- [ ] **Step 3:** Test representative viewport widths 320, 375, 430, 768, 1024, and desktop for overflow-sensitive CSS rules.
- [ ] **Step 4:** Verify Booksy, tel, mailto, Facebook, and directions links are present and correct.
- [ ] **Step 5:** Verify reduced-motion styling, keyboard focus styles, alt text, semantic landmarks, and mobile sticky-bar content clearance.
- [ ] **Step 6:** Compare `main...bopeeps-v3-modern` and confirm only the new branch contains v3 changes.
- [ ] **Step 7:** Do not merge or point `bopeepsdetails.com` at GitHub until Austin approves the built version.
