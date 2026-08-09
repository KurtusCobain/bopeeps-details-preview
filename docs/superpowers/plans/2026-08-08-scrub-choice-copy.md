# Scrub Choice and Copy Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Revise the existing scrub choices and description, using ZIP Photo 9 for Work Vehicles.

**Architecture:** Preserve the existing data-attribute-driven canvas controller. Change only the static HTML contract and add one optimized WebP asset.

**Tech Stack:** Static HTML, CSS, JavaScript, Python `unittest`, Pillow image conversion.

## Global Constraints

- Work only on `bopeeps-v3-modern`.
- Do not merge or modify `main`, Porkbun, or the production domain.
- Keep the existing scrub behavior, card sizing, gallery, services, and contact content unchanged.

---

### Task 1: Update the scrub content contract

**Files:**
- Modify: `tests/test_site_contract.py`
- Create: `assets-v3/scrub-work-vehicles.webp`
- Modify: `index.html`

**Interfaces:**
- Consumes: existing `data-scrub-choice`, `data-scrub-src`, and `data-scrub-alt` hooks.
- Produces: four semantic scrub choices consumed by the unchanged canvas controller.

- [x] **Step 1: Write the failing test**

Assert the ordered IDs, sources, labels, new paragraph, and presence of the optimized asset.

- [x] **Step 2: Run test to verify it fails**

Run: `python -m unittest tests.test_site_contract.SiteContractTests.test_scrub_selector_exposes_the_four_approved_real_photos -v`

Expected: FAIL because the existing choices still reference Photo 11 and the old labels and description.

- [x] **Step 3: Write the minimal implementation**

Convert `C:\Users\katie\Downloads\Bopeeps\9.jpg` to `assets-v3/scrub-work-vehicles.webp` at a maximum 1600-pixel long edge, then update the scrub paragraph and choice markup in `index.html`.

- [ ] **Step 4: Run verification**

Run the focused test, full static test suite, JavaScript syntax check, and browser smoke test at desktop and 390px mobile widths.

- [ ] **Step 5: Publish the preview branch**

Commit and push only `bopeeps-v3-modern`, then verify the updated HTML and image on the existing GitHub Pages preview.
