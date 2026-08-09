# Storefront Hero Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the truck-wrap hero with the approved responsive storefront design using real desktop and mobile source photos.

**Architecture:** Art-direct one semantic hero through a `<picture>` element. Below 768 pixels the hero uses a photo panel above centered content; at 768 pixels and wider it becomes a full-background storefront with left-aligned overlay content.

**Tech Stack:** Static HTML, CSS media queries, Python `unittest`, Pillow WebP conversion, GitHub Pages.

## Global Constraints

- Work only on `bopeeps-v3-modern`.
- Use `store front1.png` for desktop and `store front 2.png` for mobile.
- Keep the full approved description accessible at every width and show `Cars, trucks, SUVs, RVs, and work vehicles.` visually on mobile.
- Preserve the site header, trust strip, Booksy/phone destinations, reduced motion, and all non-hero sections.
- Do not merge or modify `main`, Porkbun, or the production domain.

---

### Task 1: Build the responsive storefront hero

**Files:**
- Create: `assets-v3/hero-storefront-desktop.webp`
- Create: `assets-v3/hero-storefront-mobile.webp`
- Modify: `index.html:72-89`
- Modify: `styles-v3.css:68-78,177-206`
- Test: `tests/test_site_contract.py`

**Interfaces:**
- Consumes: the existing `.hero`, `.hero-image`, `.hero-copy`, `.hero-text`, and `.hero-actions` hooks.
- Produces: `.hero-media`, `.hero-text-full`, and `.hero-text-mobile` hooks rendered by one responsive `<picture>` and the unchanged booking links.

- [x] **Step 1: Write failing structure and style tests**

Assert one `.hero-media` picture contains a mobile source with `media="(max-width: 767px)"` and `assets-v3/hero-storefront-mobile.webp`, plus a fallback image using `assets-v3/hero-storefront-desktop.webp`. Assert the mobile summary, full approved copy, Booksy/phone links, descriptive alt text, and absence of `storefrontdesktop.png` and `storemobile.png` references.

Assert `styles-v3.css` contains an `@media (min-width: 768px)` desktop boundary, a mobile `.hero-media` photo-panel rule, desktop absolute `.hero-media`, centered mobile content, left-aligned desktop content, and mobile full-copy screen-reader-only treatment.

- [x] **Step 2: Verify the new tests fail**

Run the two focused storefront hero tests with `python -m unittest -v` and expect failures because the current hero uses `assets/truck-wrap.jpg` and has no art-directed markup.

- [x] **Step 3: Create optimized WebP assets**

Convert `store front1.png` to `hero-storefront-desktop.webp` at 1672 by 941 and `store front 2.png` to `hero-storefront-mobile.webp` at 941 by 1672 using RGB WebP quality 85 without altering the photo content.

- [x] **Step 4: Implement semantic hero markup**

Replace the single truck-wrap image with the approved `<picture>`, preserve the heading/tagline/actions, wrap the full and mobile descriptions in distinct semantic hooks, and bump the CSS query string to invalidate the Pages cache.

- [x] **Step 5: Implement responsive hero CSS**

Use a mobile-first stacked grid with a top photo panel and centered black content panel. At 768 pixels, convert the media to a full absolute background, apply a left black gradient, left-align the copy, restore the full description, hide the mobile visual summary, and display actions inline.

- [ ] **Step 6: Verify locally**

Run focused tests, the full `unittest` suite, JavaScript syntax and behavior tests, WebP dimension checks, `git diff --check`, and visual browser checks at desktop and 390-pixel mobile widths.

- [ ] **Step 7: Publish and verify**

Commit and push only `bopeeps-v3-modern`, wait for GitHub Pages, then repeat critical image, responsive layout, link, overflow, and console checks on the live preview.
