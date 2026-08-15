from pathlib import Path

HOME = Path("index.html").read_text(encoding="utf-8")
POLICIES_PATH = Path("policies.html")


def test_service_pricing_notice_links_to_policies_page():
    assert 'class="pricing-notice"' in HOME
    assert 'id="pricing-notice-title"' in HOME
    assert 'href="policies.html"' in HOME


def test_homepage_no_longer_contains_full_policy_section():
    assert 'id="pricing-policy"' not in HOME
    assert "When does the $20 pet hair fee apply?" not in HOME


def test_policies_page_exists():
    assert POLICIES_PATH.exists()


def test_approved_disclosure_matches_on_home_and_policies_page():
    policies = POLICIES_PATH.read_text(encoding="utf-8")
    threshold = "Excessive pet hair requiring additional removal time"
    final_charge = "itemized in your final checkout and reflected on your receipt or payment confirmation email"

    assert threshold in HOME
    assert "$20 pet hair removal fee" in HOME
    assert final_charge in HOME

    assert threshold in policies
    assert "$20 pet hair removal fee" in policies
    assert final_charge in policies


def test_policy_page_explains_threshold_line_item_and_scope():
    policies = POLICIES_PATH.read_text(encoding="utf-8")
    assert "Pricing & Vehicle Condition Policy" in policies
    assert "Standard pricing" in policies
    assert "When the pet-hair fee applies" in policies
    assert "At checkout" in policies
    assert "A few stray hairs are not the intended threshold." in policies
    assert "$20 Excessive Pet Hair Removal" in policies
    assert "Booksy handles appointment availability and checkout." in policies
    assert 'href="privacy.html"' in policies
    assert 'href="index.html"' in policies
