# Pet Hair Pricing Disclosure Design

## Goal

Add clear pre-booking disclosure that excessive pet hair requiring additional removal time may incur a fixed $20 charge, without changing the live `main` branch until the development version is reviewed.

## Branch Safety

- Implement only on `dev/pet-hair-policy`, created from the current `main` branch.
- Do not change `main`, the custom domain, GitHub Pages settings, Booksy configuration, or any other existing branch during development.

## Website Placement

### Service-area notice

Immediately below the existing services/Booksy pricing controls, add a compact card titled **Pricing & Vehicle Condition**.

Copy:

> Service prices reflect standard vehicle conditions. Excessive pet hair requiring additional removal time may incur a $20 pet hair removal fee. If applied, the charge will be itemized in your final checkout and reflected on your receipt or payment confirmation email.

Include a small in-page link to the detailed pricing policy below.

### Lower-page policy / FAQ

Between the existing About and Contact sections, add a short section titled **Pricing & Vehicle Condition** with two questions:

**When does the $20 pet hair fee apply?**

Only when excessive pet hair requires additional removal time beyond normal detailing. A few stray hairs are not the intended threshold.

**How is the additional charge handled?**

If the condition requires the additional service, a separate $20 Excessive Pet Hair Removal charge is added to the final appointment amount and reflected on the final receipt or payment confirmation email.

## Visual Design

- Match the existing black/red/white BoPeeps theme.
- Notice should be visible but not alarm-like or visually dominant.
- Use existing typography, border radii, red accent, and muted text colors.
- Mobile-first: notice and FAQ stack naturally with no horizontal overflow.
- No modal, checkbox, popup, or JavaScript required.

## Accessibility

- Use semantic headings and an `aside` for the service-area notice.
- Use a normal section with question/answer headings for the lower policy content.
- Do not rely on color alone to communicate the fee.
- The in-page policy link must be keyboard accessible.

## Booksy Follow-up

The website disclosure is independent of Booksy configuration. After the website version is approved, configure Booksy separately so the same policy appears in service/policy messaging and, when applicable, the final checkout uses a separate `$20 Excessive Pet Hair Removal` line item. No Booksy setting is changed as part of this development branch.