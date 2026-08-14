from pathlib import Path
import json
import re

ROOT = Path('.')

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
PUBLIC = INDEXABLE + ['404.html']
SCHEMA_PAGES = ['index.html', 'services.html', *INDEXABLE[2:7], 'policies.html']

BOOKSY_WIDGET = 'https://booksy.com/widget/code.js?id=1808686'
REQUIRED_SCHEMA_KEYS = {
    'name', 'url', 'description', 'telephone', 'email', 'address',
    'openingHoursSpecification', 'areaServed', 'sameAs', 'image', 'logo',
    'priceRange', 'potentialAction',
}


def text(name: str) -> str:
    return (ROOT / name).read_text(encoding='utf-8')


def schema(name: str) -> dict:
    match = re.search(
        r'<script\s+type="application/ld\+json">(.*?)</script>',
        text(name),
        flags=re.I | re.S,
    )
    assert match, name
    return json.loads(match.group(1))


def test_public_pages_use_new_javascript_cache_token_and_lazy_booksy_host():
    for name in PUBLIC:
        page = text(name)
        assert 'script-v3.js?v=20260814a' in page, name
        assert 'script-v3.js?v=20260808' not in page, name
        assert 'data-booksy-widget-src=' in page, name
        assert f'<script type="text/javascript" src="{BOOKSY_WIDGET}' not in page, name

    javascript = text('script-v3.js')
    assert "document.createElement('script')" in javascript
    assert 'dataset.booksyWidgetSrc' in javascript


def test_business_schema_is_normalized_across_all_schema_pages():
    schemas = [schema(name) for name in SCHEMA_PAGES]
    for name, entity in zip(SCHEMA_PAGES, schemas):
        assert REQUIRED_SCHEMA_KEYS <= set(entity), name
        assert entity['name'] == 'BoPeeps Details & More', name
        assert entity['telephone'] == '+1-980-598-1864', name
        assert entity['email'] == 'hello@bopeepsdetails.com', name
        assert entity['address']['streetAddress'] == '1516 US-64', name
        assert entity['address']['addressLocality'] == 'Hayesville', name
        assert entity['logo'] == 'https://bopeepsdetails.com/assets/logo-modern.webp', name
        assert entity['image'] == 'https://bopeepsdetails.com/assets-v3/hero-storefront-desktop.webp', name
        assert len(entity['openingHoursSpecification']) == 1, name

    canonical = schemas[0]
    for entity in schemas[1:]:
        assert entity == canonical


def test_location_pages_do_not_expose_internal_seo_process_language():
    banned = [
        'fake branch',
        'second location that does not exist',
        'does not operate a separate',
        'without implying additional',
        'without creating fake',
    ]
    for name in INDEXABLE[2:7]:
        lower = text(name).lower()
        for phrase in banned:
            assert phrase not in lower, f'{name}: {phrase}'


def test_indexable_pages_include_complete_social_image_metadata():
    required = [
        'property="og:image:alt"',
        'property="og:image:width" content="1684"',
        'property="og:image:height" content="934"',
        'name="twitter:title"',
        'name="twitter:description"',
        'name="twitter:image"',
        'name="twitter:image:alt"',
    ]
    for name in INDEXABLE:
        page = text(name)
        for marker in required:
            assert marker in page, f'{name}: {marker}'


def test_public_pages_use_optimized_logo_and_home_uses_optimized_work_images():
    for name in PUBLIC:
        page = text(name)
        assert 'assets/logo-modern.webp' in page, name
        assert 'assets/logo-modern.jpg' not in page, name

    home = text('index.html')
    for base in [
        'gallery-exterior-care',
        'gallery-photo-8',
        'gallery-photo-14',
        'gallery-photo-21',
        'gallery-photo-25',
        'gallery-real-local-work',
        'scrub-photo-6',
        'scrub-photo-10',
        'scrub-photo-15',
        'scrub-work-vehicles',
    ]:
        assert f'assets-v3/{base}-optimized.webp' in home, base
