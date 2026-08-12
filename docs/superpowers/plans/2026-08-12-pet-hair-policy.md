# Pet Hair Pricing Disclosure Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a visible, mobile-friendly $20 excessive-pet-hair pricing disclosure in two places on the BoPeeps website while keeping the live `main` branch untouched.

**Architecture:** Make one semantic HTML update to `index.html` and add matching presentation rules without JavaScript. Development stays isolated on `dev/pet-hair-policy`; Booksy configuration is documented as a separate follow-up rather than being simulated in website code.

**Tech Stack:** Static HTML5, CSS3, GitHub Pages.

## Global Constraints

- Work only on `dev/pet-hair-policy`.
- Do not modify `main`, Pages settings, DNS, or Booksy configuration.
- Policy threshold is exactly: excessive pet hair requiring additional removal time.
- Fee is a fixed `$20` when applicable.
- The charge must be described as separately itemized in final checkout and reflected on the receipt or payment confirmation email.
- No new JavaScript or dependency.

---

### Task 1: Add policy regression checks

**Files:**
- Create: `tests/test_pet_hair_policy.py`

**Interfaces:**
- Consumes: production `index.html` markup.
- Produces: static assertions for the pricing notice, policy section, threshold language, `$20` amount, itemization wording, and in-page policy link.

- [ ] **Step 1:** Create tests that fail because the development branch does not yet contain `pricing-notice` or `pricing-policy`.
- [ ] **Step 2:** Confirm the current HTML lacks those required markers.

### Task 2: Add the service-area disclosure and lower policy section

**Files:**
- Modify: `index.html`

**Interfaces:**
- Consumes: existing `services-section`, `about-section`, and `contact-section` structure.
- Produces: `#pricing-policy`, `.pricing-notice`, and `.policy-faq` markup.

- [ ] **Step 1:** Add the compact `Pricing & Vehicle Condition` notice below the service controls.
- [ ] **Step 2:** Add a keyboard-accessible `View pricing policy` link to `#pricing-policy`.
- [ ] **Step 3:** Add the two-question policy section between About and Contact.
- [ ] **Step 4:** Add scoped responsive CSS for the new markup, matching the existing black/red theme.
- [ ] **Step 5:** Bump the page's development cache marker if needed for reliable previewing.

### Task 3: Verify the development branch

**Files:**
- Verify: `index.html`
- Verify: `tests/test_pet_hair_policy.py`

**Interfaces:**
- Consumes: completed branch changes.
- Produces: a reviewable development branch with no live-site mutation.

- [ ] **Step 1:** Confirm both disclosure locations contain `$20` and the approved threshold.
- [ ] **Step 2:** Confirm the final-payment wording mentions itemization and receipt/payment confirmation email.
- [ ] **Step 3:** Confirm the in-page link target exists exactly once.
- [ ] **Step 4:** Compare `main...dev/pet-hair-policy` and verify only development documentation/tests plus the intended website file changed.
- [ ] **Step 5:** Do not merge or move Pages; hand the branch back for user review.