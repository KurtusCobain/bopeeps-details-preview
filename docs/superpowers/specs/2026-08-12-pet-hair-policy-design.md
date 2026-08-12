# Pet Hair Pricing Disclosure Design

## Goal

Keep the pet-hair surcharge disclosure visible before booking while moving expandable policy detail off the homepage and onto a dedicated policy page that can grow with future service, pricing, booking, and payment policies.

## Branch Safety

- Implement only on `dev/pet-hair-policy`.
- Do not change `main`, the custom domain, GitHub Pages settings, DNS, or any other existing branch during development.
- Do not change Booksy configuration from this repository. The user has separately added the matching disclaimer to the Booksy service listings.

## Homepage Placement

Immediately below the existing services/Booksy pricing controls, keep a compact card titled **Pricing & Vehicle Condition**.

Copy:

> Service prices reflect standard vehicle conditions. **Excessive pet hair requiring additional removal time** may incur a **$20 pet hair removal fee**. If applied, the charge will be itemized in your final checkout and reflected on your receipt or payment confirmation email.

The card links to `policies.html` with a clear **View policies** or **View pricing policy** action.

Remove the larger lower-page pricing FAQ from the homepage so the main page remains focused and concise.

## Dedicated Policy Page

Create `policies.html` as the permanent policy destination for BoPeeps Details & More.

The page should:

- Match the existing black/red/white visual system.
- Reuse the existing BoPeeps header/logo, contact information, Booksy CTA, footer, and mobile quick-action bar.
- Use a page heading such as **Policies & Service Information**.
- Include a **Pricing & Vehicle Condition** section with the exact approved disclosure copy.
- Explain that the $20 charge applies only when excessive pet hair requires additional removal time; a few stray hairs are not the intended threshold.
- Explain that, when applied, the charge is a separate `$20 Excessive Pet Hair Removal` line item in final checkout and is reflected on the receipt or payment confirmation email.
- Include an easy **Back to Home** link.
- Be structured so additional policies can be added later as separate cards/sections without changing the homepage.

## Visual Design

- Match the existing site typography, radii, red accents, muted text, and dark panels.
- Keep the homepage notice visible but not alarm-like.
- Policy page content should be readable in one column on mobile and may use a two-column card layout on larger screens.
- No modal, checkbox, popup, new JavaScript feature, or new dependency is required.

## Accessibility

- Use semantic headings and an `aside` for the homepage notice.
- Use a normal `main` and section/article hierarchy on `policies.html`.
- Do not rely on color alone to communicate the surcharge.
- All policy and back-navigation links must be keyboard accessible.

## Booksy Alignment

The website and Booksy wording should match exactly on the core disclosure:

> Service prices reflect standard vehicle conditions. **Excessive pet hair requiring additional removal time** may incur a **$20 pet hair removal fee**. If applied, the charge will be itemized in your final checkout and reflected on your receipt or payment confirmation email.

The website does not simulate or modify Booksy checkout. When applicable, staff should use a separate `$20 Excessive Pet Hair Removal` item in the actual booking/checkout workflow.