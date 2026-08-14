from pathlib import Path
import re

PUBLIC_PAGES = [
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


def page(name: str) -> str:
    return Path(name).read_text(encoding='utf-8')


def test_every_navigation_landmark_has_an_accessible_label():
    for name in PUBLIC_PAGES:
        text = page(name)
        for attrs in re.findall(r'<nav\b([^>]*)>', text, flags=re.I):
            assert re.search(r'\baria-label="[^"]+"', attrs, flags=re.I), f'{name}: <nav{attrs}>'


def test_blank_target_links_include_noopener():
    for name in PUBLIC_PAGES:
        text = page(name)
        for tag in re.findall(r'<a\b[^>]*target="_blank"[^>]*>', text, flags=re.I):
            rel = re.search(r'\brel="([^"]*)"', tag, flags=re.I)
            assert rel and 'noopener' in rel.group(1).split(), f'{name}: {tag}'


def test_mobile_menu_updates_screen_reader_label():
    script = Path('script-v3.js').read_text(encoding='utf-8')
    assert "menuLabel.textContent = open ? 'Close menu' : 'Open menu'" in script
    assert "const closeMenu = () => setMenuState(false);" in script
