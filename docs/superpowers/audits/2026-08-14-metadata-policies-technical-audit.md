# Metadata, Policies, and Technical Audit Results

## Scope
This audit covers the current tree of `dev/site-cleanup-phone-audit`. It does not merge or publish the branch.

## Metadata and search snippets
The nine indexable routes retain their existing production canonicals while their titles/descriptions/Open Graph copy are now more clearly separated by page intent:

- Home — branded Hayesville auto-detailing landing page with pricing, real work, service-area, and booking context.
- Services — current packages and vehicle-size pricing.
- Hayesville — physical Clay County shop / Lake Chatuge-area context.
- Murphy — Murphy and Cherokee County drivers using the Hayesville shop.
- Hiawassee — Hiawassee, Towns County, and Lake Chatuge-area service context.
- Young Harris — Young Harris and Towns County service context.
- Blairsville — Blairsville and Union County service context.
- Policies — pricing, vehicle condition, and excessive pet-hair policy only.
- Privacy — static-site request data and third-party Booksy/Maps/Facebook privacy information.

The 404 route remains `noindex,nofollow` and is intentionally not converted into an indexable SEO page.

## Policy page
The Policies page is now explicitly scoped to the policy BoPeeps has actually supplied. It does not invent cancellation, no-show, payment, liability, personal-property, biohazard, or other rules.

The page preserves the approved policy facts:

- listed prices assume standard vehicle conditions
- excessive pet hair requiring additional removal time may incur a $20 pet hair removal fee
- a few stray hairs are not the intended threshold
- if applied, the additional service is itemized in checkout and reflected on the receipt or payment confirmation email

The page now separates the standard-condition baseline, excessive-pet-hair threshold, and checkout/receipt behavior into scan-friendly facts. It also clarifies that Booksy handles appointment availability and the checkout workflow while this website states the BoPeeps policy itself.

## Technical audit changes
### Regression coverage added
The static audit harness now checks:

- unique and complete title/meta/OG/canonical data on all nine indexable pages
- `og:url` matching each canonical
- exactly one H1 per indexable route
- relative internal links and fragment targets
- duplicate IDs
- heading-level progression
- local image/stylesheet/script asset existence
- positive numeric image width/height attributes
- image alt attributes, with a narrow decorative-thumbnail exception
- current phone, email, business name, Booksy URL, Facebook URL, and former-phone protection
- one Hayesville LocalBusiness/AutomotiveBusiness entity and current ReserveAction target
- sitemap/robots/favicons and existing service/pricing/location protections
- `target="_blank"` links retaining `rel="noopener"`
- accessible labels on all navigation landmarks
- hero image preload remaining limited to the storefront/LCP image
- below-the-fold service/gallery/scrub images remaining lazy-loaded

### Accessibility fixes
- Mobile menu screen-reader text now switches between `Open menu` and `Close menu` with the actual expanded state.
- Primary/footer navigation landmarks on the five local pages and the 404 page now have explicit accessible labels.

## Items reviewed and intentionally left unchanged
### CSS
The shared CSS remains compact and functional. A source review did not provide enough evidence to justify removing legacy-looking selectors without a browser/runtime regression run. No speculative CSS cleanup was performed.

### JavaScript
The existing JavaScript remains limited to mobile navigation, Booksy handoff, and the interactive scrub demonstration. Only the proven mobile-menu accessibility issue was changed; there was no broad JavaScript rewrite.

### Sitemap and robots
`sitemap.xml` already contains the intended nine production URLs and excludes 404/development/test/documentation paths. `robots.txt` already allows normal crawling and advertises the production sitemap. Neither file required changes.

### Preload/lazy loading
The homepage already preloads only the storefront hero image and lazy-loads the below-the-fold service/gallery/scrub imagery. Regression coverage was added rather than changing working markup.

### Favicons and manifest
The existing favicon set and declarations are retained. A web-app manifest was not added solely for SEO because this static business website does not need PWA installation metadata.

## Automated execution status
`pytest` and `node --check script-v3.js` have not been executed against a complete branch checkout in this connector session. The runtime cannot resolve `github.com`, and the repository has no existing GitHub Actions workflow to reuse. Source-level verification and branch-diff verification were completed, but automated tests must not be reported as passing until they are actually run against the branch.

## Branch isolation
A fresh `main...dev/site-cleanup-phone-audit` comparison shows the development branch is ahead-only with `behind_by = 0`. The comparison contains no CNAME, DNS, or GitHub Pages configuration changes. `main` remains untouched and nothing from this branch has been published.
