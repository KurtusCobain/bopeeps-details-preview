from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]

TARGETS = [
    ('assets/logo-modern.jpg', 'assets/logo-modern.webp', 720, 82),
    ('assets-v3/gallery-exterior-care.webp', 'assets-v3/gallery-exterior-care-optimized.webp', 1200, 76),
    ('assets-v3/gallery-photo-8.webp', 'assets-v3/gallery-photo-8-optimized.webp', 1200, 76),
    ('assets-v3/gallery-photo-14.webp', 'assets-v3/gallery-photo-14-optimized.webp', 1200, 76),
    ('assets-v3/gallery-photo-21.webp', 'assets-v3/gallery-photo-21-optimized.webp', 1200, 76),
    ('assets-v3/gallery-photo-25.webp', 'assets-v3/gallery-photo-25-optimized.webp', 1200, 76),
    ('assets-v3/gallery-real-local-work.webp', 'assets-v3/gallery-real-local-work-optimized.webp', 1200, 76),
    ('assets-v3/scrub-photo-6.webp', 'assets-v3/scrub-photo-6-optimized.webp', 1200, 74),
    ('assets-v3/scrub-photo-10.webp', 'assets-v3/scrub-photo-10-optimized.webp', 1200, 74),
    ('assets-v3/scrub-photo-15.webp', 'assets-v3/scrub-photo-15-optimized.webp', 1200, 74),
    ('assets-v3/scrub-work-vehicles.webp', 'assets-v3/scrub-work-vehicles-optimized.webp', 1200, 74),
]


def optimize(source_name: str, output_name: str, max_dimension: int, quality: int) -> None:
    source = ROOT / source_name
    output = ROOT / output_name

    with Image.open(source) as image:
        image.load()
        if max(image.size) > max_dimension:
            image.thumbnail((max_dimension, max_dimension), Image.Resampling.LANCZOS)
        if image.mode not in {'RGB', 'RGBA'}:
            image = image.convert('RGBA' if 'A' in image.getbands() else 'RGB')
        image.save(output, 'WEBP', quality=quality, method=6)

    if output.stat().st_size >= source.stat().st_size:
        output.unlink()
        raise RuntimeError(f'Optimization did not reduce {source_name}')


if __name__ == '__main__':
    for target in TARGETS:
        optimize(*target)
