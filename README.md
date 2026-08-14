# BoPeeps Details & More

This repository contains the mobile-first static detailing website for BoPeeps Details & More in Hayesville, North Carolina.

- Phone: 980-598-1864
- Email: hello@bopeepsdetails.com
- Booking: [Booksy](https://booksy.com/en-us/1808686_bopeeps-detail-more_other_26564_hayesville)
- Hosting: GitHub Pages
- Domain: bopeepsdetails.com after DNS cutover

## Production files

- `index.html` contains the page structure, business content, contact links, Booksy widget, gallery, and scrub controls.
- `styles-v3.css` contains the responsive black-and-red presentation and desktop/mobile hero art direction.
- `script-v3.js` contains the mobile navigation, Booksy fallback handling, and interactive scrub behavior.
- `.nojekyll` keeps the static file tree compatible with GitHub Pages.
- `assets/logo-modern.jpg` is the header logo.
- `assets-v3/` contains the optimized hero, service, scrub, and gallery images referenced by the production page.

## Image maintenance

Keep replacement images optimized for the web and preserve the existing filenames unless the HTML is updated at the same time.

- Hero images: replace `hero-storefront-desktop.webp` and `hero-storefront-mobile.webp` together so desktop and mobile retain their intended crops.
- Service images: replace the three `service-*.webp` files used by the service cards.
- Scrub images: update each choice's image source and alternative text in `index.html`; the shared controller in `script-v3.js` handles switching and resetting.
- Gallery images: replace the corresponding `gallery-*.webp` file or update its path and descriptive alternative text in `index.html`.

Run the production reference checks after every image change so no local link points to a missing asset.

## Production workflow

Keep production changes on a review branch, verify the complete static site, and promote them to `main` without force-pushing. GitHub Pages serves the repository root.

Experimental sponge cursors, bubbles, sounds, and other scrub effects belong on `experiment/scrub-effects`, not on production. The production scrub interaction should remain accessible to pointer and keyboard users.
