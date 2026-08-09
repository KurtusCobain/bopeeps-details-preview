# Gallery Image Swap Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the Exterior care and Real local work gallery images with Photos 27 and 16.

**Architecture:** Preserve the existing static gallery structure and CSS. Add two optimized WebP assets and update only the two corresponding `img` elements and the gallery source contract.

**Tech Stack:** Static HTML, Python `unittest`, Pillow WebP conversion, GitHub Pages.

## Global Constraints

- Work only on `bopeeps-v3-modern`.
- Keep all six captions, gallery layout, responsive crops, overlays, and the remaining four images unchanged.
- Save Photo 27 as `assets-v3/gallery-exterior-care.webp` and Photo 16 as `assets-v3/gallery-real-local-work.webp`, each at 1200 by 1600 pixels.
- Do not generate, retouch, or materially alter the supplied photos.
- Do not merge or modify `main`, Porkbun, or the production domain.

---

### Task 1: Replace the two gallery assets

**Files:**
- Create: `assets-v3/gallery-exterior-care.webp`
- Create: `assets-v3/gallery-real-local-work.webp`
- Modify: `index.html:192-197`
- Test: `tests/test_site_contract.py:124-139`

**Interfaces:**
- Consumes: the existing ordered `.gallery-grid` figures and their `img[src]`, `img[alt]`, and `figcaption` values.
- Produces: meaningful local WebP paths resolved by GitHub Pages and consumed by the unchanged gallery CSS.

- [x] **Step 1: Write the failing contract test**

Change the first and sixth expected gallery sources to literal values:

```python
[
    "assets-v3/gallery-exterior-care.webp",
    "assets-v3/gallery-photo-8.webp",
    "assets-v3/gallery-photo-14.webp",
    "assets-v3/gallery-photo-21.webp",
    "assets-v3/gallery-photo-25.webp",
    "assets-v3/gallery-real-local-work.webp",
]
```

Also assert that the ordered captions remain `Exterior care`, `Trucks & daily drivers`, `Interior attention`, `Jeeps & SUVs`, `RVs welcome`, and `Real local work`.

- [x] **Step 2: Verify the test fails for the old mappings**

Run:

```powershell
python -m unittest tests.test_site_contract.SiteContractTests.test_gallery_uses_the_six_approved_real_work_photos -v
```

Expected: FAIL because the first and sixth tiles still use `gallery-photo-5.webp` and `gallery-photo-28.webp`.

- [x] **Step 3: Create the optimized assets and update HTML**

Convert `C:\Users\katie\Downloads\Bopeeps\27.jpg` and `16.jpg` to the exact paths above using RGB WebP at quality 85 and a 1600-pixel longest edge. Update only the first and sixth gallery `img` elements, using the approved 1200 by 1600 dimensions and alternative text from the design spec.

- [x] **Step 4: Verify locally**

Run the focused test, the full `unittest` suite, `node --check script-v3.js`, `node tests/test_script_behavior.mjs`, WebP dimension checks, and `git diff --check`.

- [ ] **Step 5: Publish and verify the preview**

Commit the implementation, push only `bopeeps-v3-modern`, and verify both images and captions load at `https://kurtuscobain.github.io/bopeeps-details-preview/#work` with no horizontal overflow.
