# BoPeeps Customer-Facing Copy Audit Design

Date: 2026-08-14
Branch: `dev/customer-copy-audit`

## Goal

Rewrite customer-facing copy across the BoPeeps public website so it sounds professional, friendly, straightforward, and natural to a detailing customer rather than defensive, SEO-driven, developer-facing, or audit-oriented.

The local landing pages remain part of the search strategy so customers searching for detailing around Hayesville, Murphy, Hiawassee, Young Harris, and Blairsville can discover BoPeeps. Those towns are discovery targets, not service restrictions. BoPeeps welcomes customers from anywhere; all detailing is completed at the Hayesville shop.

## Voice

Use a professional but friendly and straightforward tone.

Copy should:
- sound like a local business speaking directly to a customer;
- be concise and confident;
- explain useful customer information without defending the site's architecture;
- keep regional references simple and minimal;
- favor benefits, services, convenience, and booking over explanations about SEO or web implementation.

Avoid customer-facing phrases such as:
- real shop / one real shop / single real shop;
- real local work / genuine photos on this site;
- approved service areas;
- one booking flow;
- hard-coded mileage, fixed drive-time estimates, or other implementation language;
- language that sounds like BoPeeps must prove the shop or photos are authentic;
- repeated statements that every appointment happens at the same Hayesville shop when one clear statement is enough.

## Facts that must not change

- Business name: BoPeeps Details & More.
- Shop address: 1516 US-64, Hayesville, NC 28904.
- Phone: 980-598-1864 / `tel:+19805981864`.
- Email: hello@bopeepsdetails.com.
- Hours: Monday-Saturday 7:00 AM-5:00 PM; Sunday closed.
- Service names and published prices remain unchanged.
- Excessive pet-hair policy remains unchanged in substance: a $20 fee may apply when excessive pet hair requires additional removal time.
- Booksy remains the booking destination.
- The physical detailing location remains Hayesville; the site must not imply branch locations or mobile detailing.
- Existing page URLs, canonicals, structured-data business facts, and local-page architecture remain intact unless a copy-only metadata wording change is explicitly listed below.

## Navigation and directions behavior

All customer-facing location-page directions calls to action should use a destination-only Google Maps directions URL for the BoPeeps shop, with no hard-coded origin city. This allows Maps to use the customer's current device location when available.

Button/link label: `Get Directions`.

Destination: `1516 US-64, Hayesville, NC 28904`.

Remove wording such as `Directions from Murphy`, `Directions from Hiawassee`, and explanations about live routing versus hard-coded mileage or drive times.

## Homepage changes

### Trust strip

Replace defensive/authenticity-focused wording.

- `Real Hayesville shop` / `One physical location on US-64`
  -> `Hayesville Location` / `Conveniently located on US-64`

- Keep `Clear package pricing`, with customer-friendly supporting text such as `Vehicle-size pricing shown upfront`.

- Keep `Book online`, with concise Booksy supporting text.

- `Real local work` / `Genuine BoPeeps photos on this site`
  -> customer-benefit wording such as `Quality Detailing` / `Careful interior & exterior service`.

### Services introduction

Replace `Current BoPeeps services` and any audit-like phrasing with natural customer language, while preserving the three service names and all prices.

### Gallery

Remove repeated authenticity defense:
- replace `Real BoPeeps work` with a natural heading such as `Recent BoPeeps Work`;
- remove sentences that repeatedly say the vehicles/photos are real;
- replace the `Real local work` image caption with a descriptive service/result caption;
- retain useful descriptive alt text and accessibility labels.

The interactive demo remains clearly identified as a simulated grime effect so customers are not misled about the interaction.

### Why BoPeeps

Keep the three-card structure, but polish phrases such as `one straightforward Hayesville shop` and `Straightforward in-shop service` where repetition makes the page sound defensive.

### Service area section

Reframe from a closed service-area concept to an open invitation.

Core message:
- BoPeeps welcomes customers from western North Carolina, north Georgia, and beyond;
- anyone can book regardless of where they live;
- all detailing is completed at the Hayesville shop.

Keep links to the five local landing pages for discovery and navigation.

## Services page changes

Keep all package names, descriptions, prices, specialty-vehicle guidance, and policy substance.

Rewrite awkward phrases including:
- `Compare the current BoPeeps detailing packages`;
- `One shop, one booking flow`;
- `approved surrounding service areas`;
- any language that sounds like an internal website architecture explanation.

Reframe the location/service-area section to say customers are welcome from nearby communities and beyond rather than implying an approved or limited set of towns.

## Policies page changes

Preserve the exact business-policy meaning.

Simplify labels and explanatory text that currently sound like audit notes, including:
- `Current BoPeeps policy`;
- `Standard condition baseline`;
- `Excessive pet hair threshold`;
- `This page states only the ... policy currently provided on this website`.

Use plain customer wording such as `Standard pricing`, `When the pet-hair fee applies`, and `At checkout` while retaining the $20 policy and receipt/checkout explanation.

Do not invent cancellation, deposit, refund, payment, damage, late-arrival, or other policies.

## Privacy page changes

Keep the privacy page factually conservative.

Rewrite awkward or evasive phrasing such as `does not claim to run a separate advertising tracker` into direct language describing what the current site does and does not use.

Keep the distinction between the static BoPeeps site and third-party services such as Booksy, Google Maps, and Facebook.

Do not make stronger privacy promises than the implementation supports.

## Local landing page changes

Pages:
- `auto-detailing-hayesville-nc.html`
- `auto-detailing-murphy-nc.html`
- `auto-detailing-hiawassee-ga.html`
- `auto-detailing-young-harris-ga.html`
- `auto-detailing-blairsville-ga.html`

### Purpose

Each page should help a customer who searched for detailing in or around that community discover BoPeeps, understand that the shop is in Hayesville, compare services, and get directions or book.

The page must not imply that BoPeeps only accepts customers from the named towns.

### Structure

Each page should contain:
1. A locally relevant H1 and concise introduction.
2. One clear statement that service is performed at the Hayesville shop.
3. A short, useful paragraph for customers from the named area.
4. Current service/pricing summary.
5. Shop information.
6. Before-appointment guidance.
7. Links to other nearby local pages.
8. `Book on Booksy`, `Get Directions`, and contact actions.

### Regional references

Keep them simple and minimal.

Acceptable examples where natural:
- Murphy / Cherokee County;
- Hiawassee / Lake Chatuge / Towns County;
- Young Harris / Towns County;
- Blairsville / Union County;
- Hayesville / Clay County / Lake Chatuge area.

Do not include encyclopedia-style geographic filler solely to make a page look unique.

### Remove

Remove phrases such as:
- `This is the BoPeeps physical shop`;
- `One real shop across the state line`;
- `one real shop address`;
- `single BoPeeps shop` when repeated unnecessarily;
- explanations about fixed mileage, hard-coded drive times, or why live directions are used;
- wording that describes the page itself as a local SEO or service-information page.

### Direction links

All five local pages use destination-only directions and the label `Get Directions` rather than a city-specific origin.

## 404 page

No substantive rewrite is required unless the final audit finds a minor consistency issue. Current tone is already customer-friendly.

## Metadata

Audit visible and share-facing metadata for natural wording:
- page `<title>`;
- meta description;
- Open Graph title/description;
- Twitter title/description.

Do not weaken local search intent. Local page titles can continue to use forms such as `Auto Detailing for Murphy, NC | BoPeeps Details & More`.

Remove words such as `real` or implementation-oriented wording from metadata where present.

## Accessibility copy

Preserve useful accessibility text and alt text. Do not remove factual image descriptions merely because visible copy is being simplified.

Interactive-demo accessibility text must continue to disclose that the grime layer is simulated.

## Testing and regression protection

Before implementation, add or update regression tests so the rewritten public pages:
- no longer contain the identified defensive/internal phrases;
- retain all three official service names;
- retain published service prices;
- retain the current phone, address, hours, email, Booksy URL, and policy amount;
- keep all local page canonicals and H1/local intent;
- use destination-only directions rather than hard-coded local-page origins;
- continue to pass existing public-build, metadata, structured-data, accessibility, phone-audit, and layout regression tests.

Run the full pytest suite and `node --check script-v3.js` before proposing a PR.

## Release process

1. Make all work on `dev/customer-copy-audit` only.
2. Add regression tests first where practical.
3. Rewrite customer-facing text page by page.
4. Run full local/CI verification.
5. Review the complete diff specifically for accidental changes to business facts, prices, policy substance, URLs, schema, and local SEO intent.
6. Provide a preview/review point before production.
7. Create a PR to protected `main` only after user approval.
8. Merge only after required CI succeeds.
9. Monitor the Pages deployment and retain the existing emergency rollback capability.
