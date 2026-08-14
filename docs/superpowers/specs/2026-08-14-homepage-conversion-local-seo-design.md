# Homepage Conversion and Local SEO Refresh Design

## Goal
Improve the BoPeeps homepage conversion flow and make the five existing local SEO pages genuinely distinct without changing the approved website services, pricing, booking flow, physical-location truth, or visual brand.

## Branch Safety
- Work only on `dev/site-cleanup-phone-audit` until the user explicitly approves merge/publish.
- Do not modify `main`, CNAME, DNS, GitHub Pages configuration, Booksy configuration, pricing, or service names.
- The website is the source of truth for services; Booksy will be updated separately to match it.

## Homepage Conversion Design
Preserve the existing hero, service cards, real photography, interactive scrub feature, service-area section, contact information, sticky mobile actions, and overall black/red/white visual system.

The homepage order becomes:

1. Hero
2. Compact factual trust/proof strip
3. Services and pricing
4. Real BoPeeps work gallery
5. Interactive cleaning demonstration
6. Compact Why BoPeeps section
7. Service area
8. Contact/location

### Trust/proof consolidation
Replace overlapping benefit language with factual, supportable proof points such as:
- Real Hayesville shop
- Clear package pricing
- Online booking through Booksy
- Real local work shown on the site

Do not add review ratings, review counts, testimonials, awards, guarantees, certifications, or other unsupported social-proof claims.

### Real work before interactive demo
Within the existing work section, present the real-work gallery before the scrub interaction. Keep the scrub interaction fully functional and visually recognizable.

### Why BoPeeps compression
Keep a distinct Why BoPeeps section after the interactive demo, but reduce it from repetitive benefit cards to a shorter statement and a small set of differentiators that do not duplicate the trust strip. The section should focus on vehicle variety, careful finish work, and straightforward in-shop service.

## Local SEO Page Design
Keep all five routes and the one-shop architecture:
- Hayesville, NC
- Murphy, NC
- Hiawassee, GA
- Young Harris, GA
- Blairsville, GA

Every page continues to identify `1516 US-64, Hayesville, NC 28904` as the only shop and must not imply a second storefront or mobile-detailing operation.

### Shared structure
Each city page should still include:
- unique title, description, canonical and H1
- city-specific intro
- unique regional context
- the exact website services/prices
- shop address, phone and hours
- a city-specific directions link to the Hayesville shop
- policy link
- links to the other approved service-area pages
- Booksy booking CTA

### Hayesville
Position Hayesville as the physical home location in Clay County. Use locally relevant context around the town, Lake Chatuge and the NC-64 corridor without overloading the page with tourism copy.

### Murphy
Write specifically for Murphy/Cherokee County drivers traveling to Hayesville. Mention Murphy's western North Carolina/Appalachian context and provide a directions link from Murphy to the Hayesville shop. Do not invent mileage or drive time.

### Hiawassee
Use verified Towns County/Lake Chatuge context. This page may naturally emphasize cars, SUVs, trucks, RVs and PWCs because the regional lake/outdoor context makes those vehicle types relevant, while avoiding claims that those exact customers already use BoPeeps.

### Young Harris
Use verified Towns County and Young Harris context, including Young Harris College where useful. Keep the copy focused on residents, students/families and nearby drivers without making unverified customer-demographic claims.

### Blairsville
Use verified Union County/north Georgia mountain context and provide directions to the Hayesville shop. Relevant vehicle language may include daily drivers, trucks, SUVs and recreation-oriented vehicles, but must not claim specific Blairsville customers or partnerships.

## Directions
Use normal Google Maps directions URLs with a city-specific origin and the BoPeeps Hayesville address as the destination. This gives customers accurate live routing without hard-coding mileage, travel times, or route instructions that may change.

## SEO Quality Rules
- No doorway-page keyword stuffing.
- No invented distances, drive times, landmarks-as-customer-proof, reviews, partnerships, or branch locations.
- Keep service names and prices identical to the website source of truth.
- Keep LocalBusiness schema tied to the Hayesville address only.
- Make the five pages materially different in wording and regional context, not merely city-name substitutions.

## Verification
- Add regression assertions for homepage section ordering and preservation of service names.
- Add assertions that each local page contains a unique city-specific context marker and a directions URL.
- Preserve existing phone-number, canonical, one-location, sitemap, policy and service-name regression checks.
- Compare the final branch to `main` and confirm no CNAME/DNS/Pages/external-service changes.
- Do not claim automated tests pass unless the test suite is actually executed against the branch.
