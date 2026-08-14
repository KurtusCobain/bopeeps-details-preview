from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / 'scripts' / 'build_site.py'
SITE = ROOT / '_site'

PUBLIC_ROOT_FILES = {
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
}


def test_public_build_contains_only_deployable_site_files():
    assert BUILD.exists(), 'scripts/build_site.py is required'

    subprocess.run([sys.executable, str(BUILD)], cwd=ROOT, check=True)

    root_files = {path.name for path in SITE.iterdir() if path.is_file()}
    assert root_files == PUBLIC_ROOT_FILES
    assert (SITE / 'assets').is_dir()
    assert (SITE / 'assets-v3').is_dir()

    for forbidden in ['README.md', 'docs', 'tests', '.github', 'scripts']:
        assert not (SITE / forbidden).exists(), forbidden
