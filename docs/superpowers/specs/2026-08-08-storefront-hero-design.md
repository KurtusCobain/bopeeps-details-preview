# Storefront Hero Redesign

## Goal

Redesign only the header-adjacent hero area on `bopeeps-v3-modern` to match the supplied storefront desktop and mobile mockups while preserving real HTML text, functional links, and responsive accessibility.

## Source Assets

- Desktop source: `C:\Users\katie\Downloads\Bopeeps\store front1.png` (1672 by 941)
  - Optimized output: `assets-v3/hero-storefront-desktop.webp`
- Mobile source: `C:\Users\katie\Downloads\Bopeeps\store front 2.png` (941 by 1672)
  - Optimized output: `assets-v3/hero-storefront-mobile.webp`

Convert both raw photos to WebP without generating, retouching, or materially altering their content. Use `storefrontdesktop.png` and `storemobile.png` only as visual references; do not place their flattened text or buttons on the website.

## Responsive Structure

Use one semantic hero with an art-directed `<picture>` element.

- At widths below 768 pixels, load `hero-storefront-mobile.webp` and present the hero as two stacked areas: a storefront photo panel followed by a centered black content panel.
- At widths of 768 pixels and above, load `hero-storefront-desktop.webp` as the full hero background, keep the storefront weighted to the right, and overlay the hero copy on a strong left-to-right black gradient.
- Keep the site header above the hero and the existing trust strip immediately below it.

## Content

Preserve these elements as real HTML:

- Eyebrow: `Auto detailing · Hayesville, NC`
- Headline: `Detailing` / `Done Right.`
- Tagline: `Cleaner. Shinier. Protected.`
- Desktop description: `We proudly detail cars, SUVs, trucks, big rigs, RVs, PWCs, tandem axle trailers, and more. If you've got it, we'll make it showroom ready with professional detailing done to your standards. A clean vehicle is more than just looks, it's pride.`
- Mobile visual summary: `Cars, trucks, SUVs, RVs, and work vehicles.`
- Booksy and phone actions with their current destinations.

At mobile widths, visually hide the full description with the existing screen-reader-only technique and show the shorter summary as a visual duplicate with `aria-hidden="true"`. This preserves the full approved business description for assistive technology without making it compete with the compact phone layout.

## Visual Treatment

- Keep the current black, white, and red design system.
- Desktop headline remains left aligned and prominent, with the storefront sign and building visible on the right.
- Mobile headline and buttons are centered; buttons stack full width in the content panel.
- Use CSS gradients and existing brand styling rather than modifying the supplied photos.
- Preserve clear focus indicators, reduced-motion behavior, and adequate text contrast.

## Scope

- Modify the hero markup and hero-specific CSS only, plus add the two optimized photo assets and their tests.
- Do not change the site header, trust-strip content, services, gallery, scrub demonstration, contact section, Booksy integration, or sticky mobile actions.
- Work only on `bopeeps-v3-modern`; do not merge or modify `main`, Porkbun, or the production domain.

## Verification

- Add structural tests for the responsive picture sources, image alternatives, full desktop copy, mobile summary, and preserved booking/phone destinations.
- Add style-contract checks for the 768-pixel art-direction boundary, mobile stacked hero, desktop overlay hero, and no flattened mockup asset references.
- Run the full static and JavaScript suites.
- Verify the deployed preview visually at desktop and 390-pixel mobile widths with no broken images, console errors, clipped controls, or horizontal overflow.
