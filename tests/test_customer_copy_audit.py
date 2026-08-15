from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

# Release-review regression guards cover customer-facing tone, concise location copy, and current-device directions.
PUBLIC = [
    'index.html',
    'services.html',
    'auto-detailing-hayesville-nc.html',
    'auto-detailing-murphy-nc.html',
    'auto-detailing-hiawassee-ga.html',
    'auto-detailing-young-harris-ga.html',
    'auto-detailing-blairsville-ga.html',
    'policies.html',
    'privacy.html',
    '404.html',
]
LOCAL = PUBLIC[2:7]
DESTINATION = '1516 US-64, Hayesville, NC 28904'
DIRECTIONS_HREF = 'https://www.google.com/maps/dir/?api=1&amp;destination=1516%20US-64%2C%20Hayesville%2C%20NC%2028904'
LOCATION_IDENTITY = 'BoPeeps Details &amp; More · 1516 US-64, Hayesville, NC 28904'


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag != 'a':
            return
        attrs = dict(attrs)
        if attrs.get('href'):
            self.links.append(attrs['href'])


def text(name: str) -> str:
    return Path(name).read_text(encoding='utf-8')


def links(name: str) -> list[str]:
    parser = LinkParser()
    parser.feed(text(name))
    return parser.links


def test_customer_pages_do_not_use_defensive_or_internal_copy():
    banned = [
        'real hayesville shop',
        'real local work',
        'genuine bopeeps photos on this site',
        'one real shop',
        'single bopeeps shop',
        'one booking flow',
        'approved surrounding service areas',
        'hard-coded mileage',
        'hard-coded drive-time',
        'fixed mileage',
        'fixed drive-time',
        'this is the bopeeps physical shop',
        'does not claim to run',
        'customers who make the drive from beyond',
    ]
    for name in PUBLIC:
        lower = text(name).lower()
        for phrase in banned:
            assert phrase not in lower, f'{name}: {phrase}'


def test_customer_copy_does_not_repeat_location_reassurance():
    banned = [
        'customers from anywhere are welcome to book',
        'customers are welcome from anywhere',
        'all detailing is completed at',
        'in-shop',
    ]
    for name in PUBLIC:
        lower = text(name).lower()
        for phrase in banned:
            assert phrase not in lower, f'{name}: {phrase}'
        assert lower.count('hayesville shop') <= 1, f'{name}: repeated Hayesville shop copy'


def test_homepage_uses_customer_first_trust_and_concise_location_copy():
    home = text('index.html')
    for phrase in [
        'Hayesville Location',
        'Conveniently located on US-64',
        'Clear package pricing',
        'Book online',
        'Quality Detailing',
        'Careful interior &amp; exterior service',
        'Recent BoPeeps Work',
    ]:
        assert phrase in home, phrase
    assert 'BoPeeps welcomes drivers from western North Carolina, north Georgia, and beyond.' in home
    assert 'Find us at 1516 US-64 in Hayesville, NC.' in home
    assert '<p class="eyebrow">Serving the region</p>' in home
    assert 'Drop off your vehicle and talk with us directly if you have questions about the service you need.' in home
    assert 'Come see us in Hayesville' not in home
    assert 'Drop off at our Hayesville location' not in home
    assert 'Customers from anywhere are welcome to book' not in home


def test_visible_location_context_is_not_repeated_before_address():
    brand_eyebrow = '<p class="eyebrow">BoPeeps Details &amp; More</p>'
    for name in ['services.html', 'privacy.html', *LOCAL]:
        assert brand_eyebrow in text(name), name

    expected_local_intros = {
        'auto-detailing-hayesville-nc.html': 'Professional auto detailing for Hayesville, Clay County, and the Lake Chatuge area.',
        'auto-detailing-murphy-nc.html': 'BoPeeps Details & More is a convenient option for Murphy and Cherokee County drivers.',
        'auto-detailing-hiawassee-ga.html': 'BoPeeps Details & More is a convenient option for Hiawassee, Towns County, and the Lake Chatuge area.',
        'auto-detailing-young-harris-ga.html': 'BoPeeps Details & More is a convenient option for Young Harris and Towns County drivers.',
        'auto-detailing-blairsville-ga.html': 'BoPeeps Details & More is a convenient option for Blairsville and Union County drivers.',
    }
    for name, phrase in expected_local_intros.items():
        assert phrase in text(name), f'{name}: {phrase}'


def test_customer_pages_use_concise_location_identity():
    for name in ['services.html', 'policies.html', *LOCAL]:
        assert LOCATION_IDENTITY in text(name), name


def test_footers_drop_in_shop_repetition():
    for name in PUBLIC:
        assert 'Professional in-shop auto detailing' not in text(name), name


def test_local_pages_use_device_location_directions():
    for name in LOCAL:
        page = text(name)
        assert '>Get Directions<' in page, name
        direction_links = [
            href for href in links(name)
            if href.startswith('https://www.google.com/maps/dir/?api=1')
        ]
        assert direction_links, name
        for href in direction_links:
            query = parse_qs(urlsplit(href).query)
            assert 'origin' not in query, f'{name}: {href}'
            assert query.get('destination') == [DESTINATION], f'{name}: {href}'


def test_mobile_direction_actions_use_device_location_on_every_public_page():
    for name in PUBLIC:
        page = text(name)
        start = page.index('<nav class="mobile-actions"')
        end = page.index('</nav>', start)
        mobile_nav = page[start:end]
        assert DIRECTIONS_HREF in mobile_nav, name
        assert 'google.com/maps/search/' not in mobile_nav, name

    home = text('index.html')
    assert f'class="map-caption" href="{DIRECTIONS_HREF}"' in home


def test_local_pages_keep_discovery_context_without_implying_branch_locations():
    required_context = {
        'auto-detailing-hayesville-nc.html': ['Clay County'],
        'auto-detailing-murphy-nc.html': ['Cherokee County'],
        'auto-detailing-hiawassee-ga.html': ['Towns County', 'Lake Chatuge'],
        'auto-detailing-young-harris-ga.html': ['Towns County'],
        'auto-detailing-blairsville-ga.html': ['Union County'],
    }
    for name, markers in required_context.items():
        page = text(name)
        lower = page.lower()
        for marker in markers:
            assert marker in page, f'{name}: {marker}'
        assert LOCATION_IDENTITY in page, name
        assert 'mobile detailing available' not in lower, name
        assert 'we come to you' not in lower, name


def test_policy_and_privacy_use_plain_customer_language():
    policies = text('policies.html')
    privacy = text('privacy.html')

    for phrase in ['Standard pricing', 'When the pet-hair fee applies', 'At checkout']:
        assert phrase in policies, phrase
    assert 'does not claim to run' not in privacy.lower()
    assert 'BoPeeps does not currently use this website for mailing-list signups' in privacy
