# Homepage Conversion and Local SEO Refresh Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Tighten the homepage conversion flow and rewrite the five existing local SEO pages with distinct, truthful regional context and city-specific directions to the single Hayesville shop.

**Architecture:** Preserve the static-site structure, visual system, service/pricing source of truth, Booksy integration and one-location schema. Reorder and compress existing homepage components rather than introducing a redesign, and rewrite each existing city page in place while keeping shared navigation, service tables, policy information and LocalBusiness data consistent.

**Tech Stack:** Static HTML5/CSS3, existing vanilla JavaScript, JSON-LD, Google Maps directions URLs, pytest static-content regression tests, GitHub Pages.

## Global Constraints

- Work only on `dev/site-cleanup-phone-audit` until explicit approval to merge/publish.
- Website services remain exactly `Vacuum, Hand Wash & Wax`, `Deluxe Detail Package`, and `BoPeeps Signature Detail` with current website pricing.
- Booksy remains the booking destination and will be updated separately to match the website.
- BoPeeps has one physical location: `1516 US-64, Hayesville, NC 28904`.
- Do not imply additional locations or mobile detailing.
- Do not invent reviews, ratings, mileage, drive times, customer demographics, partnerships, awards, certifications, or service inclusions.
- Preserve current phone, email, hours, policies, CNAME, DNS, GitHub Pages settings, images, pricing and Booksy URL.

---

### Task 1: Add regression coverage for conversion order and city differentiation

**Files:**
- Modify: `tests/test_local_seo_expansion.py`

**Interfaces:**
- Consumes: existing `html()`, `LOCAL_PAGES`, service-name and one-location assertions.
- Produces: static checks for homepage section order, factual trust copy, real-work-before-scrub ordering, unique city context and directions links.

- [ ] Add a homepage-order test that finds the positions of `id="top"`, the trust strip, `id="services"`, the real-work gallery marker, the interactive demo marker, `id="about"`, the service-area marker and `id="contact"`, then asserts they appear in that order.
- [ ] Require the trust strip to contain factual proof language for the Hayesville shop, package pricing, Booksy booking and real local work, and reject the previous overlapping benefit labels where they were consolidated.
- [ ] Require each local page to contain a Google Maps directions URL with the BoPeeps address as destination.
- [ ] Require distinct regional markers: Hayesville/Clay County, Murphy/Cherokee County, Hiawassee/Lake Chatuge/Towns County, Young Harris/Towns County/Young Harris College, Blairsville/Union County.
- [ ] Keep all existing tests that protect phone numbers, service names, pricing, canonicals, one-location schema, sitemap and policies.

### Task 2: Tighten homepage trust and Why BoPeeps content

**Files:**
- Modify: `index.html`

**Interfaces:**
- Consumes: existing `.trust-strip`, `.about-section`, services, gallery, scrub demo and contact components.
- Produces: shorter mobile scroll with distinct top proof points and a non-repetitive Why BoPeeps section.

- [ ] Replace the four current trust statements with factual proof points: `Real Hayesville shop`, `Clear package pricing`, `Book online`, and `Real local work`.
- [ ] Keep the trust strip directly after the hero.
- [ ] Reduce the lower Why BoPeeps copy so it focuses on careful finish work, vehicle variety and straightforward in-shop service without repeating the trust strip.
- [ ] Preserve all existing service names, prices, Booksy URLs, phone numbers, images and mobile quick actions.

### Task 3: Put real work before the interactive scrub demo

**Files:**
- Modify: `index.html`

**Interfaces:**
- Consumes: existing `.gallery-grid`, `.reveal-card`, scrub data attributes and `script-v3.js` behavior.
- Produces: gallery-first proof sequence while preserving interactive functionality.

- [ ] Rewrite the work-section heading to introduce genuine BoPeeps work first.
- [ ] Move the existing `.gallery-grid` before the `.work-grid`/`.reveal-card` markup.
- [ ] Add a concise transition heading immediately before the interactive scrub card so the demo remains understandable after the gallery.
- [ ] Do not modify scrub data attributes, image paths, canvas controls or `script-v3.js`.

### Task 4: Rewrite Hayesville and Murphy pages

**Files:**
- Modify: `auto-detailing-hayesville-nc.html`
- Modify: `auto-detailing-murphy-nc.html`

**Interfaces:**
- Consumes: existing page shell, service pricing, shop facts, Booksy CTA and LocalBusiness schema.
- Produces: two materially distinct pages with truthful local context and directions links.

- [ ] Hayesville: identify Hayesville as the Clay County home shop, reference the NC-64 corridor and Lake Chatuge context, and retain the physical-location emphasis.
- [ ] Murphy: identify Murphy as the Cherokee County market west of Hayesville in the Appalachian mountains, explain that customers travel to the Hayesville shop, and add a Google Maps directions link using Murphy, NC as origin.
- [ ] Preserve exact website service names/prices, address, phone, hours, Booksy URL, policies and one-location schema.
- [ ] Do not add mileage or drive-time claims.

### Task 5: Rewrite Hiawassee, Young Harris and Blairsville pages

**Files:**
- Modify: `auto-detailing-hiawassee-ga.html`
- Modify: `auto-detailing-young-harris-ga.html`
- Modify: `auto-detailing-blairsville-ga.html`

**Interfaces:**
- Consumes: same shared static-page structure and verified regional facts.
- Produces: three distinct north-Georgia pages with region-appropriate vehicle context and directions links.

- [ ] Hiawassee: use Towns County and Lake Chatuge context and naturally mention cars, SUVs, trucks, RVs and PWCs without claiming customer history.
- [ ] Young Harris: use Towns County and Young Harris College context, keeping claims neutral and focused on nearby drivers traveling to Hayesville.
- [ ] Blairsville: use Union County/north Georgia mountain context and relevant daily-driver/truck/SUV/recreation-vehicle language without fabricated local proof.
- [ ] Add a city-specific Google Maps directions link on each page.
- [ ] Preserve exact services/prices, one-location schema, policies, Booksy URL, address, phone and hours.

### Task 6: Verify development branch scope

**Files:**
- Verify: `index.html`
- Verify: five local SEO pages
- Verify: `tests/test_local_seo_expansion.py`
- Verify: design/plan documentation

**Interfaces:**
- Consumes: completed branch.
- Produces: evidence for review without merging or publishing.

- [ ] Re-fetch every changed HTML file and inspect the exact resulting source for required section order, service-name preservation, city-specific wording and directions links.
- [ ] Compare `main...dev/site-cleanup-phone-audit` and confirm the branch remains ahead-only with no CNAME/DNS/Pages/external-configuration changes.
- [ ] Confirm `script-v3.js`, image assets and service pricing are unchanged by this phase.
- [ ] If the exact branch can be materialized, run `pytest -q -p no:cacheprovider` and `node --check script-v3.js`; otherwise explicitly record that automated execution remains unverified rather than claiming a pass.
