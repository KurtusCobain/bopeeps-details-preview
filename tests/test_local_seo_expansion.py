from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path('.')
BOOKSY = 'https://booksy.com/en-us/1808686_bopeeps-detail-more_other_26564_hayesville'
BOOKSY_WIDGET = 'https://booksy.com/widget/code.js?id=1808686&country=us&lang=en'
FACEBOOK = 'https://www.facebook.com/people/BoPeeps-Detail/61591634832181/'
SHOP_ADDRESS = '1516 US-64, Hayesville, NC 28904'
PHONE = '980-598-1864'
PHONE_HREF = 'tel:+19805981864'
EMAIL = 'hello@bopeepsdetails.com'
BUSINESS_NAME = 'BoPeeps Details & More'
CANONICAL_BASE = 'https://bopeepsdetails.com'
FORMER_PHONE_PARTS = [
    ('706', '897', '6177'),
    ('850', '348', '5791'),
]
TEXT_SUFFIXES = {'.html', '.md', '.py', '.js', '.css', '.txt', '.xml'}

INDEXABLE = [
    'index.html',
    'services.html',
    'auto-detailing-hayesville-nc.html',
    'auto-detailing-murphy-nc.html',
    'auto-detailing-hiawassee-ga.html',
    'auto-detailing-young-harris-ga.html',
    'auto-detailing-blairsville-ga.html',
    'policies.html',
    'privacy.html',
]

PUBLIC_PAGES = INDEXABLE + ['404.html']

LOCAL_PAGES = [
    'auto-detailing-hayesville-nc.html',
    'auto-detailing-murphy-nc.html',
    'auto-detailing-hiawassee-ga.html',
    'auto-detailing-young-harris-ga.html',
    'auto-detailing-blairsville-ga.html',
]

SCHEMA_PAGES = ['index.html', 'services.html', *LOCAL_PAGES, 'policies.html']

EXPECTED_CANONICALS = {
    'index.html': f'{CANONICAL_BASE}/',
    **{name: f'{CANONICAL_BASE}/{name}' for name in INDEXABLE if name != 'index.html'},
}


class AuditParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.headings = []
        self.links = []
        self.images = []
        self.asset_refs = []
        self.meta_names = {}
        self.meta_properties = {}
        self.canonical = None
        self._scrub_choice_depth = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = set(attrs.get('class', '').split())

        if tag == 'button' and 'scrub-choice' in classes:
            self._scrub_choice_depth += 1

        if 'id' in attrs:
            self.ids.append(attrs['id'])

        if re.fullmatch(r'h[1-6]', tag):
            self.headings.append(int(tag[1]))

        if tag == 'a' and attrs.get('href'):
            self.links.append(attrs['href'])

        if tag == 'img':
            self.images.append({
                'attrs': attrs,
                'decorative_scrub_thumbnail': self._scrub_choice_depth > 0,
            })
            if attrs.get('src'):
                self.asset_refs.append(attrs['src'])
            if attrs.get('srcset'):
                self.asset_refs.extend(srcset_urls(attrs['srcset']))

        if tag == 'source' and attrs.get('srcset'):
            self.asset_refs.extend(srcset_urls(attrs['srcset']))

        if tag == 'script' and attrs.get('src'):
            self.asset_refs.append(attrs['src'])

        if tag == 'link' and attrs.get('href'):
            rel = set(attrs.get('rel', '').split())
            if 'canonical' in rel:
                self.canonical = attrs['href']
            if rel & {'stylesheet', 'icon', 'apple-touch-icon'}:
                self.asset_refs.append(attrs['href'])

        if tag == 'meta' and attrs.get('content') is not None:
            if attrs.get('name'):
                self.meta_names[attrs['name'].lower()] = attrs['content']
            if attrs.get('property'):
                self.meta_properties[attrs['property'].lower()] = attrs['content']

    def handle_endtag(self, tag):
        if tag == 'button' and self._scrub_choice_depth:
            self._scrub_choice_depth -= 1


def html(name: str) -> str:
    return (ROOT / name).read_text(encoding='utf-8')


def parse_page(name: str) -> AuditParser:
    parser = AuditParser()
    parser.feed(html(name))
    return parser


def extract(pattern: str, text: str) -> str:
    match = re.search(pattern, text, flags=re.I | re.S)
    assert match, f'missing pattern: {pattern}'
    return re.sub(r'\s+', ' ', match.group(1)).strip()


def srcset_urls(value: str) -> list[str]:
    urls = []
    for item in value.split(','):
        item = item.strip()
        if item:
            urls.append(item.split()[0])
    return urls


def local_path(url: str) -> Path | None:
    if not url or url.startswith(('#', 'data:', 'mailto:', 'tel:', '//')):
        return None
    parts = urlsplit(url)
    if parts.scheme or parts.netloc:
        return None
    path = parts.path.lstrip('/')
    if not path:
        return None
    return ROOT / path


def former_phone_variants(parts: tuple[str, str, str]) -> set[str]:
    area, prefix, line = parts
    digits = f'{area}{prefix}{line}'
    dashed = f'{area}-{prefix}-{line}'
    return {
        dashed,
        digits,
        f'+1{digits}',
        f'+1-{dashed}',
        f'tel:+1{digits}',
    }


def all_former_phone_variants() -> set[str]:
    return {
        variant
        for parts in FORMER_PHONE_PARTS
        for variant in former_phone_variants(parts)
    }


def json_ld_objects(name: str) -> list[dict]:
    blocks = re.findall(
        r'<script\s+type="application/ld\+json">(.*?)</script>',
        html(name),
        flags=re.I | re.S,
    )
    return [json.loads(block.strip()) for block in blocks]


def test_required_routes_exist():
    for name in INDEXABLE + ['404.html', 'robots.txt', 'sitemap.xml', 'seo-pages.css']:
        assert (ROOT / name).exists(), name


def test_storefront_and_favicon_assets_exist():
    for name in [
        'assets-v3/hero-storefront-desktop.webp',
        'assets-v3/hero-storefront-mobile.webp',
        'favicon-48.png',
        'apple-touch-icon.png',
        'favicon.ico',
    ]:
        path = ROOT / name
        assert path.exists(), name
        assert path.stat().st_size > 0, name


def test_every_public_page_declares_the_favicon():
    icon_pattern = r'<link\s+rel="icon"\s+type="image/png"\s+sizes="48x48"\s+href="favicon-48\.png"\s*/?>'
    apple_pattern = r'<link\s+rel="apple-touch-icon"\s+sizes="180x180"\s+href="apple-touch-icon\.png"\s*/?>'
    for name in PUBLIC_PAGES:
        text = html(name)
        assert re.search(icon_pattern, text, flags=re.I), name
        assert re.search(apple_pattern, text, flags=re.I), name


def test_all_public_pages_use_current_phone_number():
    forbidden = all_former_phone_variants()
    for name in PUBLIC_PAGES:
        text = html(name)
        for variant in forbidden:
            assert variant not in text, f'{name}: {variant}'
        assert PHONE_HREF in text, name

    for name in ['index.html', 'services.html'] + LOCAL_PAGES + ['privacy.html']:
        assert PHONE in html(name), name


def test_repository_text_has_no_obsolete_phone_numbers():
    forbidden = all_former_phone_variants()
    for path in ROOT.rglob('*'):
        if not path.is_file() or '.git' in path.parts or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = path.read_text(encoding='utf-8')
        for variant in forbidden:
            assert variant not in text, f'{path}: {variant}'


def test_current_service_copy_uses_website_names():
    home = html('index.html')
    services = html('services.html')
    local_pages = '\n'.join(html(name) for name in LOCAL_PAGES)

    assert 'Current BoPeeps services' in home
    assert 'Current Booksy services' not in home
    assert "RV's" not in home
    assert '<span>RVs</span>' in home
    assert 'Book Basic' not in services
    assert 'Book Wash &amp; Wax' in services
    assert 'Basic, Deluxe, and Signature' not in local_pages


def test_homepage_conversion_section_order_and_proof_copy():
    home = html('index.html')
    markers = [
        '<section class="hero" id="top">',
        '<section class="trust-strip"',
        '<section class="section services-section" id="services">',
        '<div class="gallery-grid"',
        'data-scrub-stage',
        '<section class="section about-section" id="about">',
        '<section class="section home-service-area"',
        '<section class="section contact-section" id="contact">',
    ]
    positions = [home.index(marker) for marker in markers]
    assert positions == sorted(positions)

    for proof in ['Real Hayesville shop', 'Clear package pricing', 'Book online', 'Real local work']:
        assert proof in home
    for old_label in ['Quality products', 'Attention to detail', 'Reliable service', 'Customer first']:
        assert old_label not in home


def test_local_pages_have_distinct_context_and_directions():
    requirements = {
        'auto-detailing-hayesville-nc.html': {
            'markers': ['Clay County', 'Lake Chatuge'],
            'origin': 'origin=Hayesville%2C%20NC',
        },
        'auto-detailing-murphy-nc.html': {
            'markers': ['Cherokee County', 'Appalachian'],
            'origin': 'origin=Murphy%2C%20NC',
        },
        'auto-detailing-hiawassee-ga.html': {
            'markers': ['Towns County', 'Lake Chatuge', 'PWCs'],
            'origin': 'origin=Hiawassee%2C%20GA',
        },
        'auto-detailing-young-harris-ga.html': {
            'markers': ['Towns County', 'Young Harris College'],
            'origin': 'origin=Young%20Harris%2C%20GA',
        },
        'auto-detailing-blairsville-ga.html': {
            'markers': ['Union County', 'north Georgia'],
            'origin': 'origin=Blairsville%2C%20GA',
        },
    }
    destination = 'destination=1516%20US-64%2C%20Hayesville%2C%20NC%2028904'
    for name, expected in requirements.items():
        text = html(name)
        for marker in expected['markers']:
            assert marker in text, f'{name}: {marker}'
        assert 'https://www.google.com/maps/dir/?api=1' in text, name
        assert expected['origin'] in text, name
        assert destination in text, name


def test_indexable_routes_have_unique_complete_metadata_and_one_h1():
    titles = []
    descriptions = []
    og_titles = []
    og_descriptions = []
    canonicals = []

    for name in INDEXABLE:
        text = html(name)
        parser = parse_page(name)
        title = extract(r'<title>(.*?)</title>', text)
        description = parser.meta_names.get('description', '').strip()
        canonical = parser.canonical
        og_title = parser.meta_properties.get('og:title', '').strip()
        og_description = parser.meta_properties.get('og:description', '').strip()
        og_url = parser.meta_properties.get('og:url', '').strip()

        assert title, name
        assert description, name
        assert canonical == EXPECTED_CANONICALS[name], name
        assert og_title == title, name
        assert og_description, name
        assert og_url == canonical, name
        assert parser.headings.count(1) == 1, name

        titles.append(title)
        descriptions.append(description)
        og_titles.append(og_title)
        og_descriptions.append(og_description)
        canonicals.append(canonical)

    assert len(titles) == len(set(titles))
    assert len(descriptions) == len(set(descriptions))
    assert len(og_titles) == len(set(og_titles))
    assert len(og_descriptions) == len(set(og_descriptions))
    assert len(canonicals) == len(set(canonicals))


def test_public_page_internal_links_and_fragments_resolve():
    parsed = {name: parse_page(name) for name in PUBLIC_PAGES}

    for source_name, parser in parsed.items():
        for href in parser.links:
            parts = urlsplit(href)
            if parts.scheme or parts.netloc or href.startswith(('mailto:', 'tel:', '//')):
                continue

            target_name = parts.path or source_name
            if parts.path:
                target_path = ROOT / parts.path.lstrip('/')
                assert target_path.exists(), f'{source_name}: {href}'
                if target_path.suffix.lower() != '.html':
                    continue
            else:
                target_path = ROOT / source_name

            if parts.fragment:
                target_parser = parsed.get(target_path.name)
                if target_parser is None:
                    target_parser = parse_page(target_path.name)
                assert parts.fragment in target_parser.ids, f'{source_name}: {href}'


def test_public_pages_have_unique_ids_and_valid_heading_progression():
    for name in PUBLIC_PAGES:
        parser = parse_page(name)
        assert len(parser.ids) == len(set(parser.ids)), name

        for previous, current in zip(parser.headings, parser.headings[1:]):
            assert current <= previous + 1, f'{name}: h{previous} -> h{current}'


def test_public_images_have_dimensions_alt_text_and_existing_local_assets():
    for name in PUBLIC_PAGES:
        parser = parse_page(name)

        for image in parser.images:
            attrs = image['attrs']
            assert 'alt' in attrs, f'{name}: {attrs.get("src")}'
            assert attrs.get('width', '').isdigit() and int(attrs['width']) > 0, f'{name}: {attrs.get("src")}'
            assert attrs.get('height', '').isdigit() and int(attrs['height']) > 0, f'{name}: {attrs.get("src")}'
            if attrs.get('alt') == '':
                assert image['decorative_scrub_thumbnail'], f'{name}: {attrs.get("src")}'

        for ref in parser.asset_refs:
            path = local_path(ref)
            if path is not None:
                assert path.exists(), f'{name}: {ref}'


def test_stylesheet_local_url_assets_exist():
    for css_name in ['styles-v3.css', 'seo-pages.css']:
        text = (ROOT / css_name).read_text(encoding='utf-8')
        for ref in re.findall(r'url\(["\']?([^"\')]+)', text):
            path = local_path(ref.strip())
            if path is not None:
                assert path.exists(), f'{css_name}: {ref}'


def test_public_business_booking_and_social_references_are_consistent():
    for name in PUBLIC_PAGES:
        text = html(name)
        parser = parse_page(name)

        assert 'Jacky Jones' not in text, name
        assert 'BoPeePs Details' not in text, name
        assert 'Bopeeps Details & More' not in text, name

        for href in parser.links:
            if href.startswith('tel:'):
                assert href == PHONE_HREF, f'{name}: {href}'
            if href.startswith('mailto:'):
                assert href == f'mailto:{EMAIL}', f'{name}: {href}'
            if href.startswith('https://www.facebook.com/'):
                assert href == FACEBOOK, f'{name}: {href}'
            if href.startswith('https://booksy.com/'):
                assert href == BOOKSY, f'{name}: {href}'

        for ref in parser.asset_refs:
            if ref.startswith('https://booksy.com/'):
                assert ref == BOOKSY_WIDGET, f'{name}: {ref}'


def test_local_business_schema_uses_one_current_business_entity():
    expected_areas = {'Hayesville', 'Murphy', 'Hiawassee', 'Young Harris', 'Blairsville'}

    for name in SCHEMA_PAGES:
        objects = json_ld_objects(name)
        matching = []
        for obj in objects:
            types = obj.get('@type', [])
            if isinstance(types, str):
                types = [types]
            if {'AutomotiveBusiness', 'LocalBusiness'} & set(types):
                matching.append(obj)

        assert len(matching) == 1, name
        entity = matching[0]
        address = entity['address']
        areas = {item['name'] for item in entity.get('areaServed', [])}

        assert entity['name'] == BUSINESS_NAME, name
        assert entity['url'] == f'{CANONICAL_BASE}/', name
        assert entity['telephone'] == '+1-980-598-1864', name
        assert entity['email'] == EMAIL, name
        assert address['streetAddress'] == '1516 US-64', name
        assert address['addressLocality'] == 'Hayesville', name
        assert address['addressRegion'] == 'NC', name
        assert address['postalCode'] == '28904', name
        assert areas == expected_areas, name
        assert entity.get('sameAs') == [FACEBOOK], name
        assert entity['potentialAction']['target'] == BOOKSY, name


def test_local_pages_are_truthful_about_one_hayesville_shop():
    surrounding = {
        'auto-detailing-murphy-nc.html': 'Murphy',
        'auto-detailing-hiawassee-ga.html': 'Hiawassee',
        'auto-detailing-young-harris-ga.html': 'Young Harris',
        'auto-detailing-blairsville-ga.html': 'Blairsville',
    }
    for name in LOCAL_PAGES:
        text = html(name)
        assert SHOP_ADDRESS in text
        assert PHONE in text
        assert 'Hayesville' in text
        assert BOOKSY in text
        lower = text.lower()
        assert 'mobile detailing available' not in lower
        assert 'we come to you' not in lower
    for name, city in surrounding.items():
        text = html(name).lower()
        assert city.lower() in text
        assert 'hayesville shop' in text
        assert ('bring your vehicle' in text) or ('bring their vehicles' in text) or ('bring the vehicle' in text)


def test_all_local_schema_keeps_hayesville_as_the_only_street_location():
    forbidden_location_fragments = [
        'Murphy, NC 28906',
        'Hiawassee, GA 30546',
        'Young Harris, GA 30582',
        'Blairsville, GA 30512',
    ]
    for name in LOCAL_PAGES:
        text = html(name)
        assert '"streetAddress":"1516 US-64"' in text or '"streetAddress": "1516 US-64"' in text
        assert '"addressLocality":"Hayesville"' in text or '"addressLocality": "Hayesville"' in text
        for fragment in forbidden_location_fragments:
            assert fragment not in text


def test_sitemap_has_exactly_nine_indexable_urls():
    tree = ET.parse(ROOT / 'sitemap.xml')
    ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    locs = [node.text.strip() for node in tree.findall('.//sm:loc', ns)]
    assert len(locs) == 9
    assert set(locs) == set(EXPECTED_CANONICALS.values())
    joined = '\n'.join(locs)
    assert '404.html' not in joined
    assert '/docs/' not in joined
    assert '/tests/' not in joined
    assert 'dev/' not in joined


def test_robots_advertises_production_sitemap():
    robots = (ROOT / 'robots.txt').read_text(encoding='utf-8')
    assert 'User-agent: *' in robots
    assert 'Allow: /' in robots
    assert f'Sitemap: {CANONICAL_BASE}/sitemap.xml' in robots


def test_booksy_and_pet_hair_policy_are_preserved():
    home = html('index.html')
    services = html('services.html')
    policies = html('policies.html')
    for text in [home, services, policies]:
        assert BOOKSY in text
    approved = 'Excessive pet hair requiring additional removal time'
    assert approved in home
    assert approved in services
    assert approved in policies


def test_public_pages_use_signature_service_name_and_current_vehicle_pricing():
    for name in INDEXABLE:
        text = html(name)
        assert 'jacky' not in text.lower(), name
        assert '>Premium Detail<' not in text, name

    home = html('index.html')
    services = html('services.html')
    local_pages = '\n'.join(html(name) for name in LOCAL_PAGES)

    assert 'BoPeeps Signature Detail' in home
    assert 'BoPeeps Signature Detail' in services
    assert 'BoPeeps Signature Detail' in local_pages

    for text in [home, services]:
        for amount in ['$60', '$75', '$90', '$85', '$100', '$120', '$150', '$200', '$250']:
            assert amount in text
        assert 'Small cars' in text
        assert 'SUVs &amp; trucks' in text
        assert 'Dual/tandem axles' in text

    for duration in ['~1 hr', '~2 hrs', '~4 hrs']:
        assert duration not in home
        assert duration not in services


def test_homepage_exposes_crawlable_core_and_service_area_links():
    home = html('index.html')
    required = [
        'services.html',
        'policies.html',
        'privacy.html',
        'auto-detailing-hayesville-nc.html',
        'auto-detailing-murphy-nc.html',
        'auto-detailing-hiawassee-ga.html',
        'auto-detailing-young-harris-ga.html',
        'auto-detailing-blairsville-ga.html',
    ]
    for href in required:
        assert f'href="{href}"' in home
    assert 'all appointments are completed at our hayesville shop' in home.lower()


def test_404_is_noindex_and_not_a_fake_success_page():
    text = html('404.html')
    assert '<meta name="robots" content="noindex,nofollow"' in text
    assert 'Page Not Found' in text
    assert 'services.html' in text
    assert BOOKSY in text
