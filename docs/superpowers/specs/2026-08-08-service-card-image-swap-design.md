# BoPeeps Service Card Image Swap

## Scope

Replace only the three images at the top of the existing service cards on the `bopeeps-v3-modern` preview branch. Preserve all card text, prices, durations, buttons, layout, other page imagery, and production-domain settings.

## Approved mapping

- Express Wash And Spray Wax: the supplied spray-bottle artwork, saved as `assets-v3/service-wash.webp`.
- Deluxe Detail Package: the supplied interior-detailing artwork, saved as `assets-v3/service-interior.webp`.
- Jacky Jones Premium Detail: the supplied branded truck artwork, saved as `assets-v3/service-premium.webp`.

## Asset handling

Convert the three supplied 1254-by-1254 PNG files to optimized WebP files without generating, retouching, upscaling, or materially altering their artwork. The existing fixed-height service-card crop remains responsible for responsive presentation.

## Markup and accessibility

Update only the three service image `src`, intrinsic dimensions, and descriptive alternative text. Use simple alternative text that identifies the artwork's service meaning without presenting an illustration as a photograph.

## Verification and delivery

Update the structural contract test to require the new filenames, first confirm that it fails against the old markup, then implement the asset and markup changes. Run the full static suite, inspect the three cards locally at desktop and mobile widths, commit and push only `bopeeps-v3-modern`, and confirm the three new images load on the existing GitHub Pages preview. Do not merge into `main` or change Porkbun or the custom domain.
