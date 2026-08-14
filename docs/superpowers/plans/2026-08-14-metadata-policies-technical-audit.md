# Metadata, Policies, and Technical Audit Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Refine search metadata across all indexable BoPeeps pages, improve the existing pet-hair policy page without inventing new rules, and add static technical/accessibility regression checks for the public site.

**Architecture:** Keep the existing static HTML/CSS/JavaScript architecture. Extend `tests/test_local_seo_expansion.py` into the audit harness, make localized metadata/policy edits in existing HTML, and change CSS/JavaScript only when a concrete defect is proven by source review or tests.

**Tech Stack:** Static HTML5, CSS3, vanilla JavaScript, JSON-LD, XML sitemap, GitHub Pages, pytest static-content tests.

## Global Constraints

- Work only on `dev/site-cleanup-phone-audit` until explicit approval to merge/publish.
- Do not modify `main`, CNAME, DNS, GitHub Pages configuration, Booksy configuration, pricing, service names, or approved business facts.
- Website service names remain `Vacuum, Hand Wash & Wax`, `Deluxe Detail Package`, and `BoPeeps Signature Detail`.
- Current phone remains `980-598-1864`; click-to-call remains `tel:+19805981864`.
- Public email remains `hello@bopeepsdetails.com`.
- Physical shop remains `1516 US-64, Hayesville, NC 28904`.
- Do not invent cancellation, no-show, payment, liability, property, biohazard, review, award, certification, location, or mobile-service claims.
- Do not add a web-app manifest solely for SEO.

---

### Task 1: Expand the static audit harness

**Files:**
- Modify: `tests/test_local_seo_expansion.py`

**Interfaces:**
- Consumes: all files in `PUBLIC_PAGES`, `INDEXABLE`, `EXPECTED_CANONICALS`, and existing business constants.
- Produces: regression checks used by every later task.

- [ ] **Step 1:** Add standard-library helpers using `html.parser.HTMLParser` and `urllib.parse.urlsplit` to collect headings, IDs, links, images, and metadata from each public HTML file.
- [ ] **Step 2:** Add metadata assertions requiring every indexable page to have unique title/meta description/OG title/OG description, `og:url == canonical`, one H1, and the expected canonical URL.
- [ ] **Step 3:** Add internal-link checks. For each relative `.html` href, assert the target file exists; when the href contains a fragment, assert that ID exists in the target page. For same-page `#fragment` links, assert the fragment ID exists locally.
- [ ] **Step 4:** Add duplicate-ID and heading-level checks. Assert every ID occurs once per page and heading levels never jump by more than one level after H1.
- [ ] **Step 5:** Add image checks. Every `<img>` must have `alt`, positive numeric `width`, and positive numeric `height`; every local `src`/`srcset` asset must exist. Permit `alt=""` only on scrub-choice thumbnails whose parent button supplies visible text.
- [ ] **Step 6:** Add business-data checks requiring public HTML to use only the current Booksy profile, current Facebook profile when Facebook is linked, current phone/email/address, and approved service/business naming.
- [ ] **Step 7:** Add structured-data checks on pages containing LocalBusiness/AutomotiveBusiness JSON-LD: Hayesville street address, current phone/email/site URL, approved service-area city names, and current Booksy ReserveAction target.
- [ ] **Step 8:** Keep all existing sitemap, robots, favicon, phone, policy, service/pricing, homepage-flow, and local-SEO tests intact.

### Task 2: Refine metadata and search snippets

**Files:**
- Modify: `index.html`
- Modify: `services.html`
- Modify: `auto-detailing-hayesville-nc.html`
- Modify: `auto-detailing-murphy-nc.html`
- Modify: `auto-detailing-hiawassee-ga.html`
- Modify: `auto-detailing-young-harris-ga.html`
- Modify: `auto-detailing-blairsville-ga.html`
- Modify: `policies.html`
- Modify: `privacy.html`

**Interfaces:**
- Consumes: existing canonical URLs and page-specific content from the current branch.
- Produces: nine distinct search/OG intents without changing routes.

- [ ] **Step 1:** Preserve every canonical URL exactly as listed in `sitemap.xml`.
- [ ] **Step 2:** Refine Home title/description/OG description around branded Hayesville detailing, clear pricing, real local work, and surrounding service area.
- [ ] **Step 3:** Refine Services metadata around the three current packages, vehicle-size pricing, specialty vehicles, and Hayesville booking.
- [ ] **Step 4:** Refine each city page metadata so its title/description/OG copy reflects its already-approved unique regional context rather than repeating generic “in-shop detailing” wording.
- [ ] **Step 5:** Refine Policies metadata so it explicitly describes pricing, vehicle condition, and excessive pet-hair information—nothing broader.
- [ ] **Step 6:** Refine Privacy metadata around static-site request data and third-party Booksy/Maps/Facebook use.
- [ ] **Step 7:** Ensure each page's `og:title` is aligned with its title, each `og:description` is useful but not duplicated across pages, and each `og:url` equals its canonical.

### Task 3: Improve the policy-page structure

**Files:**
- Modify: `policies.html`

**Interfaces:**
- Consumes: the approved pet-hair policy wording already present on Home, Services, and Policies.
- Produces: a clearer policy destination without creating new business policy.

- [ ] **Step 1:** Change the H1/lede to make the page scope explicit: pricing and vehicle condition.
- [ ] **Step 2:** Keep the approved core sentence verbatim: `Service prices reflect standard vehicle conditions. Excessive pet hair requiring additional removal time may incur a $20 pet hair removal fee. If applied, the charge will be itemized in your final checkout and reflected on your receipt or payment confirmation email.`
- [ ] **Step 3:** Present three scan-friendly facts: standard-condition baseline, excessive-pet-hair threshold, and checkout/itemization behavior.
- [ ] **Step 4:** Preserve `A few stray hairs are not the intended threshold.`
- [ ] **Step 5:** Add a clearly worded Booksy note: Booksy handles appointment availability and checkout workflow; this page states only the BoPeeps pricing/vehicle-condition policy currently provided on the website.
- [ ] **Step 6:** Preserve Booksy, Services, Home, Privacy, phone/address, footer, service-area links, and mobile quick actions.

### Task 4: Apply concrete technical fixes only

**Files:**
- Modify only files implicated by Task 1 audit failures.

**Interfaces:**
- Consumes: failures/findings from the static audit harness and direct source inspection.
- Produces: corrected markup/assets/references with no speculative refactor.

- [ ] **Step 1:** Fix broken relative links or fragment targets if detected.
- [ ] **Step 2:** Add missing image dimensions or correct invalid/misleading alt text if detected.
- [ ] **Step 3:** Remove or rename duplicate IDs if detected while preserving navigation/JS selectors.
- [ ] **Step 4:** Repair heading-level skips if detected without changing page visual hierarchy unnecessarily.
- [ ] **Step 5:** Correct stale asset, Booksy, Facebook, phone, email, address, canonical, or structured-data references if detected.
- [ ] **Step 6:** Leave `script-v3.js`, `styles-v3.css`, `seo-pages.css`, `sitemap.xml`, and `robots.txt` unchanged when the audit shows no concrete defect.

### Task 5: Verify branch scope and record results

**Files:**
- Create: `docs/superpowers/audits/2026-08-14-metadata-policies-technical-audit.md`
- Verify: all public HTML, `tests/test_local_seo_expansion.py`, `script-v3.js`, stylesheets, `sitemap.xml`, `robots.txt`.

**Interfaces:**
- Consumes: completed branch.
- Produces: pre-merge evidence and an explicit list of verified findings/limitations.

- [ ] **Step 1:** Re-read every changed HTML file and the updated test file from the development branch.
- [ ] **Step 2:** Execute `pytest -q` if an exact branch checkout can be materialized; otherwise explicitly record that automated execution remains unavailable rather than claiming pass status.
- [ ] **Step 3:** Execute `node --check script-v3.js` if an exact branch checkout is available; otherwise record it as not executed.
- [ ] **Step 4:** Compare `main...dev/site-cleanup-phone-audit`; require status `ahead`, `behind_by == 0`, and no CNAME/DNS/Pages configuration changes.
- [ ] **Step 5:** Record what was changed, what was already correct, what was intentionally left alone, and any remaining external/non-code issues.
- [ ] **Step 6:** Do not merge or publish.
