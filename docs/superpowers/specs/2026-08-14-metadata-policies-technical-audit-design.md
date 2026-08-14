# Metadata, Policies, and Technical Audit Design

## Goal
Refine BoPeeps search snippets and page metadata, improve the existing policy page without inventing new business rules, and harden the static site with repository-level technical and accessibility checks.

## Branch Safety
- Work only on `dev/site-cleanup-phone-audit` until the user explicitly approves merge/publish.
- Do not modify `main`, CNAME, DNS, GitHub Pages configuration, Booksy configuration, pricing, service names, or approved business facts.
- The website remains the source of truth for services; Booksy will be updated separately to match it.

## Metadata and Search Snippet Design
Audit all nine indexable routes for:
- `<title>`
- meta description
- canonical URL
- exactly one H1
- Open Graph title
- Open Graph description
- Open Graph URL

Every route must have a clear, unique search intent rather than repeating generic wording.

### Page intent
- Home: branded Hayesville auto-detailing landing page and service-area overview.
- Services: current packages, pricing, vehicle types, and Hayesville booking.
- Hayesville: the physical shop and Clay County location page.
- Murphy: Cherokee County/Murphy drivers traveling to Hayesville.
- Hiawassee: Towns County/Lake Chatuge-area drivers traveling to Hayesville.
- Young Harris: Towns County/Young Harris-area drivers traveling to Hayesville.
- Blairsville: Union County/Blairsville-area drivers traveling to Hayesville.
- Policies: pricing, vehicle-condition, and excessive-pet-hair policy information only.
- Privacy: website/third-party privacy information.

Canonical URLs remain exactly aligned with the sitemap and production domain. Open Graph URLs must match canonicals. Titles/descriptions should be concise and descriptive without keyword stuffing or fabricated claims.

The 404 page remains `noindex,nofollow`; it does not need to become an indexable SEO route.

## Policies Page Design
Do not invent cancellation, no-show, payment, liability, personal-property, biohazard, or other policies that BoPeeps has not supplied.

Keep the approved core policy intact:
- service prices reflect standard vehicle conditions
- excessive pet hair requiring additional removal time may incur a `$20 pet hair removal fee`
- when applied, the charge is itemized in final checkout and reflected on the receipt or payment confirmation email
- a few stray hairs are not the intended threshold

Improve the page by:
- making the actual scope explicit in the title/search copy and H1/lede
- separating the core rule, threshold explanation, and checkout explanation into easy-to-scan sections
- adding a concise note that booking availability and checkout are handled through Booksy, while this page only states the BoPeeps policy currently provided on the website
- preserving Services, Booksy, Home, Privacy, phone, address, and service-area navigation

Do not imply that Booksy creates or controls BoPeeps business policy; Booksy is the booking/checkout platform.

## Technical Audit Design
Use the existing static pytest suite as the primary audit harness. Add checks for concrete defects rather than speculative refactoring.

### Internal links and fragments
- Every relative `.html` target referenced by a public page must exist.
- Relative fragment links such as `index.html#work` must point to an ID present in the target page.
- Pure `#fragment` links must resolve within the same page.
- External HTTP(S), `mailto:`, and `tel:` links are outside static file-existence validation.

### IDs and headings
- IDs must be unique within each public page.
- Each indexable route must have exactly one H1.
- Heading levels must not skip upward through the document structure (for example H1 directly to H3 without an H2).

### Images and assets
- Every local `<img src>` and local `srcset` asset must exist.
- Every `<img>` must include explicit positive numeric `width` and `height` attributes.
- Every `<img>` must include an `alt` attribute; empty alt text is allowed only for intentionally decorative thumbnail images whose containing control already has an accessible text label.
- The hero image remains the only intentionally preloaded image.
- Below-the-fold gallery/service/footer images should remain lazy-loaded where currently appropriate.

### Business data consistency
Across public pages:
- business styling remains `BoPeeps Details & More`
- current phone remains `980-598-1864` / `tel:+19805981864`
- public email remains `hello@bopeepsdetails.com`
- physical address remains `1516 US-64, Hayesville, NC 28904`
- all Booksy booking URLs point to the one current profile
- all Facebook links point to the one current profile
- no retired service/business naming is reintroduced

### Canonical and structured-data consistency
- Indexable canonicals must match the nine sitemap URLs.
- `og:url` must equal the canonical for every indexable page.
- Pages carrying the LocalBusiness/AutomotiveBusiness entity must keep the Hayesville address, current phone, current email, production site URL, one service-area set, and current Booksy ReserveAction target.
- Surrounding-city pages must never create secondary LocalBusiness street addresses.

### Sitemap, robots, favicon, manifest
- Keep the existing nine-URL sitemap unless a real route change occurs.
- Keep `robots.txt` permissive and pointed at the production sitemap.
- Keep the existing favicon set and declarations.
- Do not add a web-app manifest solely for SEO; this static business site does not require PWA installation metadata.

### CSS and JavaScript
- Preserve the existing lightweight JavaScript unless a concrete bug is found.
- Preserve shared CSS unless a selector is proven unused across the current branch.
- Do not remove the scrub interaction's pointer behavior simply to satisfy a generic audit checklist; it already provides button-based reset/reveal alternatives and visible keyboard focus styles elsewhere.

## Verification
- Extend `tests/test_local_seo_expansion.py` with metadata, internal-link, ID, heading, image/asset, business-data, Booksy/Facebook, and structured-data checks.
- Preserve all existing phone, service-name, pricing, location-truthfulness, sitemap, robots, favicon, policy, and homepage-flow tests.
- Review every changed HTML file from the branch after editing.
- Compare `main...dev/site-cleanup-phone-audit` and confirm the branch remains ahead-only and contains no CNAME/DNS/Pages configuration changes.
- Do not claim pytest, JavaScript syntax, or browser rendering has passed unless it is actually executed against the branch.
