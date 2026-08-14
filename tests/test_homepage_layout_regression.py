from pathlib import Path
import re

# Guards the two homepage alignment defects reported during visual preview review.
CSS = Path('styles-v3.css').read_text(encoding='utf-8')


def compact(value: str) -> str:
    return re.sub(r'\s+', ' ', value).strip()


def test_interactive_demo_has_clear_separation_from_gallery_footer():
    css = compact(CSS)
    match = re.search(
        r'\.gallery-footer\s*\+\s*\.section-heading\s*\{([^}]*)\}',
        css,
    )
    assert match, 'interactive demo heading needs a dedicated post-gallery spacing rule'
    rule = match.group(1)
    margin = re.search(r'margin-top:\s*(\d+)px', rule)
    assert margin, 'interactive demo spacing must use an explicit top margin'
    assert int(margin.group(1)) >= 40


def test_three_benefit_cards_are_centered_without_an_empty_grid_track():
    css = compact(CSS)
    base = re.search(r'\.benefit-grid\s*\{([^}]*)\}', css)
    assert base, 'benefit grid rule missing'
    base_rule = base.group(1)
    assert 'max-width:' in base_rule
    assert 'margin-inline: auto' in base_rule

    desktop = re.search(
        r'@media \(min-width: 700px\)\s*\{(.*?)@media \(min-width: 768px\)',
        css,
    )
    assert desktop, '700px desktop/tablet breakpoint missing'
    benefit = re.search(r'\.benefit-grid\s*\{([^}]*)\}', desktop.group(1))
    assert benefit, 'benefit grid desktop rule missing'
    assert 'repeat(3' in benefit.group(1)
    assert 'repeat(4' not in benefit.group(1)
