# BoPeeps Production Repository Cleanup and Launch Design

## Goal

Turn `bopeeps-v3-modern` into the small production tree approved by the owner, preserve the complete pre-cleanup state, verify it, promote it to `main` without rewriting history, and reserve a separate scrub-effects experiment branch.

## Safety boundaries

- Create `archive/prelaunch-2026-08-09` from the current v3 head before deleting anything.
- Delete an `assets-v3` image only after scanning `index.html`, `styles-v3.css`, and `script-v3.js` and finding zero references.
- Keep the existing business content, Booksy and Facebook links, contact details, hours, address, hero, and scrub interaction unchanged.
- Keep Porkbun email MX and TXT records unchanged during any later custom-domain cutover.
- Stop promotion if any verification fails.

## Production shape

The production branch contains `.nojekyll`, `README.md`, `index.html`, `styles-v3.css`, `script-v3.js`, `assets/logo-modern.jpg`, and only the locally referenced files under `assets-v3/`.

Legacy layouts, v2 assets, development documentation, tests, and unused media remain recoverable from the archive branch but are not shipped from `main`.

## Launch sequence

1. Preserve the pre-cleanup commit on the archive branch.
2. Prove the deletion and reference boundaries.
3. Clean the v3 branch and rewrite its README.
4. Verify assets, JavaScript, contact data, booking links, hero art direction, scrub behavior, and exact production-tree shape.
5. Promote by normal fast-forward or merge only, then reverify `main`.
6. Serve Pages from `main /`, create `experiment/scrub-effects`, and verify the live Pages build.
7. Configure `bopeepsdetails.com` only after Pages is healthy and only while preserving email DNS records.
