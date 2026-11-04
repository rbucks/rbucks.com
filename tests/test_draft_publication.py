"""Production builds must never include unfinished draft text or pages."""
from pathlib import Path

from pelican import Pelican
from pelican.settings import read_settings


def test_production_excludes_drafts(tmp_path):
    root = Path(__file__).resolve().parents[1]
    content = tmp_path / 'content'
    content.mkdir()
    (content / 'pages').mkdir()
    header = (
        'Title: {title}\nDate: 2026-01-01 09:00\nSlug: {slug}\n'
        'Category: Business\nTags: testing\n{status}\n{body}\n'
    )
    cases = [
        ('published.md', 'Published test', 'published-test', '', 'PUBLISHED_SENTINEL'),
        ('draft.md', 'Draft test', 'draft-test', 'Status: draft\n', 'DRAFT_ARTICLE_SENTINEL'),
        ('pages/draft.md', 'Draft page', 'draft-page', 'Status: draft\n', 'DRAFT_PAGE_SENTINEL'),
    ]
    for filename, title, slug, status, body in cases:
        (content / filename).write_text(
            header.format(title=title, slug=slug, status=status, body=body),
            encoding='utf-8',
        )

    output = tmp_path / 'output'
    settings = read_settings(str(root / 'publishconf.py'), override={
        'PATH': str(content),
        'OUTPUT_PATH': str(output),
        'THEME': str(root / 'themes/rbucks-v2'),
        'PLUGIN_PATHS': [str(root / 'plugins')],
        'CACHE_CONTENT': False,
        'LOAD_CONTENT_CACHE': False,
    })
    Pelican(settings).run()

    assert (output / '2026/01/01/published-test/index.html').is_file()
    assert not (output / 'drafts').exists()
    assert not list(output.rglob('*draft-test*'))
    assert not list(output.rglob('*draft-page*'))
    for path in output.rglob('*'):
        if path.is_file() and path.suffix in {'.html', '.xml', '.json'}:
            text = path.read_text(encoding='utf-8')
            assert 'DRAFT_ARTICLE_SENTINEL' not in text, path
            assert 'DRAFT_PAGE_SENTINEL' not in text, path
            assert 'Draft test' not in text, path
            assert 'Draft page' not in text, path
