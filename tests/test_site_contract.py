from __future__ import annotations

import re
import unittest
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOOKSY_PROFILE = (
    "https://booksy.com/en-us/"
    "1808686_bopeeps-detail-more_other_26564_hayesville"
)
BOOKSY_WIDGET = "https://booksy.com/widget/code.js?id=1808686&country=us&lang=en"


class Node:
    def __init__(self, tag: str, attrs: dict[str, str], parent: "Node | None"):
        self.tag = tag
        self.attrs = attrs
        self.parent = parent
        self.children: list[Node] = []
        self.text_parts: list[str] = []

    @property
    def text(self) -> str:
        parts = list(self.text_parts)
        for child in self.children:
            parts.append(child.text)
        return " ".join(" ".join(parts).split())

    def has_class(self, name: str) -> bool:
        return name in self.attrs.get("class", "").split()

    def descendants(self, tag: str | None = None) -> list["Node"]:
        found: list[Node] = []
        for child in self.children:
            if tag is None or child.tag == tag:
                found.append(child)
            found.extend(child.descendants(tag))
        return found


class TreeParser(HTMLParser):
    VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}

    def __init__(self) -> None:
        super().__init__()
        self.root = Node("document", {}, None)
        self.stack = [self.root]

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        node = Node(tag, {key: value or "" for key, value in attrs}, self.stack[-1])
        self.stack[-1].children.append(node)
        if tag not in self.VOID_TAGS:
            self.stack.append(node)

    def handle_endtag(self, tag: str) -> None:
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                return

    def handle_data(self, data: str) -> None:
        if data.strip():
            self.stack[-1].text_parts.append(data)


def load_tree() -> Node:
    parser = TreeParser()
    parser.feed((ROOT / "index.html").read_text(encoding="utf-8"))
    return parser.root


class SiteContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.tree = load_tree()
        cls.nodes = cls.tree.descendants()

    def test_service_cards_use_real_photos_and_verified_details(self) -> None:
        cards = [node for node in self.nodes if node.has_class("service-card")]
        self.assertEqual(len(cards), 3)

        expected = [
            ("Express Wash And Spray Wax", "$60+", "1 hr", "assets-v3/service-wash.webp"),
            ("Deluxe Detail Package", "$85+", "2 hrs", "assets-v3/service-interior.webp"),
            ("Jacky Jones Premium Detail", "$150+", "4 hrs", "assets-v3/service-premium.webp"),
        ]
        actual = []
        for card in cards:
            image = card.descendants("img")[0]
            link = next(node for node in card.descendants("a") if "data-booksy-open" in node.attrs)
            actual.append((card.text, image.attrs["src"], link.attrs.get("href")))

        for (name, price, duration, image), (text, actual_image, href) in zip(expected, actual):
            self.assertIn(name, text)
            self.assertIn(price, text)
            self.assertIn(duration, text)
            self.assertEqual(actual_image, image)
            self.assertEqual(href, BOOKSY_PROFILE)

    def test_scrub_selector_exposes_the_four_approved_real_photos(self) -> None:
        choices = [node for node in self.nodes if "data-scrub-choice" in node.attrs]
        self.assertEqual(
            [(node.attrs["data-scrub-choice"], node.attrs["data-scrub-src"]) for node in choices],
            [
                ("rv", "assets-v3/scrub-photo-6.webp"),
                ("white-truck", "assets-v3/scrub-photo-10.webp"),
                ("black-truck", "assets-v3/scrub-photo-11.webp"),
                ("interior", "assets-v3/scrub-photo-15.webp"),
            ],
        )
        self.assertEqual(sum("data-scrub-canvas" in node.attrs for node in self.nodes), 1)
        self.assertEqual(sum("data-scrub-reset" in node.attrs for node in self.nodes), 1)
        self.assertEqual(sum("data-scrub-reveal" in node.attrs for node in self.nodes), 1)
        self.assertIn("simulated grime", self.tree.text.lower())

    def test_gallery_uses_the_six_approved_real_work_photos(self) -> None:
        gallery = next(node for node in self.nodes if node.has_class("gallery-grid"))
        sources = [image.attrs["src"] for image in gallery.descendants("img")]
        self.assertEqual(
            sources,
            [
                "assets-v3/gallery-photo-5.webp",
                "assets-v3/gallery-photo-8.webp",
                "assets-v3/gallery-photo-14.webp",
                "assets-v3/gallery-photo-21.webp",
                "assets-v3/gallery-photo-25.webp",
                "assets-v3/gallery-photo-28.webp",
            ],
        )
        self.assertTrue(all(image.attrs.get("alt", "").strip() for image in gallery.descendants("img")))

    def test_official_booksy_widget_and_resilient_fallback_links_are_present(self) -> None:
        widget_scripts = [
            node for node in self.nodes if node.tag == "script" and node.attrs.get("src") == BOOKSY_WIDGET
        ]
        self.assertEqual(len(widget_scripts), 1)

        booking_links = [node for node in self.nodes if "data-booksy-open" in node.attrs]
        self.assertGreaterEqual(len(booking_links), 6)
        self.assertTrue(all(link.tag == "a" and link.attrs.get("href") == BOOKSY_PROFILE for link in booking_links))

    def test_contact_contract_and_stale_values(self) -> None:
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("706-897-6177", html)
        self.assertIn("tel:+17068976177", html)
        self.assertIn("hello@bopeepsdetails.com", html)
        self.assertIn("1516 US-64", html)
        self.assertNotIn("828-", html)
        self.assertNotIn("bopeepsdetail@gmail.com", html)

    def test_preserved_preview_shell_contracts(self) -> None:
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        css = (ROOT / "styles-v3.css").read_text(encoding="utf-8")
        self.assertTrue((ROOT / ".nojekyll").is_file())
        self.assertIn('href="styles-v3.css?v=20260808b"', html)
        self.assertIn('src="script-v3.js?v=20260808"', html)
        self.assertIn('class="hero-image" src="assets/truck-wrap.jpg"', html)
        self.assertIn("Mon-Sat", html)
        self.assertIn("7:00 AM-5:00 PM", html)
        self.assertIn("Sunday", html)
        self.assertIn("Closed", html)
        self.assertIn("data-site-nav", html)
        self.assertIn('class="mobile-actions"', html)
        self.assertIn("www.google.com/maps", html)
        self.assertIn("@media (prefers-reduced-motion: reduce)", css)

    def test_service_artwork_uses_contained_fit_without_changing_image_height(self) -> None:
        css = (ROOT / "styles-v3.css").read_text(encoding="utf-8")
        rule = re.search(r"\.service-card img\s*\{([^}]*)\}", css)
        self.assertIsNotNone(rule)
        declarations = rule.group(1)
        self.assertRegex(declarations, r"height:\s*210px")
        self.assertRegex(declarations, r"object-fit:\s*contain")

    def test_all_local_page_assets_resolve(self) -> None:
        local_refs: set[str] = set()
        for node in self.nodes:
            for attr in ("src", "href"):
                value = node.attrs.get(attr, "")
                if value and not value.startswith(("http:", "https:", "tel:", "mailto:", "sms:", "#")):
                    local_refs.add(value.split("?", 1)[0])
        missing = sorted(ref for ref in local_refs if not (ROOT / ref).exists())
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
