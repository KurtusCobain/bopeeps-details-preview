from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSS_PATH = ROOT / 'styles-v3.css'


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if new in text:
        return text
    if old not in text:
        raise RuntimeError(f'Could not find expected {label} source rule')
    return text.replace(old, new, 1)


def patch_css() -> None:
    css = CSS_PATH.read_text(encoding='utf-8')

    css = replace_once(
        css,
        '.gallery-footer { margin-top: 22px; }\n.about-section',
        '.gallery-footer { margin-top: 22px; }\n.gallery-footer + .section-heading { margin-top: 52px; }\n.about-section',
        'gallery-to-demo spacing',
    )

    css = replace_once(
        css,
        '.benefit-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }',
        '.benefit-grid { display: grid; grid-template-columns: 1fr; gap: 12px; max-width: 900px; margin-inline: auto; }',
        'base benefit grid',
    )

    css = replace_once(
        css,
        '.benefit-grid { grid-template-columns: repeat(4,1fr); }',
        '.benefit-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }',
        'desktop benefit grid',
    )

    CSS_PATH.write_text(css, encoding='utf-8')


def bump_stylesheet_cache() -> None:
    old = 'styles-v3.css?v=20260809b'
    new = 'styles-v3.css?v=20260814c'
    for path in ROOT.glob('*.html'):
        text = path.read_text(encoding='utf-8')
        if old in text:
            path.write_text(text.replace(old, new), encoding='utf-8')


def main() -> None:
    patch_css()
    bump_stylesheet_cache()


if __name__ == '__main__':
    main()
