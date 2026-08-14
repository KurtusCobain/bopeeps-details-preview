# Corrected Storefront and Favicon Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the old-number storefront hero assets with optimized derivatives of the approved corrected image and add a BoPeeps favicon for browser and search-result display.

**Architecture:** Keep the existing asset URLs and responsive `<picture>` integration so all current consumers receive the corrected artwork without route changes. Generate a desktop WebP from the complete supplied image, a focused mobile crop from the same image, and standard favicon files from the official logo; add favicon declarations to every public HTML page.

**Tech Stack:** Static HTML/CSS, Python 3 with bundled Pillow for image processing, pytest, Node.js syntax validation, GitHub Pages.

## Global Constraints

- Preserve the current hero layout, overlay text, navigation, trust strip, booking and call links, accessibility behavior, and reduced-motion support.
- Preserve the supplied storefront content; only resize, compress, and crop it responsively.
- Keep `assets-v3/hero-storefront-desktop.webp` and `assets-v3/hero-storefront-mobile.webp` as the public hero URLs.
- Use `980-598-1864` in website content and `tel:+19805981864` for call links.
- Publish to production `main` only after local verification passes.

---

### Task 1: Add storefront and favicon regression coverage

**Files:**
- Modify: `tests/test_local_seo_expansion.py`

**Interfaces:**
- Consumes: `INDEXABLE`, `html(name)`, and public files under the repository root.
- Produces: regression tests requiring both hero WebPs and favicon declarations on every public page.

- [ ] **Step 1: Write the failing tests**

Add assertions equivalent to:

```python
PUBLIC_PAGES = INDEXABLE + ['404.html']

def test_storefront_and_favicon_assets_exist():
    for name in [
        'assets-v3/hero-storefront-desktop.webp',
        'assets-v3/hero-storefront-mobile.webp',
        'favicon-48.png',
        'apple-touch-icon.png',
        'favicon.ico',
    ]:
        path = ROOT / name
        assert path.exists(), name
        assert path.stat().st_size > 0, name

def test_every_public_page_declares_the_favicon():
    for name in PUBLIC_PAGES:
        text = html(name)
        assert 'rel="icon"' in text, name
        assert 'href="favicon-48.png"' in text, name
        assert 'rel="apple-touch-icon"' in text, name
        assert 'href="apple-touch-icon.png"' in text, name
```

- [ ] **Step 2: Run the focused tests and verify failure**

Run:

```powershell
python -m pytest tests/test_local_seo_expansion.py -q -p no:cacheprovider
```

Expected: failure because the favicon files and declarations do not exist yet.

### Task 2: Generate the approved responsive storefront assets

**Files:**
- Replace: `assets-v3/hero-storefront-desktop.webp`
- Replace: `assets-v3/hero-storefront-mobile.webp`

**Interfaces:**
- Consumes: `C:\Users\katie\Downloads\Bopeeps\bopeeps_storefront_correct_phone.png` at 1684x934 pixels.
- Produces: desktop WebP at 1684x934 and mobile WebP from crop box `(220, 0, 1220, 934)`.

- [ ] **Step 1: Generate the WebPs with bundled Pillow**

Use the approved source image. Save the complete source as the desktop asset with WebP quality 86 and method 6. Crop the mobile source to `(220, 0, 1220, 934)` so the storefront sign, corrected phone number, and Jeep remain visible while the baked-in Booksy graphic is excluded; save it at WebP quality 86 and method 6.

- [ ] **Step 2: Verify formats and dimensions**

Open both generated files with Pillow and assert:

```python
assert desktop.format == 'WEBP' and desktop.size == (1684, 934)
assert mobile.format == 'WEBP' and mobile.size == (1000, 934)
```

### Task 3: Create and declare the favicon set

**Files:**
- Create: `favicon-48.png`
- Create: `apple-touch-icon.png`
- Create: `favicon.ico`
- Modify: `index.html`
- Modify: `services.html`
- Modify: `auto-detailing-hayesville-nc.html`
- Modify: `auto-detailing-murphy-nc.html`
- Modify: `auto-detailing-hiawassee-ga.html`
- Modify: `auto-detailing-young-harris-ga.html`
- Modify: `auto-detailing-blairsville-ga.html`
- Modify: `policies.html`
- Modify: `privacy.html`
- Modify: `404.html`

**Interfaces:**
- Consumes: `assets/logo-modern.jpg` as the official BoPeeps logo source.
- Produces: crawlable root favicon assets and page-level icon declarations.

- [ ] **Step 1: Generate square favicon artwork**

Crop the official 1536x1024 logo with box `(90, 100, 1446, 700)` to retain the car silhouette and BoPeeps wordmark while excluding the old phone number. Fit the crop proportionally within a 512x512 black canvas with 24 pixels of minimum padding, then save 48x48 PNG, 180x180 PNG, and a multi-size ICO containing 16x16, 32x32, and 48x48 variants.

- [ ] **Step 2: Add favicon declarations to all public pages**

Insert after each page's theme-color metadata:

```html
<link rel="icon" type="image/png" sizes="48x48" href="favicon-48.png" />
<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png" />
```

- [ ] **Step 3: Update the homepage hero intrinsic dimensions**

Change the desktop `<img>` attributes to `width="1684" height="934"` while retaining the existing alt text and responsive source paths.

- [ ] **Step 4: Run the focused test and verify it passes**

Run:

```powershell
python -m pytest tests/test_local_seo_expansion.py -q -p no:cacheprovider
```

Expected: all tests pass.

### Task 4: Verify, commit, publish, and confirm production

**Files:**
- Verify all files changed in Tasks 1-3.

**Interfaces:**
- Consumes: completed static-site changes.
- Produces: verified production deployment on `https://bopeepsdetails.com/`.

- [ ] **Step 1: Run full local verification**

Run:

```powershell
python -m pytest -q -p no:cacheprovider
node --check script-v3.js
git diff --check
```

Confirm the old phone number does not occur in public HTML and all favicon links resolve to local files.

- [ ] **Step 2: Inspect desktop and mobile hero renders**

Serve the repository locally and inspect the homepage at desktop and 390px mobile widths. Confirm the corrected sign is readable, the mobile crop excludes the baked-in Booksy graphic, the real booking button remains clickable, and there is no horizontal overflow.

- [ ] **Step 3: Commit the implementation**

```powershell
git add assets-v3/hero-storefront-desktop.webp assets-v3/hero-storefront-mobile.webp favicon-48.png apple-touch-icon.png favicon.ico *.html tests/test_local_seo_expansion.py
git commit -m "Update storefront hero and favicon"
```

- [ ] **Step 4: Publish and live-verify**

Push the current commit to production `main`, wait for GitHub Pages, then verify the live homepage returns HTTP 200 and serves the corrected hero and favicon assets.
