# Service Card Image Swap Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the three service-card photos with the three approved supplied graphics under simple, meaningful filenames.

**Architecture:** Keep the current static card markup and fixed 210-pixel image area. Convert each 1254-by-1254 source PNG to an optimized WebP in `assets-v3`, update the three service image references, dimensions, alt text, and structural contract, then use a dark matching backdrop plus a centered contained foreground so the box fills without stretching the artwork or changing card dimensions.

**Tech Stack:** Static HTML, WebP assets generated with Pillow, Python `unittest` contract tests.

## Global Constraints

- Work only on `bopeeps-v3-modern`.
- Do not change service copy, prices, durations, buttons, layout, hero, gallery, scrub images, `main`, Porkbun, or the custom domain.
- Use `service-wash.webp`, `service-interior.webp`, and `service-premium.webp`.
- Preserve the supplied artwork without generation or retouching.
- Keep the service image area at 210 pixels high, fill its width with a dark matching backdrop, and keep the foreground artwork unstretched with `object-fit: contain`.

---

### Task 1: Replace the three service-card images

**Files:**
- Create: `assets-v3/service-wash.webp`
- Create: `assets-v3/service-interior.webp`
- Create: `assets-v3/service-premium.webp`
- Modify: `index.html:108-128`
- Test: `tests/test_site_contract.py`

**Interfaces:**
- Consumes: the three approved source PNG files and the existing `.service-card img` crop.
- Produces: three relative WebP image paths required by `index.html` and the structural test.

- [x] **Step 1: Update the service-card contract**

Require the ordered paths `assets-v3/service-wash.webp`, `assets-v3/service-interior.webp`, and `assets-v3/service-premium.webp` in `test_service_cards_use_real_photos_and_verified_details`.

- [x] **Step 2: Run the focused contract and verify RED**

Run: `python -m unittest tests.test_site_contract.SiteContractTests.test_service_cards_use_real_photos_and_verified_details -v`

Expected: FAIL because `index.html` still references the three prior photo filenames.

- [x] **Step 3: Convert the supplied files and update markup**

Use Pillow to save the spray-bottle PNG as `service-wash.webp`, the interior PNG as `service-interior.webp`, and the branded-truck PNG as `service-premium.webp`, each at its native 1254 by 1254 resolution. Update the three `src` attributes, dimensions, and illustration-appropriate alt text in `index.html`.

- [x] **Step 4: Verify GREEN and inspect responsive cards**

Run the focused test, full static suite, JavaScript syntax check, and `git diff --check`. Serve locally and confirm the three images load without overflow at desktop and 390px mobile widths.

- [ ] **Step 5: Commit, push, and live-check**

Commit only the approved image swap to `bopeeps-v3-modern`, push that branch, wait for Pages, and confirm the three new filenames and working images at the existing preview URL.
