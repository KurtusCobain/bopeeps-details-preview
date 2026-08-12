from pathlib import Path

HOME = Path("index.html").read_text(encoding="utf-8")
DIAGNOSTIC_HTML = Path("booksy-widget-diagnostic.html")
DIAGNOSTIC_JS = Path("booksy-widget-diagnostic.js")


def test_diagnostic_is_isolated_from_homepage():
    assert "booksy-widget-diagnostic.js" not in HOME
    assert DIAGNOSTIC_HTML.exists()
    assert DIAGNOSTIC_JS.exists()


def test_diagnostic_page_uses_production_booksy_embed_identity():
    html = DIAGNOSTIC_HTML.read_text(encoding="utf-8")
    assert "booksy.com/widget/code.js?id=1808686&country=us&lang=en" in html
    assert 'src="booksy-widget-diagnostic.js"' in html


def test_diagnostic_collects_structure_only():
    js = DIAGNOSTIC_JS.read_text(encoding="utf-8")
    forbidden = [
        "fetch(",
        "XMLHttpRequest",
        "localStorage",
        "sessionStorage",
        ".value",
        "FormData",
    ]
    for token in forbidden:
        assert token not in js


def test_diagnostic_has_b1_b2_b3_classification():
    js = DIAGNOSTIC_JS.read_text(encoding="utf-8")
    assert '"B1"' in js
    assert '"B2"' in js
    assert '"B3"' in js
    assert "MutationObserver" in js
    assert "contentDocument" in js
