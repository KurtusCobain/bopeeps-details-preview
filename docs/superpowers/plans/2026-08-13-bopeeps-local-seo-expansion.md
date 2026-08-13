# BoPeeps Local SEO Expansion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and verify a crawlable local SEO expansion for BoPeeps Details & More covering Hayesville, Murphy, Hiawassee, Young Harris, and Blairsville while preserving the current customer experience and Booksy booking flow.

**Architecture:** Keep the existing homepage as the visual and conversion hub, add one shared SEO-page stylesheet plus seven new customer-facing static HTML routes, and expose them through crawlable internal links. Technical SEO is implemented with canonical metadata, consistent one-location LocalBusiness JSON-LD, `robots.txt`, a 9-URL `sitemap.xml`, a branded 404, and static regression tests that guard against fake locations/mobile-service claims.

**Tech Stack:** Static HTML5, CSS3, existing vanilla JavaScript, JSON-LD, XML sitemap, GitHub Pages, pytest static-content tests.

## Global Constraints

- Work only on `dev/local-seo-expansion` until the user explicitly approves a merge.
- BoPeeps has one physical shop: `1516 US-64, Hayesville, NC 28904`.
- BoPeeps does not currently provide mobile detailing.
- Approved service areas: Hayesville NC, Murphy NC, Hiawassee GA, Young Harris GA, Blairsville GA.
- Phone remains `706-897-6177`; email remains `hello@bopeepsdetails.com`.
- Booksy URL remains `https://booksy.com/en-us/1808686_bopeeps-detail-more_other_26564_hayesville`.
- Existing homepage hero, storefront imagery, service cards, trust strip, gallery, scrub interaction, About, Contact, mobile quick actions, and Booksy behavior remain recognizable.
- Do not change DNS, GitHub Pages settings, email routing, Booksy configuration, prices, or payment settings.
- Do not invent reviews, ratings, awards, certifications, distances, drive times, branch locations, mobile service, testimonials, or unverified service inclusions.

---

### Task 1: Add SEO regression tests first

**Files:**
- Create: `tests/test_local_seo_expansion.py`

**Interfaces:**
- Consumes: intended route names and immutable business facts from the approved spec.
- Produces: static assertions used by every later task.

- [ ] **Step 1:** Add tests requiring the nine indexable HTML routes: `index.html`, `services.html`, five city pages, `policies.html`, and `privacy.html`, plus `404.html`, `robots.txt`, and `sitemap.xml`.
- [ ] **Step 2:** Require every indexable HTML route to contain a unique `<title>`, meta description, canonical `https://bopeepsdetails.com/...` URL, and exactly one `<h1` opening tag.
- [ ] **Step 3:** Require every city page to contain `1516 US-64`, `706-897-6177`, `Hayesville`, and language stating that service is completed at the Hayesville shop; forbid `mobile detailing` as an offered service and forbid secondary street addresses.
- [ ] **Step 4:** Require `sitemap.xml` to contain exactly nine `<loc>` entries and exclude `404.html`, tests, docs, and dev URLs.
- [ ] **Step 5:** Require `robots.txt` to advertise `https://bopeepsdetails.com/sitemap.xml`.
- [ ] **Step 6:** Require the production Booksy URL and approved pet-hair policy wording to remain present.
- [ ] **Step 7:** Run the test and confirm RED because the new pages/files do not exist yet.

### Task 2: Add shared SEO page visual system

**Files:**
- Create: `seo-pages.css`

**Interfaces:**
- Consumes: variables/components from `styles-v3.css`.
- Produces: reusable hero, content-card, service-area, CTA, footer-link, and 404 layouts for all new static pages.

- [ ] **Step 1:** Add a shared dark/red page system that reuses existing typography, buttons, header, logo, and mobile actions.
- [ ] **Step 2:** Keep all layout mobile-first and ensure local/service cards become multi-column only at wider breakpoints.
- [ ] **Step 3:** Do not change `styles-v3.css` unless a missing shared primitive is proven necessary.

### Task 3: Build Services and Privacy routes

**Files:**
- Create: `services.html`
- Create: `privacy.html`

**Interfaces:**
- Consumes: `styles-v3.css`, `seo-pages.css`, logo/assets, current verified service names/prices/durations, Booksy URL, business NAP.
- Produces: two indexable canonical routes with crawlable navigation.

- [ ] **Step 1:** Build `services.html` with unique metadata/H1, the three verified Booksy services, vehicle types already stated on the homepage, Booksy CTAs, pet-hair disclosure, Hayesville shop statement, and local-area links.
- [ ] **Step 2:** Build `privacy.html` describing hosting request data and third-party Booksy, directions/Google Maps, and Facebook links without claiming analytics/cookies/payment storage that are not present.
- [ ] **Step 3:** Add one-location JSON-LD to Services and appropriate business/navigation metadata to Privacy.

### Task 4: Build five truthful local landing pages

**Files:**
- Create: `auto-detailing-hayesville-nc.html`
- Create: `auto-detailing-murphy-nc.html`
- Create: `auto-detailing-hiawassee-ga.html`
- Create: `auto-detailing-young-harris-ga.html`
- Create: `auto-detailing-blairsville-ga.html`

**Interfaces:**
- Consumes: shared SEO stylesheet, verified business facts, current services, Booksy URL.
- Produces: five unique local-search pages representing one Hayesville shop.

- [ ] **Step 1:** Give every page a unique title, description, canonical URL, H1, intro, and city-specific service-area wording.
- [ ] **Step 2:** State clearly on every surrounding-city page that appointments are performed at `1516 US-64, Hayesville, NC 28904` and customers bring vehicles to the shop.
- [ ] **Step 3:** Keep the Hayesville page focused on the physical shop while still referencing the surrounding approved service area.
- [ ] **Step 4:** Add Services, Booksy, Policies, Home/Contact, and approved service-area links using normal anchors.
- [ ] **Step 5:** Use one LocalBusiness/AutomotiveBusiness entity with Hayesville address; surrounding cities appear only through `areaServed` or explanatory copy.

### Task 5: Add crawler and error routes

**Files:**
- Create: `robots.txt`
- Create: `sitemap.xml`
- Create: `404.html`

**Interfaces:**
- Consumes: canonical route inventory.
- Produces: crawler discovery and a branded not-found experience.

- [ ] **Step 1:** Add permissive root `robots.txt` with the production sitemap URL.
- [ ] **Step 2:** Add exactly nine canonical HTTPS sitemap URLs: Home, Services, five city pages, Policies, Privacy.
- [ ] **Step 3:** Add branded `404.html` with `noindex`, Home, Services, Booksy, and Contact navigation; do not include it in the sitemap.

### Task 6: Harden homepage and existing Policies metadata/internal linking

**Files:**
- Modify: `index.html`
- Modify: `policies.html`

**Interfaces:**
- Consumes: new route architecture.
- Produces: crawlable discovery paths from existing high-value pages.

- [ ] **Step 1:** Add homepage canonical URL, `og:url`, `og:site_name`, richer absolute social image URL, and `areaServed` to the existing one-location JSON-LD.
- [ ] **Step 2:** Add a compact homepage service-area block linking Hayesville, Murphy, Hiawassee, Young Harris, and Blairsville, explicitly saying all appointments are completed at the Hayesville shop.
- [ ] **Step 3:** Add crawlable Services, Policies, Privacy, and Facebook links in a compact footer/site-links treatment without overwhelming the primary navigation.
- [ ] **Step 4:** Add canonical/social metadata and core route links to `policies.html` while preserving the approved pet-hair copy exactly.

### Task 7: Verify the full development branch

**Files:**
- Verify all production routes and test files.

**Interfaces:**
- Consumes: completed branch.
- Produces: pre-review evidence and rendered previews.

- [ ] **Step 1:** Run `pytest -q` (or, if the connected repo cannot execute CI directly, materialize the exact branch files into a local temporary directory and run the static tests there) and require zero failures.
- [ ] **Step 2:** Run `node --check script-v3.js` and require success.
- [ ] **Step 3:** Parse every HTML file to verify unique title/meta/canonical/H1 and validate sitemap count/contents.
- [ ] **Step 4:** Compare `main...dev/local-seo-expansion`; require ahead-only with no DNS/CNAME/Pages changes.
- [ ] **Step 5:** Open/create a draft PR for review only; do not merge.
- [ ] **Step 6:** Provide direct rendered branch previews for Home, Services, all five local pages, Policies, Privacy, and 404.
