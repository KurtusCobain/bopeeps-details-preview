from pathlib import Path

ROOT = Path('.')

# The site ships only the optimized WebP variants. The unoptimized duplicate
# sources were removed on the 2026-11-18 fix branch (they were unreferenced
# and roughly doubled the published asset weight).
OPTIMIZED_ASSETS = [
    'assets-v3/gallery-exterior-care-optimized.webp',
    'assets-v3/gallery-photo-8-optimized.webp',
    'assets-v3/gallery-photo-14-optimized.webp',
    'assets-v3/gallery-photo-21-optimized.webp',
    'assets-v3/gallery-photo-25-optimized.webp',
    'assets-v3/gallery-real-local-work-optimized.webp',
    'assets-v3/scrub-photo-6-optimized.webp',
    'assets-v3/scrub-photo-10-optimized.webp',
    'assets-v3/scrub-photo-15-optimized.webp',
    'assets-v3/scrub-work-vehicles-optimized.webp',
    'assets-v3/kenworth-dump-truck-optimized.webp',
    'assets-v3/boat-silverado-optimized.webp',
    'assets-v3/boat-closeup-optimized.webp',
    'assets-v3/rv-freedom-elite-optimized.webp',
    'assets-v3/jeep-wrangler-front-optimized.webp',
    'assets-v3/gmc-sierra-hd-optimized.webp',
    'assets-v3/ford-bronco-bay-optimized.webp',
    'assets-v3/wagoneer-exterior-optimized.webp'
]

REMOVED_UNOPTIMIZED_DUPLICATES = [
    'assets/logo-modern.jpg',
    'assets-v3/gallery-exterior-care.webp',
    'assets-v3/gallery-photo-8.webp',
    'assets-v3/gallery-photo-14.webp',
    'assets-v3/gallery-photo-21.webp',
    'assets-v3/gallery-photo-25.webp',
    'assets-v3/gallery-real-local-work.webp',
    'assets-v3/scrub-photo-6.webp',
    'assets-v3/scrub-photo-10.webp',
    'assets-v3/scrub-photo-15.webp',
    'assets-v3/scrub-work-vehicles.webp'
]


def test_optimized_assets_exist():
    for name in OPTIMIZED_ASSETS:
        assert (ROOT / name).exists(), name


def test_unoptimized_duplicates_stay_removed():
    for name in REMOVED_UNOPTIMIZED_DUPLICATES:
        assert not (ROOT / name).exists(), name


def test_logo_webp_is_the_only_logo_image():
    assert (ROOT / 'assets/logo-modern.webp').exists()
    assert not (ROOT / 'assets/logo-modern.jpg').exists()
