# Corrected Storefront Hero and Search Icon Design

## Goal

Replace every website storefront hero image with responsive derivatives of `bopeeps_storefront_correct_phone.png` so the visible storefront sign uses the current phone number, `1-980-598-1864`. Add a recognizable BoPeeps favicon that search engines can display beside the website result.

## Asset treatment

- Create an optimized desktop WebP using the complete supplied image.
- Create an optimized mobile WebP cropped around the storefront sign and Jeep.
- Exclude the baked-in "Book on Booksy" graphic from the mobile crop where practical because the page already provides a real, accessible booking link.
- Preserve the supplied image content; resizing, compression, and responsive cropping are the only permitted changes.

## Integration

- Replace `assets-v3/hero-storefront-desktop.webp` and `assets-v3/hero-storefront-mobile.webp` in place.
- Keep their existing filenames so the homepage picture element, preload, social metadata, structured data, and local SEO pages continue using the corrected storefront without HTML rewrites.
- Preserve the current hero layout, overlay text, Booksy and call links, navigation, trust strip, accessibility behavior, and reduced-motion support.

## Search-result icon

- Create square favicon files from the existing official red-and-white BoPeeps logo, using a tight crop that remains recognizable at small sizes.
- Add standard favicon declarations to every indexable page and the 404 page.
- Keep the favicon on the root domain with a crawlable URL so Google can discover it during a future recrawl.
- Do not use the detailed storefront photo as the favicon because its sign and vehicle would be unreadable at search-result size.
- Treat Google's currently displayed old phone number as a cached search snippet; the corrected website content is already the source Google should pick up after recrawling.

## Verification

- Confirm both WebP files decode and have appropriate desktop and mobile dimensions.
- Confirm the favicon files decode, are square, and are referenced by every public page.
- Run the existing static test suite and JavaScript syntax check.
- Check the homepage at desktop and mobile widths for readable storefront signage, reasonable cropping, and no broken images or layout overflow.
- Publish only the approved storefront and favicon changes to production, then verify the live homepage serves them.
