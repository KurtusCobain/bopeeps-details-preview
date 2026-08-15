from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BOOKSY = 'https://booksy.com/en-us/1808686_bopeeps-detail-more_other_26564_hayesville'
MAPS_DIRECTIONS = 'https://www.google.com/maps/dir/?api=1&amp;destination=1516%20US-64%2C%20Hayesville%2C%20NC%2028904'
SHOP_ADDRESS = '1516 US-64, Hayesville, NC 28904'


def read(name: str) -> str:
    return (ROOT / name).read_text(encoding='utf-8')


def write(name: str, content: str) -> None:
    (ROOT / name).write_text(content, encoding='utf-8')


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if new in text:
        return text
    if old not in text:
        raise RuntimeError(f'Could not find expected source for {label}')
    return text.replace(old, new, 1)


def replace_regex_once(text: str, pattern: str, replacement: str, label: str) -> str:
    updated, count = re.subn(pattern, replacement, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f'Expected one match for {label}, found {count}')
    return updated


def set_descriptions(page: str, meta: str, social: str) -> str:
    page = replace_regex_once(
        page,
        r'<meta name="description" content="[^"]*"\s*/>',
        f'<meta name="description" content="{meta}" />',
        'meta description',
    )
    page = replace_regex_once(
        page,
        r'<meta property="og:description" content="[^"]*"\s*/>',
        f'<meta property="og:description" content="{social}" />',
        'Open Graph description',
    )
    page = replace_regex_once(
        page,
        r'<meta name="twitter:description" content="[^"]*"\s*/>',
        f'<meta name="twitter:description" content="{social}" />',
        'Twitter description',
    )
    return page


def patch_homepage() -> None:
    name = 'index.html'
    page = read(name)
    page = set_descriptions(
        page,
        'Auto detailing at BoPeeps Details & More in Hayesville, NC. View package pricing, detailing services, recent work, and book online through Booksy.',
        'Explore BoPeeps detailing services and pricing, see recent work, and book your appointment at our Hayesville shop.',
    )

    page = replace_once(
        page,
        '<section class="trust-strip" aria-label="BoPeeps at a glance"><div class="shell trust-grid"><article><span class="trust-icon" aria-hidden="true">⌖</span><div><strong>Real Hayesville shop</strong><small>One physical location on US-64</small></div></article><article><span class="trust-icon" aria-hidden="true">$</span><div><strong>Clear package pricing</strong><small>Vehicle-size pricing shown upfront</small></div></article><article><span class="trust-icon" aria-hidden="true">◷</span><div><strong>Book online</strong><small>Schedule through Booksy</small></div></article><article><span class="trust-icon" aria-hidden="true">✦</span><div><strong>Real local work</strong><small>Genuine BoPeeps photos on this site</small></div></article></div></section>',
        '<section class="trust-strip" aria-label="BoPeeps at a glance"><div class="shell trust-grid"><article><span class="trust-icon" aria-hidden="true">⌖</span><div><strong>Hayesville Location</strong><small>Conveniently located on US-64</small></div></article><article><span class="trust-icon" aria-hidden="true">$</span><div><strong>Clear package pricing</strong><small>Vehicle-size pricing shown upfront</small></div></article><article><span class="trust-icon" aria-hidden="true">◷</span><div><strong>Book online</strong><small>Schedule through Booksy</small></div></article><article><span class="trust-icon" aria-hidden="true">✦</span><div><strong>Quality Detailing</strong><small>Careful interior &amp; exterior service</small></div></article></div></section>',
        'homepage trust strip',
    )

    page = replace_once(
        page,
        '<div class="section-heading centered"><p class="eyebrow">Current BoPeeps services</p><h2>Our detailing services</h2><p>Pick the level that fits your vehicle, then finish scheduling securely on Booksy.</p></div>',
        '<div class="section-heading centered"><p class="eyebrow">Detailing packages</p><h2>Our detailing services</h2><p>Choose the level that fits your vehicle, then book your appointment through Booksy.</p></div>',
        'homepage services introduction',
    )

    page = replace_once(
        page,
        '<div class="section-heading"><p class="eyebrow">Real BoPeeps work</p><h2>See the finish.</h2><p>These are real vehicles photographed from BoPeeps detailing work. Browse the gallery first, then try the interactive cleaning demo below.</p></div><div class="gallery-grid" aria-label="Real BoPeeps detailing work">',
        '<div class="section-heading"><p class="eyebrow">Recent BoPeeps Work</p><h2>See the finish.</h2><p>Take a look at vehicles we\'ve detailed, then try the interactive cleaning demo below.</p></div><div class="gallery-grid" aria-label="BoPeeps detailing gallery">',
        'homepage gallery introduction',
    )
    page = replace_once(page, '<figcaption>Real local work</figcaption>', '<figcaption>Interior detailing</figcaption>', 'gallery caption')
    page = page.replace('Drag to reveal the selected real BoPeeps photo.', 'Drag to reveal the selected BoPeeps photo.')

    page = replace_once(
        page,
        '<p>Bring us the daily driver, work truck, Jeep, RV, PWC, or something bigger. We focus on careful interior and exterior finish work at one straightforward Hayesville shop.</p>',
        '<p>Bring us the daily driver, work truck, Jeep, RV, PWC, or something bigger. We focus on careful interior and exterior work and a finish you can feel good about.</p>',
        'Why BoPeeps introduction',
    )
    page = replace_once(
        page,
        '<article><span aria-hidden="true">⌖</span><h3>Straightforward in-shop service</h3><p>One Hayesville location keeps drop-off, questions, and appointment expectations clear from the start.</p></article>',
        '<article><span aria-hidden="true">⌖</span><h3>Easy in-shop service</h3><p>Drop off at our Hayesville location, ask questions directly, and know where your appointment is being handled.</p></article>',
        'Why BoPeeps location benefit',
    )

    page = replace_once(
        page,
        '<section class="section home-service-area" aria-labelledby="service-area-title"><div class="shell"><article class="seo-card"><p class="eyebrow">Our service area</p><h2 id="service-area-title">One Hayesville shop serving nearby communities</h2><p>BoPeeps welcomes drivers from Hayesville, Murphy, Hiawassee, Young Harris, and Blairsville. <strong>All appointments are completed at our Hayesville shop</strong> at 1516 US-64, Hayesville, NC 28904; we are not currently offering mobile detailing.</p>',
        '<section class="section home-service-area" aria-labelledby="service-area-title"><div class="shell"><article class="seo-card"><p class="eyebrow">Come see us in Hayesville</p><h2 id="service-area-title">Worth the drive from wherever you are.</h2><p>BoPeeps welcomes customers from western North Carolina, north Georgia, and beyond. Customers from anywhere are welcome to book; <strong>all detailing is completed at our Hayesville shop</strong> at 1516 US-64, Hayesville, NC 28904.</p>',
        'homepage service area',
    )
    write(name, page)


def patch_services() -> None:
    name = 'services.html'
    page = read(name)
    page = set_descriptions(
        page,
        'Compare BoPeeps auto detailing packages and vehicle-size pricing in Hayesville, NC, then book online through Booksy.',
        'Compare BoPeeps detailing packages and vehicle-size pricing, then book your appointment at our Hayesville shop.',
    )
    page = replace_once(
        page,
        '<p class="lede">Compare the current BoPeeps detailing packages, understand vehicle-condition pricing, and book your appointment at our Hayesville shop.</p>',
        '<p class="lede">Compare our detailing packages, check vehicle-size pricing, and book your appointment at the Hayesville shop.</p>',
        'services lede',
    )
    page = replace_once(
        page,
        '<div class="seo-shop-banner"><strong>One shop, one booking flow.</strong> Every appointment is completed at our Hayesville shop at 1516 US-64, Hayesville, NC 28904. Customers from Murphy, Hiawassee, Young Harris, Blairsville, and surrounding areas bring their vehicles to us for service.</div>',
        '<div class="seo-shop-banner"><strong>Visit us in Hayesville.</strong> All detailing is completed at 1516 US-64, Hayesville, NC 28904, and customers are welcome from surrounding communities and beyond.</div>',
        'services shop banner',
    )
    page = replace_once(
        page,
        '<div class="seo-card" style="margin-top:18px"><h2>Serving western North Carolina and north Georgia</h2><p>BoPeeps is based in Hayesville. We welcome customers from the approved surrounding service areas below, with all detailing completed at the Hayesville shop.</p>',
        '<div class="seo-card" style="margin-top:18px"><h2>Serving western North Carolina and north Georgia</h2><p>BoPeeps is based in Hayesville and welcomes customers from western North Carolina, north Georgia, and beyond. The links below can help nearby customers find the shop and plan a visit.</p>',
        'services area copy',
    )
    write(name, page)


def patch_policies() -> None:
    name = 'policies.html'
    page = read(name)
    page = set_descriptions(
        page,
        'BoPeeps pricing and vehicle-condition information, including when the $20 excessive pet-hair removal fee may apply and how it appears at checkout.',
        'Review BoPeeps standard pricing and when the $20 excessive pet-hair removal fee may apply.',
    )
    page = replace_once(
        page,
        '<p class="lede">The current BoPeeps policy covers standard vehicle-condition pricing and the $20 excessive pet-hair removal fee for appointments completed at our Hayesville shop.</p>',
        '<p class="lede">Here is what to know about standard vehicle-condition pricing and the $20 excessive pet-hair removal fee.</p>',
        'policies lede',
    )
    page = replace_once(page, '<p class="eyebrow">Current BoPeeps policy</p><h2>Standard-condition pricing</h2>', '<p class="eyebrow">Pricing policy</p><h2>Standard pricing</h2>', 'policy heading')
    page = replace_once(page, '<strong>Standard condition baseline</strong>', '<strong>Standard pricing</strong>', 'standard pricing label')
    page = replace_once(page, '<strong>Excessive pet hair threshold</strong>', '<strong>When the pet-hair fee applies</strong>', 'pet hair label')
    page = replace_once(page, '<strong>Checkout and receipt</strong>', '<strong>At checkout</strong>', 'checkout label')
    page = replace_once(
        page,
        '<aside class="seo-note"><strong>Booking and checkout:</strong> Booksy handles appointment availability and the checkout workflow. This page states only the BoPeeps pricing and vehicle-condition policy currently provided on this website.</aside>',
        '<aside class="seo-note"><strong>Booking and checkout:</strong> Booksy handles appointment availability and checkout. If the pet-hair charge applies, it will be shown as part of the final appointment amount and reflected on your receipt or payment confirmation email.</aside>',
        'policy booking note',
    )
    page = replace_once(
        page,
        '<div class="seo-shop-banner" style="margin-top:18px"><strong>In-shop appointments.</strong> BoPeeps currently performs detailing at 1516 US-64, Hayesville, NC 28904. Customers from Hayesville, Murphy, Hiawassee, Young Harris, and Blairsville bring their vehicles to the Hayesville shop.</div>',
        '<div class="seo-shop-banner" style="margin-top:18px"><strong>Appointment location.</strong> Detailing is completed at BoPeeps, 1516 US-64, Hayesville, NC 28904. Customers are welcome from anywhere.</div>',
        'policy appointment banner',
    )
    write(name, page)


def patch_privacy() -> None:
    name = 'privacy.html'
    page = read(name)
    page = set_descriptions(
        page,
        'Learn how the BoPeeps website handles basic request data and uses third-party services such as Booksy, Google Maps, and Facebook.',
        'A straightforward overview of website request data and the third-party services BoPeeps uses for booking, directions, and social media.',
    )
    page = replace_once(
        page,
        '<p class="lede">A practical explanation of this website\'s current behavior and the third-party services customers may choose to use.</p>',
        '<p class="lede">A straightforward overview of how this website works and the third-party services used for booking, directions, and social media.</p>',
        'privacy lede',
    )
    page = replace_once(
        page,
        '<p>The current BoPeeps website does not claim to run a separate advertising tracker, mailing-list signup, or first-party analytics platform. Third-party services may use their own cookies or similar technologies when their content or booking tools are loaded.</p>',
        '<p>This website does not currently use a BoPeeps mailing-list signup or a separate first-party analytics or advertising platform. Third-party services may use their own cookies or similar technologies when their content or booking tools are loaded.</p>',
        'privacy tracking paragraph',
    )
    write(name, page)


LOCAL_PAGES = {
    'auto-detailing-hayesville-nc.html': {
        'meta': 'Visit BoPeeps Details & More for auto detailing in Hayesville, NC. View current package pricing, shop information, directions, and Booksy booking.',
        'social': 'Auto detailing at the BoPeeps Hayesville shop, with current pricing, directions, and online booking.',
        'city': 'Hayesville, NC',
        'lede': 'BoPeeps Details & More provides professional auto detailing from our Hayesville shop on US-64, serving Clay County, the Lake Chatuge area, and customers who make the drive from beyond.',
        'heading': 'Detailing in Hayesville and Clay County',
        'body': 'Whether you are nearby in Hayesville or coming in from around the Lake Chatuge area, you can compare our packages, book online through Booksy, or call if you need help choosing the right service for a larger or specialty vehicle.',
        'before': 'Service prices reflect standard vehicle conditions. Excessive pet hair requiring additional removal time may incur a $20 pet hair removal fee. If you have an RV, work vehicle, trailer, PWC, or another specialty vehicle, call before booking if you are unsure which option fits.',
    },
    'auto-detailing-murphy-nc.html': {
        'meta': 'Looking for auto detailing near Murphy, NC? BoPeeps welcomes Murphy and Cherokee County customers at our Hayesville shop. See pricing, directions, and booking.',
        'social': 'BoPeeps welcomes Murphy and Cherokee County customers for detailing at our Hayesville shop. See pricing, directions, and online booking.',
        'city': 'Murphy, NC',
        'lede': 'Looking for professional auto detailing near Murphy? BoPeeps Details & More welcomes Murphy and Cherokee County customers at our Hayesville shop on US-64.',
        'heading': 'Detailing for Murphy-area customers',
        'body': 'If you are coming from Murphy or elsewhere in Cherokee County, you can compare our current packages, book online through Booksy, or call with questions about trucks, RVs, trailers, and other specialty vehicles.',
        'before': 'Service prices reflect standard vehicle conditions. Excessive pet hair requiring additional removal time may incur a $20 pet hair removal fee. If you are bringing an unusually large or specialty vehicle, call before booking so we can help you choose the right option.',
    },
    'auto-detailing-hiawassee-ga.html': {
        'meta': 'Looking for auto detailing near Hiawassee, GA? BoPeeps welcomes Towns County and Lake Chatuge-area customers at our Hayesville shop. See pricing and booking.',
        'social': 'BoPeeps welcomes Hiawassee, Towns County, and Lake Chatuge-area customers for detailing at our Hayesville shop.',
        'city': 'Hiawassee, GA',
        'lede': 'Looking for professional auto detailing near Hiawassee? BoPeeps Details & More welcomes Towns County and Lake Chatuge-area customers at our Hayesville shop.',
        'heading': 'Detailing for Hiawassee-area customers',
        'body': 'Cars, SUVs, trucks, RVs, PWCs, work vehicles, and trailers are all welcome. Compare our current packages, book online through Booksy, or call if you need help matching a larger vehicle to the right service.',
        'before': 'Service prices reflect standard vehicle conditions. Excessive pet hair requiring additional removal time may incur a $20 pet hair removal fee. For RVs, PWCs, trailers, or other specialty vehicles, call before booking if you are unsure which option applies.',
    },
    'auto-detailing-young-harris-ga.html': {
        'meta': 'Looking for auto detailing near Young Harris, GA? BoPeeps welcomes Towns County customers at our Hayesville shop. Compare pricing, get directions, and book online.',
        'social': 'BoPeeps welcomes Young Harris and Towns County customers for detailing at our Hayesville shop. See pricing, directions, and booking.',
        'city': 'Young Harris, GA',
        'lede': 'Looking for professional auto detailing near Young Harris? BoPeeps Details & More welcomes Young Harris and Towns County customers at our Hayesville shop.',
        'heading': 'Detailing for Young Harris-area customers',
        'body': 'Compare our detailing packages, book online through Booksy, or call if you have questions about a truck, RV, trailer, work vehicle, or another specialty vehicle.',
        'before': 'Service prices reflect standard vehicle conditions. Excessive pet hair requiring additional removal time may incur a $20 pet hair removal fee. If your vehicle is larger or unusual, call before booking so we can help you choose the appropriate service.',
    },
    'auto-detailing-blairsville-ga.html': {
        'meta': 'Looking for auto detailing near Blairsville, GA? BoPeeps welcomes Union County customers at our Hayesville shop. Compare package pricing, directions, and booking.',
        'social': 'BoPeeps welcomes Blairsville and Union County customers for detailing at our Hayesville shop. See pricing, directions, and online booking.',
        'city': 'Blairsville, GA',
        'lede': 'Looking for professional auto detailing near Blairsville? BoPeeps Details & More welcomes Blairsville and Union County customers at our Hayesville shop.',
        'heading': 'Detailing for Blairsville-area customers',
        'body': 'From daily drivers and SUVs to trucks, RVs, trailers, and work vehicles, you can compare our packages, book online through Booksy, or call if you need help choosing the right service.',
        'before': 'Service prices reflect standard vehicle conditions. Excessive pet hair requiring additional removal time may incur a $20 pet hair removal fee. If you are bringing an RV, trailer, PWC, or another specialty vehicle, call before booking when you need help matching it to a service.',
    },
}


SERVICE_OPTIONS = '''<article class="seo-card"><h2>Current detailing options</h2><ul><li><strong>Vacuum, Hand Wash &amp; Wax</strong> — small cars $60; SUVs &amp; trucks $75; dual/tandem axles $90</li><li><strong>Deluxe Detail Package</strong> — small cars $85; SUVs &amp; trucks $100; dual/tandem axles $120</li><li><strong>BoPeeps Signature Detail</strong> — small cars $150; SUVs &amp; trucks $200; dual/tandem axles $250</li></ul><p><a class="text-link" href="services.html">Compare all current services →</a></p></article>'''

SHOP_INFO = '''<article class="seo-card"><h2>Shop information</h2><div class="seo-facts"><div class="seo-fact"><strong>Address</strong><span>1516 US-64, Hayesville, NC 28904</span></div><div class="seo-fact"><strong>Phone</strong><span>980-598-1864</span></div><div class="seo-fact"><strong>Hours</strong><span>Monday–Saturday · 7:00 AM–5:00 PM<br>Sunday · Closed</span></div></div></article>'''


def area_links(current: str) -> str:
    items = [
        ('auto-detailing-hayesville-nc.html', 'Hayesville, NC'),
        ('auto-detailing-murphy-nc.html', 'Murphy, NC'),
        ('auto-detailing-hiawassee-ga.html', 'Hiawassee, GA'),
        ('auto-detailing-young-harris-ga.html', 'Young Harris, GA'),
        ('auto-detailing-blairsville-ga.html', 'Blairsville, GA'),
    ]
    links = []
    for href, label in items:
        current_attr = ' aria-current="page"' if href == current else ''
        links.append(f'<a href="{href}"{current_attr}>{label}</a>')
    return ''.join(links)


def local_main(filename: str, data: dict[str, str]) -> str:
    links = area_links(filename)
    return f'''<main id="main" class="seo-page-main">
    <section class="seo-hero"><div class="shell"><p class="eyebrow">BoPeeps Details & More · Hayesville, NC</p><h1>Auto Detailing {'in' if filename == 'auto-detailing-hayesville-nc.html' else 'for'} <span>{data['city']}</span></h1><p class="lede">{data['lede']}</p></div></section>
    <section class="seo-shell-section"><div class="shell">
      <div class="seo-shop-banner"><strong>Your appointment is at BoPeeps in Hayesville.</strong> All detailing is completed at {SHOP_ADDRESS}.</div>
      <div class="seo-grid two" style="margin-top:18px"><article class="seo-card"><h2>{data['heading']}</h2><p>{data['body']}</p><p><a class="text-link" href="{MAPS_DIRECTIONS}" target="_blank" rel="noopener">Get Directions</a></p></article>{SERVICE_OPTIONS}</div>
      <div class="seo-grid two" style="margin-top:18px">{SHOP_INFO}<article class="seo-card"><h2>Before your appointment</h2><p>{data['before']}</p><p><a class="text-link" href="policies.html">View policies →</a></p></article></div>
      <div class="seo-card" style="margin-top:18px"><h2>Nearby communities</h2><p>Coming from another nearby town? Use the links below for local information, or simply get directions from wherever you are. BoPeeps welcomes customers from anywhere.</p><div class="seo-area-links">{links}</div></div>
      <div class="seo-actions"><a class="button button-primary" data-booksy-open href="{BOOKSY}" target="_blank" rel="noopener">Book on Booksy</a><a class="button button-outline" href="{MAPS_DIRECTIONS}" target="_blank" rel="noopener">Get Directions</a><a class="button button-outline" href="index.html#contact">Contact BoPeeps</a></div>
    </div></section>
  </main>'''


def patch_local_pages() -> None:
    for name, data in LOCAL_PAGES.items():
        page = read(name)
        page = set_descriptions(page, data['meta'], data['social'])
        page = replace_regex_once(
            page,
            r'<main id="main" class="seo-page-main">.*?</main>',
            local_main(name, data),
            f'{name} main content',
        )
        write(name, page)


def patch_existing_tests() -> None:
    name = 'tests/test_local_seo_expansion.py'
    tests = read(name)
    tests = replace_once(tests, "assert 'Current BoPeeps services' in home", "assert 'Detailing packages' in home", 'service copy regression')
    tests = replace_once(
        tests,
        "for proof in ['Real Hayesville shop', 'Clear package pricing', 'Book online', 'Real local work']:",
        "for proof in ['Hayesville Location', 'Clear package pricing', 'Book online', 'Quality Detailing']:",
        'homepage proof regression',
    )
    tests = replace_regex_once(
        tests,
        r'def test_local_pages_have_distinct_context_and_directions\(\):.*?\n\ndef test_indexable_routes_have_unique_complete_metadata_and_one_h1\(\):',
        '''def test_local_pages_have_distinct_context_and_directions():
    requirements = {
        'auto-detailing-hayesville-nc.html': ['Clay County'],
        'auto-detailing-murphy-nc.html': ['Cherokee County'],
        'auto-detailing-hiawassee-ga.html': ['Towns County', 'Lake Chatuge'],
        'auto-detailing-young-harris-ga.html': ['Towns County'],
        'auto-detailing-blairsville-ga.html': ['Union County'],
    }
    destination = 'destination=1516%20US-64%2C%20Hayesville%2C%20NC%2028904'
    for name, markers in requirements.items():
        page = html(name)
        for marker in markers:
            assert marker in page, f'{name}: {marker}'
        assert 'https://www.google.com/maps/dir/?api=1' in page, name
        assert 'origin=' not in page, name
        assert destination in page, name
        assert '>Get Directions<' in page, name


def test_indexable_routes_have_unique_complete_metadata_and_one_h1():''',
        'local directions regression',
    )
    tests = replace_regex_once(
        tests,
        r'def test_local_pages_are_truthful_about_one_hayesville_shop\(\):.*?\n\ndef test_all_local_schema_keeps_hayesville_as_the_only_street_location\(\):',
        '''def test_local_pages_are_truthful_about_one_hayesville_shop():
    surrounding = {
        'auto-detailing-murphy-nc.html': 'Murphy',
        'auto-detailing-hiawassee-ga.html': 'Hiawassee',
        'auto-detailing-young-harris-ga.html': 'Young Harris',
        'auto-detailing-blairsville-ga.html': 'Blairsville',
    }
    for name in LOCAL_PAGES:
        page = html(name)
        assert SHOP_ADDRESS in page
        assert PHONE in page
        assert 'Hayesville' in page
        assert BOOKSY in page
        lower = page.lower()
        assert 'mobile detailing available' not in lower
        assert 'we come to you' not in lower
    for name, city in surrounding.items():
        page = html(name)
        assert city in page
        assert 'Your appointment is at BoPeeps in Hayesville.' in page


def test_all_local_schema_keeps_hayesville_as_the_only_street_location():''',
        'one-shop truth regression',
    )
    tests = replace_once(
        tests,
        "assert 'all appointments are completed at our hayesville shop' in home.lower()",
        "assert 'all detailing is completed at our hayesville shop' in home.lower()",
        'homepage location regression',
    )
    write(name, tests)

    name = 'tests/test_pet_hair_policy.py'
    tests = read(name)
    tests = replace_regex_once(
        tests,
        r'def test_policy_page_explains_threshold_line_item_and_scope\(\):.*',
        '''def test_policy_page_explains_threshold_line_item_and_scope():
    policies = POLICIES_PATH.read_text(encoding="utf-8")
    assert "Pricing & Vehicle Condition Policy" in policies
    assert "Standard pricing" in policies
    assert "When the pet-hair fee applies" in policies
    assert "At checkout" in policies
    assert "A few stray hairs are not the intended threshold." in policies
    assert "$20 Excessive Pet Hair Removal" in policies
    assert "Booksy handles appointment availability and checkout." in policies
    assert 'href="privacy.html"' in policies
    assert 'href="index.html"' in policies
''',
        'pet hair policy regression',
    )
    write(name, tests)


def main() -> None:
    patch_homepage()
    patch_services()
    patch_policies()
    patch_privacy()
    patch_local_pages()
    patch_existing_tests()


if __name__ == '__main__':
    main()
