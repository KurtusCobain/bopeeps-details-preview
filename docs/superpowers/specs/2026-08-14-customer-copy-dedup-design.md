# Customer Copy De-duplication Design

Date: 2026-08-14
Branch: `dev/customer-copy-audit`

## Goal

Reduce repeated location reassurance across every customer-facing page while keeping the site clear, accurate, and useful for local search.

BoPeeps welcomes customers from any location, but the website does not need to repeat that point in multiple nearby sections. The physical address and directions already establish where customers should go.

## Tone

Professional, friendly, and straightforward.

The site should state facts once, then move on. It should not sound defensive, corrective, or as though it expects customers to misunderstand the business model.

## Core Rule

Keep location information where it helps a customer make a decision or find BoPeeps. Remove location language when it merely repeats something already made clear by the page heading, address, directions button, map, shop-information card, or footer.

Avoid repeated phrases such as:

- `in-shop auto detailing`
- `all detailing is completed at...`
- `customers are welcome from anywhere`
- `customers from anywhere are welcome to book`
- `Hayesville shop` repeated multiple times on the same page
- `your appointment is at BoPeeps in Hayesville` when the address is already directly below or nearby

## Homepage

Keep the `Hayesville Location` trust item because it is useful orientation.

Change the service-area paragraph to one concise statement:

> BoPeeps welcomes drivers from western North Carolina, north Georgia, and beyond. Find us at 1516 US-64 in Hayesville, NC.

Do not add another sentence saying customers from anywhere are welcome.

Keep the map, address, contact section, and Directions action. Those already make the location clear.

The footer should remain concise:

> Professional auto detailing in Hayesville, North Carolina.

No `in-shop` qualifier is needed there.

## Services Page

The hero should focus on services and pricing, not repeatedly explain the location.

Replace the current location banner with a short factual identifier such as:

> BoPeeps Details & More · 1516 US-64, Hayesville, NC

Keep one regional discovery section mentioning western North Carolina and north Georgia, but do not also say `surrounding communities and beyond` or repeat that customers may come from anywhere.

Keep address/directions/contact functionality unchanged.

The footer should use the same concise wording as the homepage rather than `Professional in-shop auto detailing...`.

## Policies Page

Remove the `Customers are welcome from anywhere` statement from the appointment-location banner.

If the location banner remains, keep it purely factual:

> BoPeeps Details & More · 1516 US-64, Hayesville, NC

The policy page should stay focused on pricing and vehicle condition rather than explaining where service happens more than once.

Use the concise footer wording.

## Privacy Page

No additional location explanation is needed beyond standard site navigation/footer information.

Use the concise footer wording and preserve the direct privacy wording already approved.

## Local SEO Pages

Each local page should answer two questions quickly:

1. Is BoPeeps relevant to someone searching from this city/area?
2. Where do I go?

The city-specific H1, title, metadata, and one short local-context paragraph provide the search relevance.

The shop address and Get Directions action provide the destination.

### Local-page location pattern

Do not repeat `Hayesville shop` in the hero, banner, body, nearby-community block, and footer.

Use one concise destination banner near the top:

> BoPeeps Details & More · 1516 US-64, Hayesville, NC

Then let the page focus on services, pricing, vehicle types, policies, and directions.

The local introduction may mention Hayesville once where needed for clarity, for example:

> Looking for professional auto detailing near Murphy? BoPeeps Details & More is located on US-64 in Hayesville, a convenient option for Murphy and Cherokee County drivers.

After that, do not keep re-explaining the physical-location model.

### Nearby communities block

Keep the useful cross-links for search/navigation, but simplify the paragraph to something like:

> Coming from another nearby town? Use the links below for local information, or get directions from your current location.

Remove `BoPeeps welcomes customers from anywhere` from every local page because the regional links and destination-only directions already communicate that customers may travel to the business.

### Regional references

Keep them minimal:

- Hayesville: Clay County / Lake Chatuge only where natural
- Murphy: Cherokee County
- Hiawassee: Towns County / Lake Chatuge
- Young Harris: Towns County
- Blairsville: Union County

Do not add geographic filler.

## Metadata and Structured Data

Customer-facing meta descriptions and social descriptions may mention Hayesville once when it helps establish the destination, but should not repeat `shop` language unnecessarily.

Structured data remains factual and can continue to identify the Hayesville address and service-area cities. It should not be treated as customer-facing prose, but overly promotional wording such as `Professional in-shop auto detailing...` should be normalized to `Professional auto detailing in Hayesville, NC` for consistency.

Do not change:

- canonical URLs
- page URLs
- service names
- service prices
- phone number
- email
- business address
- business hours
- Booksy URL
- Facebook URL
- pet-hair fee/policy substance
- local-page city targeting

## Directions

Keep the destination-only Google Maps directions behavior already implemented. Do not add city-specific origins.

## Testing

Update customer-copy regression tests to prevent reintroduction of repetitive phrases, including:

- `customers from anywhere are welcome to book`
- `customers are welcome from anywhere`
- repeated `Professional in-shop auto detailing` footer copy
- unnecessary `All detailing is completed at` banners on customer pages

Tests should still require:

- accurate Hayesville address
- device-location directions links
- city-specific local-search context
- current services/prices/policies
- no implication of multiple branch locations

## Success Criteria

The finished site should make the following clear without repeating itself:

- BoPeeps is located in Hayesville.
- Customers from surrounding areas can find and visit the business.
- Directions use the customer's current device location when available.
- The local pages remain useful for Google discovery.
- Customer-facing copy sounds natural instead of defensive or repetitive.

No production merge or publish occurs until the revised copy is previewed and approved.