from pathlib import Path

HTML = Path("index.html").read_text(encoding="utf-8")


def test_service_pricing_notice_exists():
    assert 'class="pricing-notice"' in HTML
    assert 'id="pricing-notice-title"' in HTML
    assert 'href="#pricing-policy"' in HTML


def test_pet_hair_threshold_and_fee_are_disclosed():
    approved_threshold = "Excessive pet hair requiring additional removal time"
    assert HTML.count(approved_threshold) >= 2
    assert HTML.count("$20") >= 2


def test_final_charge_is_described_as_itemized():
    assert "itemized in your final checkout" in HTML
    assert "receipt or payment confirmation email" in HTML


def test_lower_pricing_policy_section_exists_once():
    assert HTML.count('id="pricing-policy"') == 1
    assert "When does the $20 pet hair fee apply?" in HTML
    assert "How is the additional charge handled?" in HTML


def test_policy_explains_normal_pet_hair_threshold():
    assert "A few stray hairs are not the intended threshold." in HTML
    assert "Excessive Pet Hair Removal" in HTML
