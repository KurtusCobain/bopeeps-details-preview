from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path('.')
BOOKSY = 'https://booksy.com/en-us/1808686_bopeeps-detail-more_other_26564_hayesville'
SHOP_ADDRESS = '1516 US-64, Hayesville, NC 28904'
PHONE = '706-897-6177'
CANONICAL_BASE = 'https://bopeepsdetails.com'

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

LOCAL_PAGES = [
    'auto-detailing-hayesville-nc.html',
    'auto-detailing-murphy-nc.html',
    'auto-detailing-hiawassee-ga.html',
    'auto-detailing-young-harris-ga.html',
    'auto-detailing-blairsville-ga.html',
]

EXPECTED_CANONICALS = {
    'index.html': f'{CANONICAL_BASE}/',
    **{name: f'{CANONICAL_BASE}/{name}' for name in INDEXABLE if name != 'index.html'},
}


def html(name: str) -> str:
    return (ROOT / name).read_text(encoding='utf-8')


def extract(pattern: str, text: str) -> str:
    match = re.search(pattern, text, flags=re.I | re.S)
    assert match, f'missing pattern: {pattern}'
    return re.sub(r'\s+', ' ', match.group(1)).strip()


def test_required_routes_exist():
    for name in INDEXABLE + ['404.html', 'robots.txt', 'sitemap.xml', 'seo-pages.css']:
        assert (ROOT / name).exists(), name


def test_indexable_routes_have_unique_core_metadata_and_one_h1():
    titles = []
    descriptions = []
    canonicals = []
    for name in INDEXABLE:
        text = html(name)
        title = extract(r'<title>(.*?)</title>', text)
        description = extract(r'<meta\s+name="description"\s+content="([^"]+)"', text)
        canonical = extract(r'<link\s+rel="canonical"\s+href="([^"]+)"', text)
        assert canonical == EXPECTED_CANONICALS[name]
        assert len(re.findall(r'<h1(?:\s|>)', text, flags=re.I)) == 1, name
        titles.append(title)
        descriptions.append(description)
        canonicals.append(canonical)
    assert len(titles) == len(set(titles))
    assert len(descriptions) == len(set(descriptions))
    assert len(canonicals) == len(set(canonicals))


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
