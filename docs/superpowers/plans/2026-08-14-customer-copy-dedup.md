# Customer Copy De-duplication Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Remove repetitive location reassurance from every customer-facing page while preserving local-search relevance, the Hayesville destination, device-location directions, and all existing business facts.

**Architecture:** Keep the current static HTML structure and existing copy-audit workflow. Extend the customer-copy regression suite first, then update the existing deterministic final-polish script so the same transformation can be replayed safely. The apply workflow will run the main copy audit, the final polish, the complete regression suite, and JavaScript syntax validation before committing generated page changes to the dev branch.

**Tech Stack:** Static HTML/CSS/JavaScript, Python 3.12 transformation scripts and pytest regression tests, GitHub Actions.

## Global Constraints

- Tone remains professional, friendly, and straightforward.
- State the Hayesville location where it helps customers find the business; do not repeatedly explain the physical-location model.
- Remove repeated `in-shop`, `all detailing is completed at`, `customers are welcome from anywhere`, and repeated `Hayesville shop` reassurance from visible copy.
- Keep destination-only Google Maps directions with no city-specific `origin` parameter.
- Keep local-page city targeting and minimal regional references: Hayesville/Clay County/Lake Chatuge, Murphy/Cherokee County, Hiawassee/Towns County/Lake Chatuge, Young Harris/Towns County, Blairsville/Union County.
- Do not change canonical URLs, public page URLs, service names, service prices, phone, email, business address, business hours, Booksy URL, Facebook URL, or pet-hair policy substance.
- Do not merge or publish to `main` until the revised preview is reviewed and approved.

---

### Task 1: Add regression guards for location-copy de-duplication

**Files:**
- Modify: `tests/test_customer_copy_audit.py`

**Interfaces:**
- Consumes: existing `PUBLIC`, `LOCAL`, `text()`, `links()`, `DIRECTIONS_HREF`, and customer-copy assertions.
- Produces: regression requirements that the final-polish script must satisfy.

- [ ] **Step 1: Extend the failing tests**

Add exact guards equivalent to:

```python
def test_customer_copy_does_not_repeat_location_reassurance():
    banned = [
        'customers from anywhere are welcome to book',
        'customers are welcome from anywhere',
        'professional in-shop auto detailing',
        'all detailing is completed at',
    ]
    for name in PUBLIC:
        lower = text(name).lower()
        for phrase in banned:
            assert phrase not in lower, f'{name}: {phrase}'


def test_homepage_service_area_is_concise():
    home = text('index.html')
    assert 'BoPeeps welcomes drivers from western North Carolina, north Georgia, and beyond.' in home
    assert 'Find us at 1516 US-64 in Hayesville, NC.' in home
    assert 'Customers from anywhere are welcome to book' not in home


def test_customer_pages_use_concise_location_identity():
    identity = 'BoPeeps Details &amp; More · 1516 US-64, Hayesville, NC 28904'
    for name in ['services.html', 'policies.html', *LOCAL]:
        assert identity in text(name), name


def test_footers_drop_in_shop_repetition():
    for name in PUBLIC:
        assert 'Professional in-shop auto detailing' not in text(name)
```

Also update any older assertion that explicitly requires `Customers from anywhere are welcome to book` so it requires only the concise regional sentence.

- [ ] **Step 2: Run Site CI and verify the new guards fail for the current dev copy**

Expected failures must point to the known repetition: homepage duplicate welcome sentence, `all detailing is completed at` banners, `customers are welcome from anywhere`, and `Professional in-shop auto detailing` footer text.

- [ ] **Step 3: Commit the red regression state**

Commit message: `test: guard customer copy de-duplication`

---

### Task 2: Implement deterministic de-duplication in the final-polish transformation

**Files:**
- Modify: `scripts/apply_customer_copy_final_polish.py`
- Generated/modified by workflow: `index.html`, `services.html`, `policies.html`, `privacy.html`, `404.html`, `auto-detailing-hayesville-nc.html`, `auto-detailing-murphy-nc.html`, `auto-detailing-hiawassee-ga.html`, `auto-detailing-young-harris-ga.html`, `auto-detailing-blairsville-ga.html`

**Interfaces:**
- Consumes: the already-approved customer-copy output produced by `scripts/apply_customer_copy_audit.py` and the first final-polish pass.
- Produces: concise public copy that satisfies Task 1 without changing page structure, business facts, or direction URLs.

- [ ] **Step 1: Add exact homepage replacements**

Transform the service-area paragraph to:

```html
<p>BoPeeps welcomes drivers from western North Carolina, north Georgia, and beyond. Find us at 1516 US-64 in Hayesville, NC.</p>
```

Normalize any repeated footer copy to:

```html
<p>Professional auto detailing in Hayesville, North Carolina.</p>
```

Normalize the structured-data business description from `Professional in-shop auto detailing...` to `Professional auto detailing in Hayesville, NC.` while preserving the Hayesville address and `areaServed` data.

- [ ] **Step 2: Simplify Services and Policies location copy**

Services hero lede becomes service-focused:

```html
<p class="lede">Compare our detailing packages, check vehicle-size pricing, and book online through Booksy.</p>
```

Services location banner becomes:

```html
<div class="seo-shop-banner"><strong>BoPeeps Details &amp; More · 1516 US-64, Hayesville, NC 28904</strong></div>
```

Services regional section keeps nearby-search value but removes another broad welcome statement:

```html
<div class="seo-card" style="margin-top:18px"><h2>Find BoPeeps from nearby communities</h2><p>Looking for BoPeeps from Murphy, Hiawassee, Young Harris, or Blairsville? Use the local pages below for directions and nearby information.</p>
```

Policies location banner becomes the same concise business/address identity and removes `Customers are welcome from anywhere`.

- [ ] **Step 3: Simplify local landing-page location copy**

For all five local pages, replace the explanatory appointment banner with:

```html
<div class="seo-shop-banner"><strong>BoPeeps Details &amp; More · 1516 US-64, Hayesville, NC 28904</strong></div>
```

Use concise introductions that mention the search city/region and Hayesville no more than needed. Required intent examples:

```text
Hayesville: BoPeeps Details & More provides professional auto detailing in Hayesville for Clay County and the Lake Chatuge area.
Murphy: Looking for professional auto detailing near Murphy? BoPeeps Details & More is on US-64 in Hayesville, convenient for Murphy and Cherokee County drivers.
Hiawassee: Looking for professional auto detailing near Hiawassee? BoPeeps Details & More is in Hayesville, convenient for Towns County and the Lake Chatuge area.
Young Harris: Looking for professional auto detailing near Young Harris? BoPeeps Details & More is in Hayesville, convenient for Towns County drivers.
Blairsville: Looking for professional auto detailing near Blairsville? BoPeeps Details & More is in Hayesville, convenient for Union County drivers.
```

Replace every nearby-community paragraph with:

```html
<p>Coming from another nearby town? Use the links below for local information, or get directions from your current location.</p>
```

Keep all destination-only `Get Directions` links unchanged.

- [ ] **Step 4: Normalize customer-facing metadata where it repeats `Hayesville shop`**

Keep city keywords and Hayesville destination context, but use `location`, `BoPeeps`, or `directions` rather than repeatedly saying `our Hayesville shop`. Do not change titles, canonicals, Open Graph URLs, or Twitter card structure.

- [ ] **Step 5: Let the apply workflow run the transformation and full verification before it commits generated pages**

Required workflow order remains:

```text
apply_customer_copy_audit.py
apply_customer_copy_final_polish.py
pytest -q
node --check script-v3.js
commit generated customer copy
```

Expected: 0 pytest failures and JavaScript syntax success before the bot commit is made.

---

### Task 3: Final editorial and integration verification

**Files:**
- Review: every public HTML page
- Review: `tests/test_customer_copy_audit.py`
- Review: `scripts/apply_customer_copy_final_polish.py`

**Interfaces:**
- Consumes: final generated branch state from Task 2.
- Produces: exact dev commit ready for user preview, not production.

- [ ] **Step 1: Trigger ordinary Site CI on a user-authored final-head commit**

Run the complete configured suite. Expected: all pytest tests pass and `node --check script-v3.js` succeeds on the exact final dev head.

- [ ] **Step 2: Read the rendered-source copy on all public pages**

Verify there is no visible repetition of `customers from anywhere`, `in-shop`, `all detailing is completed at`, or excessive `Hayesville shop` language. Confirm the address, Directions action, service names/prices, policies, contact details, regional references, and local H1/title intent remain correct.

- [ ] **Step 3: Compare `dev/customer-copy-audit` against `main`**

Expected: branch remains ahead of current production and 0 commits behind. Confirm `main` and the current Pages deployment did not change.

- [ ] **Step 4: Provide a pinned preview at the exact final CI-tested commit**

Stop before PR/merge/publish. Ask for explicit approval before production integration.
