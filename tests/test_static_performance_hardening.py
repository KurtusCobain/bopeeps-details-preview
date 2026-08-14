from html.parser import HTMLParser
from pathlib import Path

HOME = Path('index.html').read_text(encoding='utf-8')


class HomeImageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
        self.preloads = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'img':
            self.images.append(attrs)
        if tag == 'link' and attrs.get('rel') == 'preload' and attrs.get('as') == 'image':
            self.preloads.append(attrs.get('href'))


def parsed_home():
    parser = HomeImageParser()
    parser.feed(HOME)
    return parser


def test_homepage_only_preloads_the_lcp_storefront_image():
    parser = parsed_home()
    assert parser.preloads == ['assets-v3/hero-storefront-desktop.webp']


def test_hero_is_eager_while_below_fold_work_images_are_lazy():
    parser = parsed_home()
    by_src = {image.get('src'): image for image in parser.images}

    hero = by_src['assets-v3/hero-storefront-desktop.webp']
    assert hero.get('loading') != 'lazy'

    below_fold_prefixes = (
        'assets-v3/service-',
        'assets-v3/gallery-',
        'assets-v3/scrub-',
    )
    for image in parser.images:
        src = image.get('src', '')
        if src.startswith(below_fold_prefixes):
            assert image.get('loading') == 'lazy', src


def test_footer_logo_is_lazy_loaded():
    parser = parsed_home()
    logos = [image for image in parser.images if image.get('src') == 'assets/logo-modern.jpg']
    assert len(logos) >= 2
    assert logos[-1].get('loading') == 'lazy'
