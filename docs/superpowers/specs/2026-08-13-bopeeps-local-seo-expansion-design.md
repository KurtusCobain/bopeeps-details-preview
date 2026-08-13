# BoPeeps Local SEO Expansion Design

## Goal

Expand BoPeeps Details & More from a strong single-page local business site into a technically sound, crawlable local-search site that can rank for in-shop auto detailing searches in Hayesville, Murphy, Hiawassee, Young Harris, and Blairsville while preserving the current design, Booksy booking flow, gallery, interactive scrub demo, contact information, and policies.

## Branch Safety

- Implement only on `dev/local-seo-expansion` until the user explicitly approves a merge.
- Do not modify `main`, GitHub Pages settings, DNS, Porkbun email records, Booksy configuration, service prices, or payment settings during development.
- Preview and test every new route before any live merge.
- Keep the existing live homepage behavior intact unless a change is specifically required for SEO, navigation, accessibility, or metadata.

## Business Model and Location Truthfulness

BoPeeps Details & More operates from one physical shop:

**1516 US-64, Hayesville, NC 28904**

The business does **not currently provide mobile detailing**.

All local landing pages must make the service model clear: customers from surrounding communities bring their vehicles to the Hayesville shop. The site must never imply that BoPeeps has a physical storefront, staffed location, mobile-detailing unit, or guaranteed on-site service in Murphy, Hiawassee, Young Harris, or Blairsville.

The business phone remains **706-897-6177**, public email remains **hello@bopeepsdetails.com**, and appointments continue through the existing Booksy profile.

## Target Search Areas

Primary physical-location market:

- Hayesville, North Carolina

Approved surrounding service areas:

- Murphy, North Carolina
- Hiawassee, Georgia
- Young Harris, Georgia
- Blairsville, Georgia

These are service-area landing pages, not location pages for separate branches.

## Route Architecture

The optimized site should expose the following customer-facing routes:

1. `/` — primary BoPeeps homepage and Hayesville business landing page
2. `/services.html` — complete detailing service overview and booking handoff
3. `/auto-detailing-hayesville-nc.html` — dedicated Hayesville local-search landing page
4. `/auto-detailing-murphy-nc.html` — service-area page for Murphy customers traveling to Hayesville
5. `/auto-detailing-hiawassee-ga.html` — service-area page for Hiawassee customers traveling to Hayesville
6. `/auto-detailing-young-harris-ga.html` — service-area page for Young Harris customers traveling to Hayesville
7. `/auto-detailing-blairsville-ga.html` — service-area page for Blairsville customers traveling to Hayesville
8. `/policies.html` — existing policies and service information
9. `/privacy.html` — privacy and third-party service disclosure
10. `/404.html` — branded not-found page with useful navigation
11. `/robots.txt` — crawler directives and sitemap reference
12. `/sitemap.xml` — canonical public URL inventory

The sitemap should include indexable HTML routes only. It should not include `404.html`, development files, test files, diagnostics, or repository documentation.

## Homepage SEO Improvements

Preserve the current visual homepage and interactive behavior while adding or refining:

- Canonical URL: `https://bopeepsdetails.com/`
- Search-focused title and meta description without keyword stuffing
- Open Graph URL, title, description, image, and site-name metadata
- Twitter-compatible social card metadata where useful
- Crawlable links to Services, Policies, Privacy, and local service-area pages
- A concise service-area section that names the approved surrounding communities and states that service is performed at the Hayesville shop
- Consistent NAP information: business name, address, phone, email, and hours
- Stronger structured data tied to the one real Hayesville location

The hero, storefront imagery, service cards, trust strip, gallery, scrub interaction, About section, Contact section, mobile quick actions, and Booksy integration should remain visually and functionally recognizable.

## Services Page

`services.html` should provide a richer, crawlable explanation of the current Booksy services without replacing Booksy as the booking system.

It should include the verified current services:

- Express Wash And Spray Wax — from $60+ — approximately 1 hour
- Deluxe Detail Package — from $85+ — approximately 2 hours
- Jacky Jones Premium Detail — from $150+ — approximately 4 hours

The page may expand service descriptions and clarify vehicle types served, but it must not invent unverified inclusions or alter pricing.

Every service should have a clear Booksy booking CTA. The existing Pricing & Vehicle Condition disclosure and pet-hair fee policy must remain easy to reach.

## Local Landing Page Template

Each city page should be genuinely useful and locally specific rather than a copied doorway page with only the city name changed.

Every local page should contain:

- A unique `<title>`, meta description, canonical URL, and H1
- A clear statement that detailing is performed at the Hayesville shop
- The real Hayesville address and phone number
- A short city-specific introduction explaining that BoPeeps serves drivers from that community
- Relevant vehicle/service context without inventing unsupported local claims
- A concise explanation of the trip-to-shop model
- Links to Services, Booksy, Policies, Contact/Home, and other useful site routes
- LocalBusiness/AutomotiveBusiness structured data that still identifies the single Hayesville physical location
- Optional `areaServed` references for approved communities, while keeping the business `address` fixed to Hayesville

Pages must not fabricate testimonials, awards, distances, drive times, landmarks, partnerships, customer counts, or neighborhood facts unless independently verified before publication.

## Structured Data

Use valid JSON-LD built around one real business entity.

The primary entity should remain `AutomotiveBusiness` / `LocalBusiness` and include, where appropriate and verified:

- `name`: BoPeeps Details & More
- canonical site URL
- phone
- public email
- Hayesville postal address
- opening hours
- Facebook profile in `sameAs`
- service-area information for Hayesville, Murphy, Hiawassee, Young Harris, and Blairsville
- representative business image/logo
- Booksy booking URL as a booking/action destination where semantically appropriate

Do not create separate LocalBusiness entities or fake addresses for surrounding cities.

## Privacy Page

Add a practical privacy page describing the site's current behavior, including:

- Basic server/browser request data that may be processed by the hosting platform
- Third-party links and embeds, including Booksy and Google Maps/directions where applicable
- Facebook/external links
- No claim that BoPeeps controls third-party privacy practices
- Contact email for privacy questions

Do not claim collection, analytics, advertising cookies, mailing lists, payment storage, or tracking technologies that the site does not actually use.

## Technical SEO

Add and validate:

- `robots.txt` at the site root
- `sitemap.xml` at the site root
- canonical tags on all indexable HTML routes
- unique titles and descriptions
- one clear H1 per page
- correct internal links with no development-branch URLs
- consistent absolute canonical domain `https://bopeepsdetails.com`
- appropriate `noindex` behavior only where needed; customer SEO pages should remain indexable
- descriptive image alt text where images carry content
- semantic headings and keyboard-accessible navigation
- no broken asset, stylesheet, script, Booksy, phone, email, or internal links

## robots.txt

The intended production crawler file should allow normal public crawling and advertise the sitemap, for example:

```text
User-agent: *
Allow: /

Sitemap: https://bopeepsdetails.com/sitemap.xml
```

No development-only or diagnostic route should be intentionally exposed as a production SEO page.

## Sitemap

`sitemap.xml` should use fully qualified HTTPS canonical URLs and include the homepage, Services, five approved local landing pages, Policies, and Privacy.

That produces **9 indexable sitemap URLs** for the initial SEO release:

1. Home
2. Services
3. Hayesville
4. Murphy
5. Hiawassee
6. Young Harris
7. Blairsville
8. Policies
9. Privacy

The branded 404 route is tested but not submitted for indexing.

## Internal Linking

Use normal HTML anchor links so crawlers and visitors can move among pages without relying on JavaScript.

The site should expose a coherent hierarchy:

- Homepage → Services
- Homepage → local service-area pages
- Homepage → Policies / Privacy
- Services → local pages / Booksy / Policies
- Local pages → Services / Booksy / Home / Policies
- Footer → core business, policy, privacy, and service-area routes

Avoid overwhelming the main navigation. Local links can live in a compact service-area/footer section rather than turning the header into a large city menu.

## Social and Trust Signals

Preserve and strengthen the existing Facebook connection. Ensure the public Facebook profile is linked from relevant site areas and referenced in structured data.

Keep Booksy as the authoritative live booking destination.

The site may display trust-oriented statements that are already supportable from current business information, but must not invent review ratings, review counts, certifications, guarantees, years in business, awards, or affiliations.

## Search Engine Launch Workflow

After the user approves the development build and it is merged to production:

1. Verify every production route returns the intended HTTP status.
2. Verify `robots.txt` and `sitemap.xml` are publicly reachable.
3. Verify SSL remains active on the custom domain.
4. Verify Google Search Console ownership for `bopeepsdetails.com`; prefer durable DNS verification if available.
5. Submit `https://bopeepsdetails.com/sitemap.xml` to Google Search Console.
6. Request indexing for the homepage, Services page, and primary Hayesville landing page first; selectively request the remaining local pages afterward if useful.
7. Import the verified Google property into Bing Webmaster Tools when possible, or verify Bing separately if import is unavailable.
8. Submit the same sitemap to Bing.
9. Consider IndexNow only after the static SEO release is stable; it is not required for the first release.

Search Console and Bing account actions are post-deployment checkpoints and must not block development of the static site itself.

## Google Business Profile Alignment

Website SEO should align with the real Google Business Profile rather than attempting to simulate multiple locations.

Post-development checklist:

- Business name matches the real customer-facing brand
- Address is the Hayesville shop only
- Phone number matches the website
- Hours match the website
- Website URL points to `https://bopeepsdetails.com/`
- Appropriate detailing/business categories are used in the profile
- Service areas may include approved surrounding communities if supported by the profile configuration
- Photos and updates should use genuine BoPeeps work

No Google Business Profile changes are made from the website repository itself.

## Testing and Verification

Before asking the user to merge, the development branch should have automated/static checks covering at least:

- Required route files exist
- Each indexable route has a unique title, meta description, canonical URL, and H1
- Canonical URLs use `https://bopeepsdetails.com`
- All five approved service areas are represented
- Every local page states that service is performed at the Hayesville shop or otherwise avoids implying a local branch/mobile service
- No local page contains a fake secondary street address
- Business phone/address/email remain correct
- Sitemap includes exactly the intended indexable routes
- Sitemap excludes 404 and development files
- robots.txt references the production sitemap
- Core internal links resolve to existing files/routes
- Existing Booksy URL remains unchanged
- Existing policy wording remains available
- JavaScript syntax checks pass
- Existing site tests continue to pass

For the final pre-merge review, provide direct rendered previews for the homepage, Services page, every local landing page, Privacy, Policies, and 404.

## Non-Goals for This Release

- No mobile detailing launch
- No fake city storefronts or addresses
- No separate domains or subdomains for service areas
- No blog/CMS
- No paid-search campaign
- No automated review solicitation system
- No Booksy widget modification
- No service-price changes
- No analytics/advertising platform unless separately approved
- No DNS or email-routing changes during development

## Success Criteria

The development build is successful when:

- BoPeeps has a clear crawlable page architecture covering the five approved search areas.
- Every page accurately represents one Hayesville shop serving surrounding customers.
- The existing customer experience and Booksy flow remain intact.
- Technical SEO essentials are present and testable.
- The branch can be previewed and reviewed without affecting the live site.
- The user can approve a single controlled merge, after which Google and Bing submission can be completed as separate launch checkpoints.
