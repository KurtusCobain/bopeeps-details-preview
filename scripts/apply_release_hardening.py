from pathlib import Path
import html
import json
import re

ROOT = Path(__file__).resolve().parents[1]

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

BOOKSY_WIDGET = 'https://booksy.com/widget/code.js?id=1808686&country=us&lang=en'
BOOKSY_HOST = (
    '<div class="booksy-widget-host" data-booksy-widget-host '
    'data-booksy-widget-src="https://booksy.com/widget/code.js?id=1808686&amp;country=us&amp;lang=en"></div>'
)
OG_IMAGE = 'https://bopeepsdetails.com/assets-v3/hero-storefront-desktop.webp'
OG_IMAGE_ALT = 'BoPeeps Details & More storefront in Hayesville, North Carolina'

SCHEMA = {
    '@context': 'https://schema.org',
    '@type': ['AutomotiveBusiness', 'LocalBusiness'],
    '@id': 'https://bopeepsdetails.com/#business',
    'name': 'BoPeeps Details & More',
    'url': 'https://bopeepsdetails.com/',
    'description': 'Professional in-shop auto detailing in Hayesville, NC serving Hayesville, Murphy, Hiawassee, Young Harris, and Blairsville.',
    'telephone': '+1-980-598-1864',
    'email': 'hello@bopeepsdetails.com',
    'address': {
        '@type': 'PostalAddress',
        'streetAddress': '1516 US-64',
        'addressLocality': 'Hayesville',
        'addressRegion': 'NC',
        'postalCode': '28904',
        'addressCountry': 'US',
    },
    'openingHoursSpecification': [{
        '@type': 'OpeningHoursSpecification',
        'dayOfWeek': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
        'opens': '07:00',
        'closes': '17:00',
    }],
    'areaServed': [
        {'@type': 'City', 'name': 'Hayesville'},
        {'@type': 'City', 'name': 'Murphy'},
        {'@type': 'City', 'name': 'Hiawassee'},
        {'@type': 'City', 'name': 'Young Harris'},
        {'@type': 'City', 'name': 'Blairsville'},
    ],
    'sameAs': ['https://www.facebook.com/people/BoPeeps-Detail/61591634832181/'],
    'image': OG_IMAGE,
    'logo': 'https://bopeepsdetails.com/assets/logo-modern.webp',
    'priceRange': '$60+',
    'potentialAction': {
        '@type': 'ReserveAction',
        'target': 'https://booksy.com/en-us/1808686_bopeeps-detail-more_other_26564_hayesville',
    },
}

LOCATION_REPLACEMENTS = {
    'auto-detailing-hayesville-nc.html': {
        'We keep one clear location for drop-off, questions, and scheduled detailing rather than advertising mobile service.':
            'All detailing is completed on-site at the Hayesville shop, with one clear location for drop-off, questions, and scheduled service.',
        'The surrounding pages below help Murphy, Hiawassee, Young Harris, and Blairsville drivers plan service at this same location; they are not separate storefronts.':
            'The surrounding pages below help Murphy, Hiawassee, Young Harris, and Blairsville drivers plan service at this same Hayesville location.',
    },
    'auto-detailing-murphy-nc.html': {
        'We do not operate a separate Murphy storefront or mobile-detailing route.':
            'All BoPeeps detailing for Murphy-area customers is completed at the Hayesville shop.',
        'Instead of presenting a second location that does not exist, we give Murphy-area drivers the same real shop address, service menu, pricing, and booking path used across the website.':
            'Murphy-area drivers use the same Hayesville shop address, service menu, pricing, and booking path shown across the website.',
        'These pages provide city-specific information without creating fake branch locations.':
            'These pages provide directions and service information for other nearby communities.',
    },
    'auto-detailing-hiawassee-ga.html': {
        'The work is completed at the Hayesville shop; BoPeeps does not operate a separate Hiawassee storefront or mobile-detailing route.':
            'All BoPeeps detailing for Hiawassee-area customers is completed at the Hayesville shop.',
        'The surrounding pages below provide useful local context without implying additional BoPeeps locations.':
            'The surrounding pages below provide directions and service information for other nearby communities.',
    },
    'auto-detailing-young-harris-ga.html': {
        'BoPeeps does not operate a separate Young Harris storefront or mobile-detailing route.':
            'All BoPeeps detailing for Young Harris-area customers is completed at the Hayesville shop.',
        'These local pages provide useful context without suggesting additional business locations.':
            'These local pages provide directions and service information for other nearby communities.',
    },
    'auto-detailing-blairsville-ga.html': {
        'BoPeeps does not operate a Blairsville storefront or mobile-detailing route.':
            'All BoPeeps detailing for Blairsville-area customers is completed at the Hayesville shop.',
        'The pages below give each community its own useful information without creating fake branch locations.':
            'The pages below provide directions and service information for other nearby communities.',
    },
}

OPTIMIZED_HOME_REFS = [
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
]


def replace_booksy_host(page: str) -> str:
    if 'data-booksy-widget-src=' in page:
        return page
    pattern = re.compile(
        r'<div class="booksy-widget-host" data-booksy-widget-host>\s*'
        r'<script type="text/javascript" src="https://booksy\.com/widget/code\.js\?id=1808686&country=us&lang=en"></script>\s*'
        r'</div>'
    )
    updated, count = pattern.subn(BOOKSY_HOST, page)
    if count != 1:
        raise RuntimeError(f'Expected one Booksy widget host, found {count}')
    return updated


def add_social_metadata(page: str) -> str:
    if 'property="og:image:alt"' in page:
        return page
    title_match = re.search(r'<title>(.*?)</title>', page, flags=re.S)
    description_match = re.search(r'<meta property="og:description" content="([^"]+)"', page)
    if not title_match or not description_match:
        raise RuntimeError('Missing title or og:description')

    title = html.escape(html.unescape(title_match.group(1).strip()), quote=True)
    description = html.escape(html.unescape(description_match.group(1).strip()), quote=True)
    alt = html.escape(OG_IMAGE_ALT, quote=True)
    block = (
        '<meta name="twitter:card" content="summary_large_image" />\n'
        f'  <meta property="og:image:alt" content="{alt}" />\n'
        '  <meta property="og:image:width" content="1684" />\n'
        '  <meta property="og:image:height" content="934" />\n'
        f'  <meta name="twitter:title" content="{title}" />\n'
        f'  <meta name="twitter:description" content="{description}" />\n'
        f'  <meta name="twitter:image" content="{OG_IMAGE}" />\n'
        f'  <meta name="twitter:image:alt" content="{alt}" />'
    )
    updated, count = re.subn(
        r'<meta name="twitter:card" content="summary_large_image"\s*/>',
        block,
        page,
        count=1,
    )
    if count != 1:
        raise RuntimeError('Expected one twitter:card marker')
    return updated


def normalize_schema(page: str) -> str:
    block = '<script type="application/ld+json">' + json.dumps(SCHEMA, separators=(',', ':')) + '</script>'
    updated, count = re.subn(
        r'<script\s+type="application/ld\+json">.*?</script>',
        block,
        page,
        count=1,
        flags=re.S,
    )
    if count != 1:
        raise RuntimeError('Expected one LocalBusiness JSON-LD block')
    return updated


def harden_file(name: str) -> None:
    path = ROOT / name
    page = path.read_text(encoding='utf-8')

    page = re.sub(r'script-v3\.js\?v=[0-9A-Za-z]+', 'script-v3.js?v=20260814a', page)
    page = page.replace('assets/logo-modern.jpg', 'assets/logo-modern.webp')
    page = replace_booksy_host(page)

    if name in INDEXABLE:
        page = add_social_metadata(page)
    if name in SCHEMA_PAGES:
        page = normalize_schema(page)
    if name in LOCATION_REPLACEMENTS:
        for old, new in LOCATION_REPLACEMENTS[name].items():
            page = page.replace(old, new)
    if name == 'index.html':
        for base in OPTIMIZED_HOME_REFS:
            page = page.replace(f'assets-v3/{base}.webp', f'assets-v3/{base}-optimized.webp')

    path.write_text(page, encoding='utf-8')


if __name__ == '__main__':
    for filename in PUBLIC:
        harden_file(filename)
