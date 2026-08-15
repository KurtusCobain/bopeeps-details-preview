from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BRAND_EYEBROW = '<p class="eyebrow">BoPeeps Details &amp; More</p>'
OLD_LOCATION_EYEBROW = '<p class="eyebrow">BoPeeps Details & More · Hayesville, NC</p>'


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


def patch_homepage() -> None:
    name = 'index.html'
    page = read(name)
    page = replace_required(
        page,
        '<p class="eyebrow">Come see us in Hayesville</p>',
        '<p class="eyebrow">Serving the region</p>',
        'homepage regional eyebrow',
    )
    page = replace_required(
        page,
        'Drop off at our Hayesville location and talk with us directly if you have questions about your vehicle or service.',
        'Drop off your vehicle and talk with us directly if you have questions about the service you need.',
        'homepage drop-off copy',
    )
    write(name, page)


def patch_page_eyebrows() -> None:
    for name in [
        'services.html',
        'privacy.html',
        'auto-detailing-hayesville-nc.html',
        'auto-detailing-murphy-nc.html',
        'auto-detailing-hiawassee-ga.html',
        'auto-detailing-young-harris-ga.html',
        'auto-detailing-blairsville-ga.html',
    ]:
        page = read(name)
        page = replace_required(page, OLD_LOCATION_EYEBROW, BRAND_EYEBROW, f'{name} hero eyebrow')
        write(name, page)


def patch_local_introductions() -> None:
    replacements = {
        'auto-detailing-hayesville-nc.html': (
            'BoPeeps Details & More provides professional auto detailing in Hayesville for Clay County and the Lake Chatuge area.',
            'Professional auto detailing for Hayesville, Clay County, and the Lake Chatuge area.',
        ),
        'auto-detailing-murphy-nc.html': (
            'Looking for professional auto detailing near Murphy? BoPeeps Details & More is on US-64 in Hayesville, convenient for Murphy and Cherokee County drivers.',
            'Looking for professional auto detailing near Murphy? BoPeeps Details & More is a convenient option for Murphy and Cherokee County drivers.',
        ),
        'auto-detailing-hiawassee-ga.html': (
            'Looking for professional auto detailing near Hiawassee? BoPeeps Details & More is in Hayesville, convenient for Towns County and the Lake Chatuge area.',
            'Looking for professional auto detailing near Hiawassee? BoPeeps Details & More is a convenient option for Hiawassee, Towns County, and the Lake Chatuge area.',
        ),
        'auto-detailing-young-harris-ga.html': (
            'Looking for professional auto detailing near Young Harris? BoPeeps Details & More is in Hayesville, convenient for Towns County drivers.',
            'Looking for professional auto detailing near Young Harris? BoPeeps Details & More is a convenient option for Young Harris and Towns County drivers.',
        ),
        'auto-detailing-blairsville-ga.html': (
            'Looking for professional auto detailing near Blairsville? BoPeeps Details & More is in Hayesville, convenient for Union County drivers.',
            'Looking for professional auto detailing near Blairsville? BoPeeps Details & More is a convenient option for Blairsville and Union County drivers.',
        ),
    }
    for name, (old, new) in replacements.items():
        page = read(name)
        page = replace_required(page, old, new, f'{name} local introduction')
        write(name, page)


def main() -> None:
    patch_homepage()
    patch_page_eyebrows()
    patch_local_introductions()


if __name__ == '__main__':
    main()
