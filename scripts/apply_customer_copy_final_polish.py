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
MAPS_SEARCH = 'https://www.google.com/maps/search/?api=1&query=1516%20US-64%2C%20Hayesville%2C%20NC%2028904'
MAPS_DIRECTIONS = 'https://www.google.com/maps/dir/?api=1&amp;destination=1516%20US-64%2C%20Hayesville%2C%20NC%2028904'


def read(name: str) -> str:
    return (ROOT / name).read_text(encoding='utf-8')


def write(name: str, content: str) -> None:
    (ROOT / name).write_text(content, encoding='utf-8')


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
    old = (
        'BoPeeps Details & More provides professional auto detailing from our Hayesville shop '
        'on US-64, serving Clay County, the Lake Chatuge area, and customers who make the drive '
        'from beyond.'
    )
    new = (
        'BoPeeps Details & More provides professional auto detailing in Hayesville for Clay '
        'County, the Lake Chatuge area, and customers coming from farther away.'
    )
    if new not in page:
        if old not in page:
            raise RuntimeError('Could not find Hayesville local-page introduction')
        page = page.replace(old, new, 1)
    write(name, page)


def main() -> None:
    patch_mobile_directions()
    patch_privacy_sentence()
    patch_hayesville_lede()


if __name__ == '__main__':
    main()
