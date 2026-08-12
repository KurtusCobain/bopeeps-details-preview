# Booksy Widget Description Expansion Experiment — Result

## Result

**Do not ship Approach B.**

Deployment classification: **B3 in practice / unsupported host-page surface**.

The BoPeeps website can safely control the Booksy launch button and surrounding site content, but the actual client-facing booking interface and service-selection page are managed by Booksy. Booksy's current documentation does not expose a supported setting, API, or website-side CSS hook for changing the number of service-description lines shown inside that booking interface.

## What Was Tested

A standalone development diagnostic was added on `dev/booksy-widget-description` rather than modifying the production homepage. It uses the same BoPeeps Booksy embed identity (`id=1808686`, `country=us`, `lang=en`) and inspects only structural DOM facts such as Booksy containers, iframe origins, cross-origin accessibility, and description-like clipping styles.

The diagnostic is intentionally read-only. It does not read form values, client data, appointment selections, account state, or payment information, and it does not intercept Booksy network requests or replace Booksy booking controls.

## Evidence

Booksy's current website-widget documentation instructs businesses to copy the unique Booksy widget code into their website. Booksy separately states in its booking-system guidance that the actual client-facing booking page where customers choose services and times is managed within Booksy. Booksy documents service descriptions as content configured in Booksy and displayed on the Booksy profile/service listing.

Because the internal booking surface is Booksy-managed rather than a documented host-page component, modifying its description clamp from `bopeepsdetails.com` would rely on unsupported internal implementation details. Even if a browser version temporarily exposed a workable selector, that would be brittle and could break whenever Booksy changes its markup.

## Runtime Limitation

The development diagnostic page is committed and ready for a normal browser confirmation, but the execution environment used for this review cannot establish outbound browser/network access to Booksy. Therefore no claim is made that a live DOM capture was performed from this environment.

This limitation does not change the deployment recommendation: there is no supported Booksy mechanism for host-page CSS to control internal description truncation, so Approach B should not be merged into production.

## Recommendation

Use one of these supported paths instead:

1. **Native Booksy content:** keep the detailed service descriptions in Booksy; use Message to Client, Questions to Client, Policies, and service configuration for information customers need during booking.
2. **BoPeeps service chooser:** keep the full, visually rich service descriptions on `bopeepsdetails.com`, then hand the customer into Booksy for scheduling/checkout.

For BoPeeps, the recommended next website experiment is the second option: preserve Booksy as the booking engine while making the BoPeeps website the detailed service-selection layer.

## Branch Safety

- No change was made to `main`.
- No change was made to the live homepage.
- No GitHub Pages, DNS, Booksy account, pricing, payment, or booking settings were changed.
- The diagnostic and result remain isolated on `dev/booksy-widget-description`.
