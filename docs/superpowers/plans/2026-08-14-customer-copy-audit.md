# BoPeeps Customer-Facing Copy Audit Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rewrite the BoPeeps public website copy so it is professional, friendly, straightforward, customer-first, and free of defensive SEO/developer language while preserving business facts, local-search intent, layout, URLs, structured data, booking, pricing, and rollback safety.

**Architecture:** Keep the existing static HTML/CSS/JS architecture. Make copy-only edits to the public HTML pages, update regression tests that currently encode the old wording, add a focused customer-copy regression file, and expand CI to run on the new development branch. Do not redesign components or change business logic.

**Tech Stack:** Static HTML/CSS/JavaScript, Python 3.12 + pytest, GitHub Actions, GitHub Pages.

## Global Constraints

- Work only on `dev/customer-copy-audit` until user approves a preview.
- Tone: professional, friendly, straightforward.
- BoPeeps welcomes customers from anywhere; the five local pages are discovery pages, not service restrictions.
- All detailing is completed at `1516 US-64, Hayesville, NC 28904`.
- Preserve phone `980-598-1864` / `tel:+19805981864`, email `hello@bopeepsdetails.com`, hours, Booksy URL, service names, prices, and the approved $20 excessive-pet-hair policy substance.
- Preserve public URLs, canonical URLs, the LocalBusiness schema facts, layout, accessibility structure, optimized assets, lazy Booksy loading, protected `main`, and the emergency rollback workflow.
- Local directions must use a destination-only Google Maps directions URL and visible label `Get Directions`; no local-page `origin=` parameters.
- Keep regional references simple and minimal; no encyclopedia-style filler.
- Do not invent cancellation, refund, deposit, damage, payment, late-arrival, mobile-service, branch-location, or other policies.

---

### Task 1: Update CI and lock the new copy contract with failing tests

**Files:**
- Modify: `.github/workflows/ci.yml`
- Create: `tests/test_customer_copy_audit.py`
- Modify: `tests/test_local_seo_expansion.py`
- Modify: `tests/test_pet_hair_policy.py`

**Interfaces:**
- Consumes: existing public-page constants and static HTML files.
- Produces: regression rules that all later copy tasks must satisfy.

- [ ] **Step 1: Add the new branch to push CI**

Change the Site CI push branch list to include:

```yaml
      - dev/customer-copy-audit
```

Keep `dev/site-cleanup-phone-audit` and `main` unchanged.

- [ ] **Step 2: Create `tests/test_customer_copy_audit.py` with failing customer-language guards**

Use this structure:

```python
from pathlib import Path
from urllib.parse import urlsplit, parse_qs

PUBLIC = [
    'index.html', 'services.html', 'auto-detailing-hayesville-nc.html',
    'auto-detailing-murphy-nc.html', 'auto-detailing-hiawassee-ga.html',
    'auto-detailing-young-harris-ga.html', 'auto-detailing-blairsville-ga.html',
    'policies.html', 'privacy.html', '404.html',
]
LOCAL = PUBLIC[2:7]
DESTINATION = '1516 US-64, Hayesville, NC 28904'


def text(name):
    return Path(name).read_text(encoding='utf-8')


def test_customer_pages_do_not_use_defensive_or_internal_copy():
    banned = [
        'real hayesville shop', 'real local work', 'genuine bopeeps photos on this site',
        'one real shop', 'single bopeeps shop', 'one booking flow',
        'approved surrounding service areas', 'hard-coded mileage',
        'hard-coded drive-time', 'fixed mileage', 'fixed drive-time',
        'this is the bopeeps physical shop', 'does not claim to run',
    ]
    for name in PUBLIC:
        lower = text(name).lower()
        for phrase in banned:
            assert phrase not in lower, f'{name}: {phrase}'


def test_homepage_uses_customer_first_trust_and_service_area_copy():
    home = text('index.html')
    for phrase in [
        'Hayesville Location', 'Conveniently located on US-64',
        'Clear package pricing', 'Book online', 'Quality Detailing',
        'Careful interior &amp; exterior service', 'Recent BoPeeps Work',
    ]:
        assert phrase in home
    assert 'western North Carolina, north Georgia, and beyond' in home


def test_local_pages_use_device_location_directions():
    for name in LOCAL:
        page = text(name)
        assert '>Get Directions<' in page
        for href in page.split('href="')[1:]:
            url = href.split('"', 1)[0]
            if url.startswith('https://www.google.com/maps/dir/?api=1'):
                query = parse_qs(urlsplit(url).query)
                assert 'origin' not in query, name
                assert query.get('destination') == [DESTINATION], name


def test_local_pages_welcome_beyond_named_towns_without_implying_branch_locations():
    combined = '\n'.join(text(name) for name in LOCAL).lower()
    assert 'customers from anywhere' in text('index.html').lower() or 'and beyond' in text('index.html').lower()
    assert 'mobile detailing available' not in combined
    assert 'we come to you' not in combined
```

- [ ] **Step 3: Update outdated expectations in `tests/test_local_seo_expansion.py`**

Replace the assertion that requires `Current BoPeeps services` with a natural services eyebrow such as `Detailing packages`.

Replace the homepage proof expectations:

```python
for proof in ['Hayesville Location', 'Clear package pricing', 'Book online', 'Quality Detailing']:
    assert proof in home
```

Update `test_local_pages_have_distinct_context_and_directions` so each page requires only concise local markers:

```python
requirements = {
    'auto-detailing-hayesville-nc.html': ['Clay County'],
    'auto-detailing-murphy-nc.html': ['Cherokee County'],
    'auto-detailing-hiawassee-ga.html': ['Towns County', 'Lake Chatuge'],
    'auto-detailing-young-harris-ga.html': ['Towns County'],
    'auto-detailing-blairsville-ga.html': ['Union County'],
}
```

For every local page assert:

```python
assert 'https://www.google.com/maps/dir/?api=1' in text
assert 'origin=' not in text
assert 'destination=1516%20US-64%2C%20Hayesville%2C%20NC%2028904' in text
assert '>Get Directions<' in text
```

Remove the old requirement for `Appalachian` and `Young Harris College`.

Update `test_homepage_exposes_crawlable_core_and_service_area_links` to assert the homepage clearly says detailing is completed at the Hayesville shop without requiring the exact old sentence.

- [ ] **Step 4: Update `tests/test_pet_hair_policy.py` to preserve policy meaning without old audit wording**

Keep the approved threshold, $20 fee, and itemized checkout sentence tests. Replace old wording checks with:

```python
assert 'Standard pricing' in policies
assert 'When the pet-hair fee applies' in policies
assert 'At checkout' in policies
assert 'A few stray hairs are not the intended threshold.' in policies
assert '$20 Excessive Pet Hair Removal' in policies
assert 'Booksy handles appointment availability and checkout.' in policies
```

- [ ] **Step 5: Commit the red tests before changing customer copy**

Commit message:

```text
test: define customer-first copy contract
```

Expected CI: failures in the new copy assertions and any deliberately updated old-copy assertions.

---

### Task 2: Rewrite the homepage customer-facing copy

**Files:**
- Modify: `index.html`

**Interfaces:**
- Consumes: copy contract from Task 1.
- Produces: customer-first homepage copy while preserving section order, service cards, pricing, interactive behavior, and layout hooks.

- [ ] **Step 1: Rewrite metadata without changing local intent**

Keep the title. Change descriptions to customer-first wording, for example:

```html
<meta name="description" content="Auto detailing at BoPeeps Details & More in Hayesville, NC. View package pricing, detailing services, recent work, and book online through Booksy." />
<meta property="og:description" content="Explore BoPeeps detailing services and pricing, see recent work, and book your appointment at our Hayesville shop." />
<meta name="twitter:description" content="Explore BoPeeps detailing services and pricing, see recent work, and book your appointment at our Hayesville shop." />
```

- [ ] **Step 2: Replace trust-strip wording exactly**

```text
Hayesville Location — Conveniently located on US-64
Clear package pricing — Vehicle-size pricing shown upfront
Book online — Schedule through Booksy
Quality Detailing — Careful interior & exterior service
```

- [ ] **Step 3: Polish the services introduction**

Use:

```html
<p class="eyebrow">Detailing packages</p>
<h2>Our detailing services</h2>
<p>Choose the level that fits your vehicle, then book your appointment through Booksy.</p>
```

Do not change service names, descriptions, or prices.

- [ ] **Step 4: Rewrite gallery proof copy**

Use:

```html
<p class="eyebrow">Recent BoPeeps Work</p>
<h2>See the finish.</h2>
<p>Take a look at vehicles we've detailed, then try the interactive cleaning demo below.</p>
```

Change gallery `aria-label` to `BoPeeps detailing gallery`.

Change the final gallery caption from `Real local work` to `Interior detailing`.

Keep image alt text factual. Keep the interactive demo's `simulated grime` wording in visible and accessibility text.

- [ ] **Step 5: Polish Why BoPeeps**

Keep `Detailing without the runaround.` and the three-card layout. Replace defensive location repetition with customer benefits. Suggested third card:

```html
<h3>Easy in-shop service</h3>
<p>Drop off at our Hayesville location, ask questions directly, and know where your appointment is being handled.</p>
```

- [ ] **Step 6: Reframe service area as an open invitation**

Use a heading such as:

```html
<p class="eyebrow">Come see us in Hayesville</p>
<h2 id="service-area-title">Worth the drive from wherever you are.</h2>
<p>BoPeeps welcomes customers from western North Carolina, north Georgia, and beyond. Customers from anywhere are welcome to book; all detailing is completed at our Hayesville shop at 1516 US-64, Hayesville, NC 28904.</p>
```

Keep all five local-page links.

- [ ] **Step 7: Commit homepage copy**

Commit message:

```text
copy: make homepage customer-first
```

---

### Task 3: Rewrite services, policies, and privacy copy

**Files:**
- Modify: `services.html`
- Modify: `policies.html`
- Modify: `privacy.html`
- Review only: `404.html`

**Interfaces:**
- Consumes: business-fact and policy regression tests.
- Produces: plain-language support pages without changing business rules.

- [ ] **Step 1: Rewrite Services hero/banner and service-area copy**

Use a lede such as:

```text
Compare our detailing packages, check vehicle-size pricing, and book your appointment at the Hayesville shop.
```

Replace `One shop, one booking flow.` with:

```text
Visit us in Hayesville. All detailing is completed at 1516 US-64, Hayesville, NC 28904, and customers are welcome from surrounding communities and beyond.
```

Replace `approved surrounding service areas` with:

```text
BoPeeps is based in Hayesville and welcomes customers from western North Carolina, north Georgia, and beyond.
```

Keep all service names, prices, descriptions, specialty-vehicle guidance, and Booksy buttons.

- [ ] **Step 2: Rewrite Policies labels without changing policy substance**

Use:

```text
Eyebrow: Pricing policy
H2: Standard pricing
Fact 1: Standard pricing
Fact 2: When the pet-hair fee applies
Fact 3: At checkout
```

Keep these exact policy facts:

```text
Excessive pet hair requiring additional removal time
$20 pet hair removal fee
A few stray hairs are not the intended threshold.
$20 Excessive Pet Hair Removal
itemized in your final checkout and reflected on your receipt or payment confirmation email
```

Replace the audit-like note with:

```text
Booking and checkout: Booksy handles appointment availability and checkout. If the pet-hair charge applies, it will be shown as part of the final appointment amount and reflected on your receipt or payment confirmation email.
```

Reframe the location banner to a simple appointment-location note; do not list towns as if they are restrictions.

- [ ] **Step 3: Rewrite Privacy in direct language**

Use a simpler lede such as:

```text
A straightforward overview of how this website works and the third-party services used for booking, directions, and social media.
```

Replace:

```text
The current BoPeeps website does not claim to run a separate advertising tracker, mailing-list signup, or first-party analytics platform.
```

with:

```text
This website does not currently use a BoPeeps mailing-list signup or a separate first-party analytics or advertising platform. Third-party services may use their own cookies or similar technologies when their content or booking tools are loaded.
```

Do not strengthen any privacy promise beyond what the site supports.

- [ ] **Step 4: Leave 404 substantially unchanged**

Only correct a consistency issue if discovered by the final audit.

- [ ] **Step 5: Commit support-page copy**

Commit message:

```text
copy: simplify services policies and privacy
```

---

### Task 4: Rewrite all five local landing pages and device-location directions

**Files:**
- Modify: `auto-detailing-hayesville-nc.html`
- Modify: `auto-detailing-murphy-nc.html`
- Modify: `auto-detailing-hiawassee-ga.html`
- Modify: `auto-detailing-young-harris-ga.html`
- Modify: `auto-detailing-blairsville-ga.html`

**Interfaces:**
- Consumes: local-page H1/canonical/schema tests and destination-only directions tests.
- Produces: distinct local-discovery pages that do not imply service restrictions or branch locations.

- [ ] **Step 1: Keep local titles/H1s and simplify intros**

Retain each page's local search intent in `<title>` and H1. Use concise customer intros, e.g. Murphy:

```text
Looking for professional auto detailing near Murphy? BoPeeps Details & More welcomes Murphy and Cherokee County customers at our Hayesville shop on US-64.
```

Use similarly short local context for the other pages:
- Hayesville: Clay County; optionally one Lake Chatuge reference.
- Hiawassee: Towns County / Lake Chatuge.
- Young Harris: Towns County.
- Blairsville: Union County.

Do not require Appalachian, Young Harris College, county-seat facts, tourism language, or geographic filler.

- [ ] **Step 2: Replace defensive shop banners**

Each page gets one simple statement such as:

```text
Your appointment is at BoPeeps in Hayesville. All detailing is completed at 1516 US-64, Hayesville, NC 28904.
```

Do not repeat `one`, `real`, `single`, `physical shop`, or similar proof language.

- [ ] **Step 3: Rewrite the local customer paragraph**

Use one short paragraph that explains customers from the named area are welcome and can compare services, book, or call for specialty vehicles. Do not describe website architecture or explain why routing is live.

- [ ] **Step 4: Convert directions to destination-only URLs**

Use this exact destination URL shape on every local page:

```html
href="https://www.google.com/maps/dir/?api=1&amp;destination=1516%20US-64%2C%20Hayesville%2C%20NC%2028904"
```

Visible link/button text:

```text
Get Directions
```

Remove every `origin=` parameter and every `Directions from <city>` label.

- [ ] **Step 5: Simplify nearby-community section**

Use a heading such as `Nearby communities` or `Coming from another nearby town?` and explain that the linked pages help customers find BoPeeps from nearby areas. Do not call them approved service areas or imply those towns are the only customers accepted.

- [ ] **Step 6: Keep pricing, shop facts, canonicals, schema, Booksy, and policy notes unchanged in substance**

Do not modify LocalBusiness JSON-LD fields as part of this copy pass.

- [ ] **Step 7: Commit local-page copy**

Commit message:

```text
copy: simplify local discovery pages and directions
```

---

### Task 5: Final audit, full verification, and preview gate

**Files:**
- Review: all public `.html` files
- Review: `tests/*.py`
- Review: `.github/workflows/ci.yml`
- Generated locally by test only: `_site/`

**Interfaces:**
- Consumes: completed copy and regression suite.
- Produces: verified dev-branch candidate ready for user preview; no PR or production release yet.

- [ ] **Step 1: Run the focused copy tests**

Run:

```bash
pytest -q tests/test_customer_copy_audit.py tests/test_local_seo_expansion.py tests/test_pet_hair_policy.py
```

Expected: PASS.

- [ ] **Step 2: Run the full regression suite**

Run:

```bash
pytest -q
```

Expected: all tests pass.

- [ ] **Step 3: Validate JavaScript syntax**

Run:

```bash
node --check script-v3.js
```

Expected: exit 0 with no syntax error.

- [ ] **Step 4: Verify the public build**

Run:

```bash
python scripts/build_site.py
```

Confirm `_site/` includes only the approved public files/assets and no `docs/`, `tests/`, `.github/`, `scripts/`, or README.

- [ ] **Step 5: Run a final banned-language scan**

Search all public HTML for:

```text
real hayesville shop
real local work
genuine bopeeps photos on this site
one real shop
one booking flow
approved surrounding service areas
hard-coded
fixed mileage
fixed drive-time
does not claim to run
```

Expected: none.

- [ ] **Step 6: Review the diff for protected facts**

Confirm no accidental changes to:
- service names and all nine price points;
- phone/email/address/hours;
- Booksy and Facebook URLs;
- pet-hair policy substance and $20 amount;
- page URLs/canonicals/sitemap;
- LocalBusiness schema fields;
- CSS layout fixes and JS behavior;
- rollback workflow.

- [ ] **Step 7: Commit any final consistency fixes**

Commit message if needed:

```text
copy: finish customer-facing language audit
```

- [ ] **Step 8: Provide user preview and audit summary**

Do not open a PR and do not merge to `main` yet. Give the user a pinned preview/review point, list exactly what changed, and wait for explicit production approval.
