from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
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
MAPS_SEARCH = 'https://www.google.com/maps/search/?api=1&query=1516%20US-64%2C%20Hayesville%2C%20NC%2028904'
MAPS_DIRECTIONS = 'https://www.google.com/maps/dir/?api=1&amp;destination=1516%20US-64%2C%20Hayesville%2C%20NC%2028904'
LOCATION_IDENTITY = 'BoPeeps Details &amp; More · 1516 US-64, Hayesville, NC 28904'


def read(name: str) -> str:
    return (ROOT / name).read_text(encoding='utf-8')


def write(name: str, content: str) -> None:
    (ROOT / name).write_text(content, encoding='utf-8')


def replace_required(page: str, old: str, new: str, label: str) -> str:
    if old in page:
        return page.replace(old, new)
    if new in page:
        return page
    raise RuntimeError(f'Could not find expected copy for {label}')


def patch_mobile_directions() -> None:
    for name in PUBLIC:
        page = read(name)
        match = re.search(r'<nav class="mobile-actions".*?</nav>', page, flags=re.S)
        if not match:
            raise RuntimeError(f'Missing mobile quick actions in {name}')
        old_nav = match.group(0)
        new_nav = old_nav.replace(MAPS_SEARCH, MAPS_DIRECTIONS)
        if MAPS_DIRECTIONS not in new_nav:
            raise RuntimeError(f'Could not set device-location directions in {name}')
        page = page[:match.start()] + new_nav + page[match.end():]
        write(name, page)

    home = read('index.html')
    home = home.replace(
        f'class="map-caption" href="{MAPS_SEARCH}"',
        f'class="map-caption" href="{MAPS_DIRECTIONS}"',
    )
    if f'class="map-caption" href="{MAPS_DIRECTIONS}"' not in home:
        raise RuntimeError('Could not update homepage map directions')
    write('index.html', home)


def patch_privacy_sentence() -> None:
    name = 'privacy.html'
    page = read(name)
    old = (
        'This website does not currently use a BoPeeps mailing-list signup or a separate '
        'first-party analytics or advertising platform.'
    )
    new = (
        'BoPeeps does not currently use this website for mailing-list signups, first-party '
        'analytics, or a separate advertising platform.'
    )
    if new not in page:
        if old not in page:
            raise RuntimeError('Could not find privacy analytics sentence')
        page = page.replace(old, new, 1)
    write(name, page)


def patch_hayesville_lede() -> None:
    name = 'auto-detailing-hayesville-nc.html'
    page = read(name)
    old_options = [
        (
            'BoPeeps Details & More provides professional auto detailing from our Hayesville shop '
            'on US-64, serving Clay County, the Lake Chatuge area, and customers who make the drive '
            'from beyond.'
        ),
        (
            'BoPeeps Details & More provides professional auto detailing in Hayesville for Clay '
            'County, the Lake Chatuge area, and customers coming from farther away.'
        ),
    ]
    new = (
        'BoPeeps Details & More provides professional auto detailing in Hayesville for Clay '
        'County and the Lake Chatuge area.'
    )
    if new not in page:
        for old in old_options:
            if old in page:
                page = page.replace(old, new, 1)
                break
        else:
            raise RuntimeError('Could not find Hayesville local-page introduction')
    write(name, page)


def patch_global_location_language() -> None:
    old_schema = (
        'Professional in-shop auto detailing in Hayesville, NC serving Hayesville, Murphy, '
        'Hiawassee, Young Harris, and Blairsville.'
    )
    new_schema = 'Professional auto detailing in Hayesville, NC.'
    old_footer = 'Professional in-shop auto detailing at 1516 US-64, Hayesville, NC 28904.'
    new_footer = 'Professional auto detailing in Hayesville, North Carolina.'

    for name in PUBLIC:
        page = read(name)
        page = page.replace(old_schema, new_schema)
        page = page.replace(old_footer, new_footer)
        write(name, page)


def patch_homepage_location_copy() -> None:
    name = 'index.html'
    page = read(name)
    page = replace_required(
        page,
        'Explore BoPeeps detailing services and pricing, see recent work, and book your appointment at our Hayesville shop.',
        'Explore BoPeeps detailing services and pricing, see recent work, and book online through Booksy.',
        'homepage social description',
    )
    page = replace_required(
        page,
        '<h3>Easy in-shop service</h3><p>Drop off at our Hayesville location, ask questions directly, and know where your appointment is being handled.</p>',
        '<h3>Easy drop-off</h3><p>Drop off at our Hayesville location and talk with us directly if you have questions about your vehicle or service.</p>',
        'homepage service benefit',
    )
    page = replace_required(
        page,
        '<h2 id="service-area-title">Worth the drive from wherever you are.</h2><p>BoPeeps welcomes customers from western North Carolina, north Georgia, and beyond. Customers from anywhere are welcome to book; <strong>all detailing is completed at our Hayesville shop</strong> at 1516 US-64, Hayesville, NC 28904.</p>',
        '<h2 id="service-area-title">Detailing worth the drive.</h2><p>BoPeeps welcomes drivers from western North Carolina, north Georgia, and beyond. Find us at 1516 US-64 in Hayesville, NC.</p>',
        'homepage regional copy',
    )
    page = replace_required(
        page,
        'Book online, call with a question, or stop by the Hayesville shop during business hours.',
        'Book online, call with a question, or visit us during business hours.',
        'homepage contact introduction',
    )
    write(name, page)


def patch_services_location_copy() -> None:
    name = 'services.html'
    page = read(name)
    page = replace_required(
        page,
        'Compare BoPeeps detailing packages and vehicle-size pricing, then book your appointment at our Hayesville shop.',
        'Compare BoPeeps detailing packages and vehicle-size pricing, then book online through Booksy.',
        'services social description',
    )
    page = replace_required(
        page,
        '<p class="lede">Compare our detailing packages, check vehicle-size pricing, and book your appointment at the Hayesville shop.</p>',
        '<p class="lede">Compare our detailing packages, check vehicle-size pricing, and book online through Booksy.</p>',
        'services hero lede',
    )
    page = replace_required(
        page,
        '<div class="seo-shop-banner"><strong>Visit us in Hayesville.</strong> All detailing is completed at 1516 US-64, Hayesville, NC 28904, and customers are welcome from surrounding communities and beyond.</div>',
        f'<div class="seo-shop-banner"><strong>{LOCATION_IDENTITY}</strong></div>',
        'services location banner',
    )
    page = replace_required(
        page,
        '<div class="seo-card" style="margin-top:18px"><h2>Serving western North Carolina and north Georgia</h2><p>BoPeeps is based in Hayesville and welcomes customers from western North Carolina, north Georgia, and beyond. The links below can help nearby customers find the shop and plan a visit.</p>',
        '<div class="seo-card" style="margin-top:18px"><h2>Find BoPeeps from nearby communities</h2><p>Looking for BoPeeps from Murphy, Hiawassee, Young Harris, or Blairsville? Use the local pages below for directions and nearby information.</p>',
        'services nearby communities copy',
    )
    write(name, page)


def patch_policies_location_copy() -> None:
    name = 'policies.html'
    page = read(name)
    page = replace_required(
        page,
        '<div class="seo-shop-banner" style="margin-top:18px"><strong>Appointment location.</strong> Detailing is completed at BoPeeps, 1516 US-64, Hayesville, NC 28904. Customers are welcome from anywhere.</div>',
        f'<div class="seo-shop-banner" style="margin-top:18px"><strong>{LOCATION_IDENTITY}</strong></div>',
        'policies location banner',
    )
    write(name, page)


LOCAL_COPY = {
    'auto-detailing-hayesville-nc.html': {
        'meta_old': 'Visit BoPeeps Details & More for auto detailing in Hayesville, NC. View current package pricing, shop information, directions, and Booksy booking.',
        'meta_new': 'Visit BoPeeps Details & More for auto detailing in Hayesville, NC. View package pricing, directions, and Booksy booking.',
        'social_old': 'Auto detailing at the BoPeeps Hayesville shop, with current pricing, directions, and online booking.',
        'social_new': 'Auto detailing at BoPeeps in Hayesville, with current pricing, directions, and online booking.',
        'lede_old': 'BoPeeps Details & More provides professional auto detailing in Hayesville for Clay County, the Lake Chatuge area, and customers coming from farther away.',
        'lede_new': 'BoPeeps Details & More provides professional auto detailing in Hayesville for Clay County and the Lake Chatuge area.',
    },
    'auto-detailing-murphy-nc.html': {
        'meta_old': 'Looking for auto detailing near Murphy, NC? BoPeeps welcomes Murphy and Cherokee County customers at our Hayesville shop. See pricing, directions, and booking.',
        'meta_new': 'Looking for auto detailing near Murphy, NC? Find BoPeeps Details & More in Hayesville with pricing, directions, and online booking.',
        'social_old': 'BoPeeps welcomes Murphy and Cherokee County customers for detailing at our Hayesville shop. See pricing, directions, and online booking.',
        'social_new': 'Auto detailing near Murphy and Cherokee County, with pricing, directions to BoPeeps in Hayesville, and online booking.',
        'lede_old': 'Looking for professional auto detailing near Murphy? BoPeeps Details & More welcomes Murphy and Cherokee County customers at our Hayesville shop on US-64.',
        'lede_new': 'Looking for professional auto detailing near Murphy? BoPeeps Details & More is on US-64 in Hayesville, convenient for Murphy and Cherokee County drivers.',
    },
    'auto-detailing-hiawassee-ga.html': {
        'meta_old': 'Looking for auto detailing near Hiawassee, GA? BoPeeps welcomes Towns County and Lake Chatuge-area customers at our Hayesville shop. See pricing and booking.',
        'meta_new': 'Looking for auto detailing near Hiawassee, GA? Find BoPeeps Details & More in Hayesville with pricing, directions, and online booking.',
        'social_old': 'BoPeeps welcomes Hiawassee, Towns County, and Lake Chatuge-area customers for detailing at our Hayesville shop.',
        'social_new': 'Auto detailing near Hiawassee, Towns County, and Lake Chatuge, with directions and online booking.',
        'lede_old': 'Looking for professional auto detailing near Hiawassee? BoPeeps Details & More welcomes Towns County and Lake Chatuge-area customers at our Hayesville shop.',
        'lede_new': 'Looking for professional auto detailing near Hiawassee? BoPeeps Details & More is in Hayesville, convenient for Towns County and the Lake Chatuge area.',
    },
    'auto-detailing-young-harris-ga.html': {
        'meta_old': 'Looking for auto detailing near Young Harris, GA? BoPeeps welcomes Towns County customers at our Hayesville shop. Compare pricing, get directions, and book online.',
        'meta_new': 'Looking for auto detailing near Young Harris, GA? Find BoPeeps Details & More in Hayesville with pricing, directions, and online booking.',
        'social_old': 'BoPeeps welcomes Young Harris and Towns County customers for detailing at our Hayesville shop. See pricing, directions, and booking.',
        'social_new': 'Auto detailing near Young Harris and Towns County, with directions to BoPeeps and online booking.',
        'lede_old': 'Looking for professional auto detailing near Young Harris? BoPeeps Details & More welcomes Young Harris and Towns County customers at our Hayesville shop.',
        'lede_new': 'Looking for professional auto detailing near Young Harris? BoPeeps Details & More is in Hayesville, convenient for Towns County drivers.',
    },
    'auto-detailing-blairsville-ga.html': {
        'meta_old': 'Looking for auto detailing near Blairsville, GA? BoPeeps welcomes Union County customers at our Hayesville shop. Compare package pricing, directions, and booking.',
        'meta_new': 'Looking for auto detailing near Blairsville, GA? Find BoPeeps Details & More in Hayesville with pricing, directions, and online booking.',
        'social_old': 'BoPeeps welcomes Blairsville and Union County customers for detailing at our Hayesville shop. See pricing, directions, and online booking.',
        'social_new': 'Auto detailing near Blairsville and Union County, with directions to BoPeeps and online booking.',
        'lede_old': 'Looking for professional auto detailing near Blairsville? BoPeeps Details & More welcomes Blairsville and Union County customers at our Hayesville shop.',
        'lede_new': 'Looking for professional auto detailing near Blairsville? BoPeeps Details & More is in Hayesville, convenient for Union County drivers.',
    },
}


def patch_local_location_copy() -> None:
    old_banner = (
        '<div class="seo-shop-banner"><strong>Your appointment is at BoPeeps in Hayesville.</strong> '
        'All detailing is completed at 1516 US-64, Hayesville, NC 28904.</div>'
    )
    new_banner = f'<div class="seo-shop-banner"><strong>{LOCATION_IDENTITY}</strong></div>'
    old_nearby = (
        'Coming from another nearby town? Use the links below for local information, or simply '
        'get directions from wherever you are. BoPeeps welcomes customers from anywhere.'
    )
    new_nearby = (
        'Coming from another nearby town? Use the links below for local information, or get '
        'directions from your current location.'
    )

    for name, data in LOCAL_COPY.items():
        page = read(name)
        page = replace_required(page, data['meta_old'], data['meta_new'], f'{name} meta description')
        page = replace_required(page, data['social_old'], data['social_new'], f'{name} social description')
        page = replace_required(page, data['lede_old'], data['lede_new'], f'{name} introduction')
        page = replace_required(page, old_banner, new_banner, f'{name} location banner')
        page = replace_required(page, old_nearby, new_nearby, f'{name} nearby communities')
        write(name, page)


def main() -> None:
    patch_mobile_directions()
    patch_privacy_sentence()
    patch_hayesville_lede()
    patch_global_location_language()
    patch_homepage_location_copy()
    patch_services_location_copy()
    patch_policies_location_copy()
    patch_local_location_copy()


if __name__ == '__main__':
    main()
