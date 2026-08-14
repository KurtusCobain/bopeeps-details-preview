from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / '_site'

PUBLIC_FILES = [
    '.nojekyll',
    '404.html',
    'CNAME',
    'apple-touch-icon.png',
    'auto-detailing-blairsville-ga.html',
    'auto-detailing-hayesville-nc.html',
    'auto-detailing-hiawassee-ga.html',
    'auto-detailing-murphy-nc.html',
    'auto-detailing-young-harris-ga.html',
    'favicon-48.png',
    'favicon.ico',
    'index.html',
    'policies.html',
    'privacy.html',
    'robots.txt',
    'script-v3.js',
    'seo-pages.css',
    'services.html',
    'sitemap.xml',
    'styles-v3.css',
]

PUBLIC_DIRS = ['assets', 'assets-v3']


def build() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()

    for name in PUBLIC_FILES:
        shutil.copy2(ROOT / name, OUT / name)

    for name in PUBLIC_DIRS:
        shutil.copytree(ROOT / name, OUT / name)


if __name__ == '__main__':
    build()
