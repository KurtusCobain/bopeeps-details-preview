# BoPeeps Production Repository Cleanup & Launch Design

## Goal

Turn `bopeeps-v3-modern` into a small, production-ready website tree, preserve the complete pre-cleanup state on a permanent archive branch, verify the cleaned site, promote it to `main`, and reserve a separate experiment branch for future scrub-effect work.

## Safety Rules

1. No existing file is permanently lost: before cleanup, create `archive/prelaunch-2026-08-09` from the then-current `bopeeps-v3-modern` head.
2. Do not force-move `main` unless a normal fast-forward/merge path is impossible and the user explicitly approves a different integration path.
3. Do not delete any `assets-v3` image unless an automated reference scan across `index.html`, `styles-v3.css`, and `script-v3.js` reports zero references.
4. Do not change the live business content during cleanup except to rewrite stale repository documentation.
5. Keep `706-897-6177`, `hello@bopeepsdetails.com`, the current Booksy profile URL, Facebook link, Hayesville address, and current hours unchanged.
6. Preserve the existing scrub interaction for launch. Sponge cursor, bubbles, sounds, and other scrub experiments belong on a later `experiment/scrub-effects` branch.

## Current Production Source

GitHub Pages is currently served from `bopeeps-v3-modern` at `/`.

The live page currently depends on:

- `.nojekyll`
- `index.html`
- `styles-v3.css`
- `script-v3.js`
- `assets/logo-modern.jpg`
- the referenced images under `assets-v3/`

## Production Keep List

Keep these root files:

- `.nojekyll`
- `index.html`
- `styles-v3.css`
- `script-v3.js`
- `README.md` — rewrite to describe the actual production website and maintenance workflow

Keep this legacy asset only because the current header uses it:

- `assets/logo-modern.jpg`

Keep these referenced `assets-v3` files:

- `assets-v3/gallery-exterior-care.webp`
- `assets-v3/gallery-photo-14.webp`
- `assets-v3/gallery-photo-21.webp`
- `assets-v3/gallery-photo-25.webp`
- `assets-v3/gallery-photo-8.webp`
- `assets-v3/gallery-real-local-work.webp`
- `assets-v3/hero-storefront-desktop.webp`
- `assets-v3/hero-storefront-mobile.webp`
- `assets-v3/scrub-photo-10.webp`
- `assets-v3/scrub-photo-15.webp`
- `assets-v3/scrub-photo-6.webp`
- `assets-v3/scrub-work-vehicles.webp`
- `assets-v3/service-interior.webp`
- `assets-v3/service-premium.webp`
- `assets-v3/service-wash.webp`

## Exact Legacy Deletion Manifest

After the archive branch exists and verification confirms the v3 site does not reference these files, remove the following from `bopeeps-v3-modern`.

### Root legacy files

- `DEPLOYMENT_NOTES.md`
- `script-v2.js`
- `script.js`
- `styles.css`

### `assets-v2/` — remove all files

- `assets-v2/business-card-v2.svg`
- `assets-v2/logo-main-v2.svg`
- `assets-v2/logo-modern-v2.svg`
- `assets-v2/logo-round-v2.svg`
- `assets-v2/poster-detail-v2.svg`
- `assets-v2/social-card-v2.svg`
- `assets-v2/storefront-hero-v2.svg`
- `assets-v2/truck-wrap-v2.svg`

### `assets/` — keep only `logo-modern.jpg`; remove

- `assets/brand-board.jpg`
- `assets/business-card.jpg`
- `assets/contact_sheet.jpg`
- `assets/logo-main.jpg`
- `assets/logo-round.jpg`
- `assets/poster-detail.jpg`
- `assets/services-panel.jpg`
- `assets/social-card.jpg`
- `assets/storefront-full.jpg`
- `assets/storefront-hero.jpg`
- `assets/storefront-mobile.jpg`
- `assets/truck-wrap.jpg`

### `hybrid-preview/` — remove all files

- `hybrid-preview/README.md`
- `hybrid-preview/index.html`
- `hybrid-preview/mobile.css`
- `hybrid-preview/packages-update.css`
- `hybrid-preview/script.js`
- `hybrid-preview/styles.css`

### Development documentation — remove from production after archive

Existing specs:

- `docs/superpowers/specs/2026-08-08-bopeeps-v3-modern-design.md`
- `docs/superpowers/specs/2026-08-08-gallery-image-swap-design.md`
- `docs/superpowers/specs/2026-08-08-hero-description-design.md`
- `docs/superpowers/specs/2026-08-08-scrub-choice-copy-design.md`
- `docs/superpowers/specs/2026-08-08-service-card-image-swap-design.md`
- `docs/superpowers/specs/2026-08-08-storefront-hero-design.md`

Existing plans:

- `docs/superpowers/plans/2026-08-08-bopeeps-v3-modern.md`
- `docs/superpowers/plans/2026-08-08-gallery-image-swap.md`
- `docs/superpowers/plans/2026-08-08-hero-description.md`
- `docs/superpowers/plans/2026-08-08-scrub-choice-copy.md`
- `docs/superpowers/plans/2026-08-08-service-card-image-swap.md`
- `docs/superpowers/plans/2026-08-09-storefront-hero.md`

Cleanup documents created for this operation will also be removed from the production branch after they are preserved by the archive branch:

- `docs/superpowers/specs/2026-08-09-repo-cleanup-launch-design.md`
- `docs/superpowers/plans/2026-08-09-repo-cleanup-launch.md`

## Conditional `assets-v3` Deletion Candidates

Delete these only if the pre-delete reference scan finds zero references in production HTML, CSS, and JavaScript:

- `assets-v3/gallery-photo-5.webp`
- `assets-v3/gallery-photo-28.webp`
- `assets-v3/scrub-photo-11.webp`

If any candidate is referenced, keep it and report the reference instead of deleting it.

## README Rewrite

Replace the stale README with a concise production README containing:

- Business: `BoPeeps Details & More`
- Website purpose: mobile-first static detailing website
- Public phone: `706-897-6177`
- Public email: `hello@bopeepsdetails.com`
- Booking: Booksy
- Hosting: GitHub Pages
- Domain: `bopeepsdetails.com` after DNS cutover
- Production files and what each one does
- How to swap hero, service, scrub, and gallery images
- Reminder that experimental scrub effects are developed off production

The rewritten README must contain no old 828 or 850 phone number and no `bopeepsdetail@gmail.com` address.

## Verification Before Promotion

Run or reproduce equivalent checks against the cleaned branch:

1. JavaScript syntax check for `script-v3.js`.
2. Extract every local `src`, `srcset`, stylesheet/script reference, and CSS `url(...)`; confirm each referenced local file exists.
3. Search production files for stale contact data:
   - fail on `828-`
   - fail on `850-`
   - fail on `bopeepsdetail@gmail.com`
4. Confirm required strings exist:
   - `706-897-6177`
   - `hello@bopeepsdetails.com`
   - the BoPeeps Booksy profile
   - the BoPeeps Facebook page
5. Confirm desktop and mobile storefront hero references exist.
6. Confirm `script-v3.js` still contains the scrub pointer handlers and choice switching logic.
7. Confirm the cleaned Git tree contains only the approved production files/assets plus the rewritten README.

If any verification fails, stop before promoting to `main`.

## Promotion & Launch Sequence

1. Create `archive/prelaunch-2026-08-09` from the current v3 head before deletions.
2. Apply cleanup on `bopeeps-v3-modern`.
3. Run the full verification checklist.
4. Promote verified `bopeeps-v3-modern` to `main` using a non-destructive fast-forward/merge path.
5. Re-run verification on `main`.
6. Point GitHub Pages production source at `main` `/`.
7. Create `experiment/scrub-effects` from the final verified production commit.
8. Verify the GitHub Pages preview before custom-domain DNS cutover.
9. Connect `bopeepsdetails.com` only after the `main` Pages build is healthy; preserve Porkbun email MX/TXT records.

## Expected Production Shape

```text
bopeeps-details-preview/
├── .nojekyll
├── README.md
├── index.html
├── script-v3.js
├── styles-v3.css
├── assets/
│   └── logo-modern.jpg
└── assets-v3/
    ├── gallery-exterior-care.webp
    ├── gallery-photo-14.webp
    ├── gallery-photo-21.webp
    ├── gallery-photo-25.webp
    ├── gallery-photo-8.webp
    ├── gallery-real-local-work.webp
    ├── hero-storefront-desktop.webp
    ├── hero-storefront-mobile.webp
    ├── scrub-photo-10.webp
    ├── scrub-photo-15.webp
    ├── scrub-photo-6.webp
    ├── scrub-work-vehicles.webp
    ├── service-interior.webp
    ├── service-premium.webp
    └── service-wash.webp
```

The three conditional unused v3 assets are absent only if the reference scan confirms they are unused.
