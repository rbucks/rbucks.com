"""Tests for the search_index_generator plugin."""
import json
import os
import sys
import tempfile
from unittest.mock import MagicMock, patch

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from plugins.search_index_generator import strip_html, generate_search_index, register


# ─── strip_html ──────────────────────────────────────────────────────────────

class TestStripHtml:
    def test_basic(self):
        """Basic HTML tags stripped."""
        assert strip_html("<p>Hello</p>") == "Hello"

    def test_nested_tags(self):
        """Nested HTML tags stripped."""
        assert strip_html("<div><strong>Bold</strong> text</div>") == "Bold text"

    def test_no_html(self):
        """Plain text without HTML is unchanged."""
        assert strip_html("Just plain text.") == "Just plain text."

    def test_empty_string(self):
        """Empty string returns empty string."""
        assert strip_html("") == ""

    def test_multiline(self):
        """Multiline HTML stripped."""
        result = strip_html("<p>Line 1</p>\n<p>Line 2</p>")
        assert "Line 1" in result
        assert "Line 2" in result

    def test_self_closing_tags(self):
        """Self-closing tags removed."""
        assert strip_html("Text<br />more") == "Textmore"

    def test_only_tags(self):
        """Only tags returns empty string."""
        assert strip_html("<br><hr><img>") == ""

    def test_strip_extra_whitespace(self):
        """Leading/trailing whitespace stripped."""
        assert strip_html("  <p>Content</p>  ") == "Content"

    def test_special_chars(self):
        """Special characters preserved after stripping."""
        result = strip_html("<p>Café &amp; résumé</p>")
        assert "Café" in result


# ─── generate_search_index ───────────────────────────────────────────────────

class MockArticle:
    """Minimal mock for a Pelican article."""
    def __init__(self, title, slug, url, category, tags, summary, metadata=None):
        self.title = title
        self.slug = slug
        self.url = url
        self.category = MagicMock()
        self.category.name = category
        self.tags = [MagicMock() for _ in tags]
        for i, t in enumerate(tags):
            self.tags[i].name = t
        self.summary = summary
        self.metadata = metadata or {}
        # Support both explicit summary in metadata and _content fallback
        if summary and 'summary' not in self.metadata:
            self.metadata['summary'] = summary
        self._content = summary or ''
        self.date = MagicMock()
        self.date.strftime.return_value = '2024-01-15'


class TestGenerateSearchIndex:
    def test_basic_index(self, tmp_path):
        """Basic index with one article."""
        article = MockArticle(
            title="Test Post",
            slug="test-post",
            url="2024/01/15/test-post/",
            category="Business",
            tags=["testing", "pytest"],
            summary="<p>A test summary.</p>",
            metadata={'description': 'A test description.'},
        )

        generator = MagicMock()
        generator.context = {'articles': [article]}
        generator.settings = {'OUTPUT_PATH': str(tmp_path), 'SITEURL': 'https://example.com'}

        generate_search_index(generator)

        index_path = tmp_path / 'search_index.json'
        assert index_path.exists()

        with open(index_path, 'r') as f:
            data = json.load(f)

        assert len(data['articles']) == 1
        a = data['articles'][0]
        assert a['title'] == 'Test Post'
        assert a['slug'] == 'test-post'
        assert a['url'] == '/2024/01/15/test-post/'
        assert a['category'] == 'Business'
        assert a['tags'] == ['testing', 'pytest']
        assert a['date'] == '2024-01-15'
        assert a['description'] == 'A test description.'
        assert a['summary'] == 'A test summary.'

    def test_multiple_articles(self, tmp_path):
        """Multiple articles in the index."""
        articles = [
            MockArticle("First", "first", "2024/01/01/first/", "Tech", ["a"], "<p>First</p>", {}),
            MockArticle("Second", "second", "2024/01/02/second/", "Biz", ["b"], "<p>Second</p>", {'description': 'Second desc'}),
        ]

        generator = MagicMock()
        generator.context = {'articles': articles}
        generator.settings = {'OUTPUT_PATH': str(tmp_path), 'SITEURL': ''}

        generate_search_index(generator)

        with open(tmp_path / 'search_index.json') as f:
            data = json.load(f)

        assert len(data['articles']) == 2
        assert data['articles'][0]['title'] == 'First'
        assert data['articles'][1]['title'] == 'Second'

    def test_metadata_description_none(self, tmp_path):
        """When description metadata is absent, should be None."""
        article = MockArticle(
            "No Desc", "no-desc", "2024/01/01/no-desc/",
            "Personal", ["test"], "<p>Summary here</p>", {}
        )
        generator = MagicMock()
        generator.context = {'articles': [article]}
        generator.settings = {'OUTPUT_PATH': str(tmp_path), 'SITEURL': ''}

        generate_search_index(generator)

        with open(tmp_path / 'search_index.json') as f:
            data = json.load(f)

        assert data['articles'][0]['description'] is None

    def test_summary_with_html(self, tmp_path):
        """HTML in summary should be stripped."""
        article = MockArticle(
            "HTML Summary", "html-summary", "2024/01/01/html-summary/",
            "Tech", ["test"],
            "<p>This has <strong>HTML</strong> tags.</p>",
            {},
        )
        generator = MagicMock()
        generator.context = {'articles': [article]}
        generator.settings = {'OUTPUT_PATH': str(tmp_path), 'SITEURL': ''}

        generate_search_index(generator)

        with open(tmp_path / 'search_index.json') as f:
            data = json.load(f)

        summary = data['articles'][0]['summary']
        assert 'HTML' in summary
        assert '<strong>' not in summary
        assert '<p>' not in summary

    def test_summary_empty(self, tmp_path):
        """Empty summary should be empty string."""
        article = MockArticle(
            "Empty Sum", "empty-sum", "2024/01/01/empty-sum/",
            "Tech", ["test"], "", {},
        )
        generator = MagicMock()
        generator.context = {'articles': [article]}
        generator.settings = {'OUTPUT_PATH': str(tmp_path), 'SITEURL': ''}

        generate_search_index(generator)

        with open(tmp_path / 'search_index.json') as f:
            data = json.load(f)

        assert data['articles'][0]['summary'] == ''

    def test_no_articles(self, tmp_path):
        """No articles should produce empty index."""
        generator = MagicMock()
        generator.context = {'articles': []}
        generator.settings = {'OUTPUT_PATH': str(tmp_path), 'SITEURL': ''}

        generate_search_index(generator)

        with open(tmp_path / 'search_index.json') as f:
            data = json.load(f)

        assert data['articles'] == []

    def test_output_path_created(self, tmp_path):
        """Output directory should be created if it doesn't exist."""
        nested = tmp_path / 'nested' / 'path'
        generator = MagicMock()
        generator.context = {'articles': []}
        generator.settings = {'OUTPUT_PATH': str(nested), 'SITEURL': ''}

        generate_search_index(generator)

        assert nested.exists()
        assert (nested / 'search_index.json').exists()

    def test_json_validity(self, tmp_path):
        """Generated JSON should be valid and parseable."""
        articles = [
            MockArticle(
                f"Post {i}", f"post-{i}", f"2024/01/{i:02d}/post-{i}/",
                "Category", ["tag"], "<p>Summary</p>",
                {'description': f'Desc {i}'},
            )
            for i in range(10)
        ]
        generator = MagicMock()
        generator.context = {'articles': articles}
        generator.settings = {'OUTPUT_PATH': str(tmp_path), 'SITEURL': ''}

        generate_search_index(generator)

        # Verify it's valid JSON
        with open(tmp_path / 'search_index.json') as f:
            data = json.load(f)
        assert len(data['articles']) == 10

    def test_article_url_format(self, tmp_path):
        """Article URL should start with /."""
        article = MockArticle(
            "Test", "test", "2024/01/15/test/",
            "Tech", ["x"], "<p>S</p>", {},
        )
        generator = MagicMock()
        generator.context = {'articles': [article]}
        generator.settings = {'OUTPUT_PATH': str(tmp_path), 'SITEURL': ''}

        generate_search_index(generator)

        with open(tmp_path / 'search_index.json') as f:
            data = json.load(f)
        assert data['articles'][0]['url'].startswith('/')


# ─── register ────────────────────────────────────────────────────────────────

class TestRegister:
    def test_register_connects_signal(self):
        """register() should connect to the right signal."""
        with patch('pelican.signals.article_generator_finalized.connect') as mock_connect:
            register()
            mock_connect.assert_called_once_with(generate_search_index)
