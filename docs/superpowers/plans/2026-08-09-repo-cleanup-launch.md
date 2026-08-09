# BoPeeps Production Cleanup and Launch Plan

- [ ] Verify the existing v3 branch and production references.
- [ ] Commit this launch record and create `archive/prelaunch-2026-08-09` from it.
- [ ] Add a verification script that rejects missing assets, stale contact data, missing booking/social links, missing scrub behavior, and any unapproved production-tree path.
- [ ] Watch the production-tree verification fail against the legacy tree.
- [ ] Remove the approved legacy manifest, unused v3 candidates, tests, and development documents.
- [ ] Rewrite `README.md` for production maintenance.
- [ ] Run the complete verification suite and push `bopeeps-v3-modern`.
- [ ] Promote the verified commit to `main` without force and re-run verification.
- [ ] Point GitHub Pages at `main /` and create `experiment/scrub-effects`.
- [ ] Verify the live Pages build before any custom-domain cutover.
- [ ] Preserve Porkbun MX/TXT email records during custom-domain configuration.
