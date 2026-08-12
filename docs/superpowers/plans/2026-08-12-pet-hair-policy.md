# Pet Hair Pricing Disclosure Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Keep the compact pet-hair surcharge disclosure on the homepage, move detailed policy content to a new `policies.html` page, and preserve `main` unchanged for review.

**Architecture:** `index.html` retains one compact `Pricing & Vehicle Condition` notice below the services area and links to a dedicated static `policies.html`. The new policy page reuses the existing site visual language and common business links, while static tests verify the homepage link, removal of the former lower-page policy section, and the required policy-page content.

**Tech Stack:** Static HTML5, CSS3, existing `styles-v3.css`, GitHub Pages.

## Global Constraints

- Work only on `dev/pet-hair-policy`.
- Do not modify `main`, Pages settings, DNS, or Booksy configuration.
- Core disclosure wording must match the approved Booksy wording exactly.
- Policy threshold is exactly: excessive pet hair requiring additional removal time.
- Fee is a fixed `$20` when applicable.
- The charge must be described as itemized in final checkout and reflected on the receipt or payment confirmation email.
- No new dependency and no new JavaScript behavior.

---

### Task 1: Update policy regression checks

**Files:**
- Modify: `tests/test_pet_hair_policy.py`

**Interfaces:**
- Consumes: `index.html` and `policies.html`.
- Produces: static assertions for the homepage notice, `policies.html` link, absence of the old lower-page policy block, exact disclosure copy, and policy-page itemization details.

- [ ] **Step 1:** Change the test so it expects `policies.html` to exist and the homepage link to target it.
- [ ] **Step 2:** Add an assertion that `index.html` no longer contains `id="pricing-policy"`.
- [ ] **Step 3:** Add assertions that `policies.html` contains `Pricing & Vehicle Condition`, `$20 Excessive Pet Hair Removal`, the approved threshold, and receipt/payment-confirmation wording.
- [ ] **Step 4:** Run the test before implementation and verify it fails because `policies.html` does not yet exist and the homepage still contains the old lower policy section.

### Task 2: Create the dedicated policy page

**Files:**
- Create: `policies.html`

**Interfaces:**
- Consumes: existing site CSS, logo assets, contact information, Booksy URL, and mobile quick actions.
- Produces: a standalone expandable policy destination.

- [ ] **Step 1:** Create a semantic page titled `Policies & Service Information | BoPeeps Details & More`.
- [ ] **Step 2:** Reuse `styles-v3.css` plus page-scoped CSS for the policy hero/cards.
- [ ] **Step 3:** Add the exact approved disclosure under `Pricing & Vehicle Condition`.
- [ ] **Step 4:** Add concise detail explaining the threshold and separate `$20 Excessive Pet Hair Removal` checkout item.
- [ ] **Step 5:** Add Home, Booksy, phone, email, footer, and mobile quick-action navigation.

### Task 3: Simplify the homepage policy presentation

**Files:**
- Modify: `index.html`

**Interfaces:**
- Consumes: existing `.pricing-notice` card.
- Produces: a homepage notice that links to `policies.html` and no longer duplicates the full policy section.

- [ ] **Step 1:** Change the notice link from `#pricing-policy` to `policies.html` and label it `View policies →`.
- [ ] **Step 2:** Remove the lower `#pricing-policy` section between About and Contact.
- [ ] **Step 3:** Remove homepage-only `.policy-section`, `.policy-grid`, and `.policy-faq` CSS while retaining `.pricing-notice` styling.
- [ ] **Step 4:** Keep all unrelated homepage markup, Booksy links, scrub interactions, assets, contact details, and CNAME unchanged.

### Task 4: Verify branch and preview

**Files:**
- Verify: `index.html`
- Verify: `policies.html`
- Verify: `tests/test_pet_hair_policy.py`

**Interfaces:**
- Consumes: completed development branch.
- Produces: reviewable home and policy pages with no live mutation.

- [ ] **Step 1:** Run `pytest -q tests/test_pet_hair_policy.py` and require zero failures.
- [ ] **Step 2:** Confirm `main...dev/pet-hair-policy` is ahead-only and `main` has not moved.
- [ ] **Step 3:** Confirm GitHub Pages still serves `main`.
- [ ] **Step 4:** Update the existing draft PR description to describe the dedicated policy page.
- [ ] **Step 5:** Provide direct rendered previews for both the full homepage and `policies.html`; do not merge.