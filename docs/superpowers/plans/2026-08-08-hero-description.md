# Hero Description Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the existing hero description with the approved normal-weight business copy.

**Architecture:** Keep the existing `.hero-text` element and CSS unchanged. Protect the approved copy with the static HTML contract suite.

**Tech Stack:** Static HTML, Python `unittest`, GitHub Pages.

## Global Constraints

- Work only on `bopeeps-v3-modern`.
- Use the approved copy exactly and keep normal `.hero-text` styling.
- Do not change hero layout, headings, buttons, image, spacing, or other site content.
- Do not merge or modify `main`, Porkbun, or the production domain.

---

### Task 1: Replace the hero description

**Files:**
- Modify: `index.html:80`
- Test: `tests/test_site_contract.py`

**Interfaces:**
- Consumes: the existing `.hero-text` paragraph.
- Produces: the approved description rendered by the unchanged responsive hero styles.

- [x] **Step 1: Write the failing contract test**

Assert that the `.hero-text` node contains this literal text:

```text
We proudly detail cars, SUVs, trucks, big rigs, RVs, PWCs, tandem axle trailers, and more. If you've got it, we'll make it showroom ready with professional detailing done to your standards. A clean vehicle is more than just looks, it's pride.
```

Also assert the previous `Professional interior and exterior detailing` sentence is absent.

- [x] **Step 2: Verify the test fails**

Run `python -m unittest tests.test_site_contract.SiteContractTests.test_hero_uses_the_approved_business_description -v` and expect a failure showing the previous copy.

- [x] **Step 3: Implement the copy replacement**

Replace only the text content of `p.hero-text` in `index.html` with the approved paragraph.

- [x] **Step 4: Verify locally**

Run the focused test, full `unittest` suite, `node --check script-v3.js`, `node tests/test_script_behavior.mjs`, and `git diff --check`.

- [ ] **Step 5: Publish and verify**

Commit and push only `bopeeps-v3-modern`, then confirm the live hero text and absence of horizontal overflow on the existing GitHub Pages preview.
