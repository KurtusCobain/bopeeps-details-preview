# Gallery Image Swap Design

## Goal

Replace two images in the existing real-work gallery on `bopeeps-v3-modern` without changing the gallery layout or captions.

## Image Mapping

- Replace the `Exterior care` tile image with `C:\Users\katie\Downloads\Bopeeps\27.jpg`.
  - Optimized asset: `assets-v3/gallery-exterior-care.webp`
  - Alternative text: `White Jeep receiving exterior care at the BoPeeps shop`
- Replace the `Real local work` tile image with `C:\Users\katie\Downloads\Bopeeps\16.jpg`.
  - Optimized asset: `assets-v3/gallery-real-local-work.webp`
  - Alternative text: `Detailed black vehicle interior photographed at the BoPeeps shop`

Both originals are 1536 by 2048 pixels. Convert them to 1200 by 1600 WebP images without generating, retouching, or materially altering their content.

## Preserved Behavior and Scope

- Keep the captions `Exterior care` and `Real local work` unchanged.
- Keep the existing gallery tile dimensions, responsive crops, gradient overlays, and remaining four gallery images unchanged.
- Keep the scrub demonstration, services, contact details, Booksy integration, navigation, and all other site sections unchanged.
- Commit and push only `bopeeps-v3-modern`; do not merge or modify `main`, Porkbun, or the production domain.

## Verification

- Update the static gallery contract test to require the two meaningful asset paths in their existing positions.
- Confirm all local asset paths resolve, both WebP files are 1200 by 1600, the full test suite passes, and JavaScript syntax remains valid.
- Verify both updated tiles load correctly on the deployed GitHub Pages preview with no horizontal overflow.
