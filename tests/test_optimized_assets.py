from pathlib import Path

ROOT = Path('.')

PAIRS = [
    ('assets/logo-modern.jpg', 'assets/logo-modern.webp'),
    ('assets-v3/gallery-exterior-care.webp', 'assets-v3/gallery-exterior-care-optimized.webp'),
    ('assets-v3/gallery-photo-8.webp', 'assets-v3/gallery-photo-8-optimized.webp'),
    ('assets-v3/gallery-photo-14.webp', 'assets-v3/gallery-photo-14-optimized.webp'),
    ('assets-v3/gallery-photo-21.webp', 'assets-v3/gallery-photo-21-optimized.webp'),
    ('assets-v3/gallery-photo-25.webp', 'assets-v3/gallery-photo-25-optimized.webp'),
    ('assets-v3/gallery-real-local-work.webp', 'assets-v3/gallery-real-local-work-optimized.webp'),
    ('assets-v3/scrub-photo-6.webp', 'assets-v3/scrub-photo-6-optimized.webp'),
    ('assets-v3/scrub-photo-10.webp', 'assets-v3/scrub-photo-10-optimized.webp'),
    ('assets-v3/scrub-photo-15.webp', 'assets-v3/scrub-photo-15-optimized.webp'),
    ('assets-v3/scrub-work-vehicles.webp', 'assets-v3/scrub-work-vehicles-optimized.webp'),
]


def test_optimized_assets_exist_and_are_smaller_than_sources():
    for source_name, optimized_name in PAIRS:
        source = ROOT / source_name
        optimized = ROOT / optimized_name
        assert source.exists(), source_name
        assert optimized.exists(), optimized_name
        assert optimized.stat().st_size < source.stat().st_size, optimized_name


def test_logo_webp_is_substantially_smaller():
    source = ROOT / 'assets/logo-modern.jpg'
    optimized = ROOT / 'assets/logo-modern.webp'
    assert optimized.stat().st_size <= source.stat().st_size * 0.5
