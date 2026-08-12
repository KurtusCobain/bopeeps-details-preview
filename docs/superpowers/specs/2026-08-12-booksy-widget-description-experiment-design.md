# Booksy Widget Description Expansion Experiment Design

## Goal

Determine whether the Booksy booking modal's service-description rows can be safely accessed and expanded from the BoPeeps website without changing Booksy booking behavior or touching the live `main` branch.

## Safety

- Work only on `dev/booksy-widget-description`.
- Do not modify `main`, GitHub Pages settings, DNS, Booksy account settings, pricing, services, payments, or booking logic.
- Treat Booksy's widget as third-party software. Do not replace, intercept, spoof, or rewrite booking actions.
- If the booking UI is isolated from the host page or no stable supported DOM surface exists, stop the experiment and report Approach B as unsuitable.

## Research Baseline

Booksy officially documents how to embed its website widget and how to configure service descriptions, but does not document a control for the number of service-description lines shown in the embedded service picker. Booksy also states that the actual client-facing booking page is managed within Booksy. Therefore, expanding the descriptions from our site would be an unsupported enhancement and must be treated as experimental.

## Diagnostic Phase

Add a development-only diagnostic that runs after the Booksy widget opens and records only structural information visible to the host page:

1. Whether a Booksy-owned modal/container becomes visible in the host document.
2. Whether one or more iframes are inserted and, if so, their public `src`/origin metadata.
3. Whether service-description text nodes are accessible from the host document.
4. Whether accessible description elements use a CSS line clamp, fixed height, overflow rule, or another truncation mechanism.
5. Whether a stable selector can be identified without relying on obfuscated/minified class names.

The diagnostic must not read client personal information, booking form values, authentication state, or payment information.

## Expansion Test

Only if the diagnostic proves that the service-description elements are directly accessible in the same document and have a stable structural selector:

- Add a development-only CSS override that removes only the description truncation (`line-clamp`, `max-height`, or `overflow`) while leaving service name, price, duration, Book buttons, scheduling, account, and payment UI untouched.
- Prefer a narrowly scoped selector under a stable Booksy container or semantic attribute.
- Do not use brittle selectors based solely on generated class hashes, element order, or visible service text.
- Do not mutate Booksy data or replace Booksy-generated markup.

## Stop Conditions

Approach B is considered unsuitable if any of the following is true:

- Service rows are inside a cross-origin iframe or otherwise inaccessible from the BoPeeps page.
- Booksy uses an inaccessible closed shadow root.
- The only usable selectors are generated/obfuscated classes likely to change without notice.
- Expanding the text requires modifying Booksy JavaScript, intercepting network requests, or cloning/replacing booking markup.
- The override affects booking controls or causes layout/interaction regressions.

## Result Categories

- **B1 — Safe enough to test:** same-document service descriptions, stable selector, CSS-only clamp removal.
- **B2 — Technically possible but brittle:** same-document access exists but selectors/markup are unstable; do not ship.
- **B3 — Not accessible:** cross-origin or otherwise isolated widget content; do not attempt host-page CSS overrides.

## Verification

Before any recommendation to merge:

- Confirm `main` has not changed.
- Confirm the development branch changes only diagnostic/experimental files and narrowly scoped widget code.
- Confirm Booksy service selection, Book buttons, modal close behavior, and navigation remain unchanged.
- Confirm the diagnostic collects no client or payment data.

No merge is part of this experiment unless the user separately approves a verified B1 result.
