# Hero Description Update Design

## Goal

Replace the current hero description on `bopeeps-v3-modern` with the approved business description.

## Copy

Use this exact normal-weight paragraph:

> We proudly detail cars, SUVs, trucks, big rigs, RVs, PWCs, tandem axle trailers, and more. If you've got it, we'll make it showroom ready with professional detailing done to your standards. A clean vehicle is more than just looks, it's pride.

## Presentation and Scope

- Keep the existing `.hero-text` element and normal font weight.
- Allow the paragraph to wrap naturally within the existing responsive hero layout.
- Keep the hero headline, tagline, image, buttons, spacing, and all other website content unchanged.
- Update only `bopeeps-v3-modern`; do not merge or modify `main`, Porkbun, or the production domain.

## Verification

- Add a static contract assertion for the approved description and removal of the previous sentence.
- Run the full static and JavaScript checks.
- Confirm the updated description renders on the GitHub Pages preview without horizontal overflow.
