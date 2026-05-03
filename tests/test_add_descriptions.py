"""Tests for the add_descriptions.py script."""
import os
import sys
import pytest

# Ensure the project root is on sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from add_descriptions import (
    parse_frontmatter_and_body,
    frontmatter_to_dict,
    has_description,
    generate_description,
    process_file,
    MAX_DESC_LENGTH,
)

from tests.conftest import (
    SAMPLE_POST_WITH_ALL,
    SAMPLE_POST_NO_DESC,
    SAMPLE_POST_NO_SUMMARY,
    SAMPLE_POST_MARKDOWN,
    SAMPLE_POST_EMPTY_BODY,
    SAMPLE_POST_ONELINE,
    SAMPLE_POST_EXACT_LENGTH,
    SAMPLE_POST_HTML_IN_BODY,
    SAMPLE_POST_NO_FRONTMATTER,
    SAMPLE_POST_HEADER_IN_CONTENT,
    write_temp_post,
)


# ─── parse_frontmatter_and_body ──────────────────────────────────────────────

class TestParseFrontmatterAndBody:
    def test_basic_frontmatter(self):
        """Standard frontmatter with all fields."""
        fm, body = parse_frontmatter_and_body(SAMPLE_POST_WITH_ALL)
        assert len(fm) == 7
        assert fm[0] == 'Title: Test Post'
        assert body.startswith('This is the first paragraph')

    def test_no_frontmatter(self):
        """No frontmatter at all."""
        fm, body = parse_frontmatter_and_body(SAMPLE_POST_NO_FRONTMATTER)
        assert fm == []
        assert body.startswith('This is a post with no frontmatter')

    def test_empty_frontmatter(self):
        """Empty string."""
        fm, body = parse_frontmatter_and_body('')
        assert fm == []
        assert body == ''

    def test_frontmatter_only_no_body(self):
        """Frontmatter with no body content after blank line."""
        text = "Title: Only\nDate: 2024-01-01\nSlug: only\nCategory: Test\nTags: test\n\n"
        fm, body = parse_frontmatter_and_body(text)
        assert len(fm) == 5
        assert body == ''

    def test_fields_with_colons_in_value(self):
        """Fields whose values contain colons (e.g. dates, URLs)."""
        text = "Title: My Post\nDate: 2024-01-01 12:30:00\nSlug: my-post\nCategory: Blog\nTags: test\n\nBody content."
        fm, body = parse_frontmatter_and_body(text)
        assert len(fm) == 5
        assert 'Date:' in fm[1]
        assert body == 'Body content.'

    def test_fields_with_extra_spaces(self):
        """Fields with extra whitespace."""
        text = "Title:  Spaced Out  \nDate: 2024-01-01\nSlug: spaced-out\nCategory:  Test  \nTags:  spaced, out  \n\nBody."
        fm, body = parse_frontmatter_and_body(text)
        assert len(fm) == 5

    def test_multiple_blank_lines(self):
        """Multiple blank lines between frontmatter and body."""
        text = "Title: Blank\nDate: 2024-01-01\nSlug: blank\nCategory: Test\nTags: test\n\n\n\n\nBody after multiple blanks."
        fm, body = parse_frontmatter_and_body(text)
        assert len(fm) == 5
        assert body == '\n\n\nBody after multiple blanks.'


# ─── frontmatter_to_dict ─────────────────────────────────────────────────────

class TestFrontmatterToDict:
    def test_basic(self):
        """Standard conversion."""
        fm, _ = parse_frontmatter_and_body(SAMPLE_POST_WITH_ALL)
        d = frontmatter_to_dict(fm)
        assert d['Title'] == 'Test Post'
        assert d['Slug'] == 'test-post'
        assert d['Category'] == 'Business'
        assert 'testing, pytest' in d['Tags']

    def test_empty_list(self):
        """Empty frontmatter list."""
        d = frontmatter_to_dict([])
        assert d == {}

    def test_malformed_line(self):
        """Line without a colon should be skipped."""
        lines = ['Title: Valid', 'This is not frontmatter', 'Tags: test']
        d = frontmatter_to_dict(lines)
        assert 'Title' in d
        assert 'Tags' in d
        assert len(d) == 2

    def test_hyphenated_keys(self):
        """Keys with hyphens should work."""
        lines = ['Custom-Key: value', 'Another-Key: another']
        d = frontmatter_to_dict(lines)
        assert d['Custom-Key'] == 'value'


# ─── has_description ─────────────────────────────────────────────────────────

class TestHasDescription:
    def test_has_description(self):
        """Description exists."""
        fm, _ = parse_frontmatter_and_body(SAMPLE_POST_WITH_ALL)
        assert has_description(fm) is True

    def test_no_description(self):
        """Description is missing."""
        fm, _ = parse_frontmatter_and_body(SAMPLE_POST_NO_DESC)
        assert has_description(fm) is False

    def test_empty_list(self):
        """Empty frontmatter."""
        assert has_description([]) is False

    def test_no_summary(self):
        """Post without Summary (but should not affect Description check)."""
        fm, _ = parse_frontmatter_and_body(SAMPLE_POST_NO_SUMMARY)
        assert has_description(fm) is False


# ─── generate_description ────────────────────────────────────────────────────

class TestGenerateDescription:
    def test_basic_paragraph(self):
        """First paragraph should be used."""
        desc = generate_description("First paragraph here. It has content.\n\nSecond paragraph.")
        assert desc == "First paragraph here. It has content."

    def test_skip_short_first_para(self):
        """Short first paragraph should be skipped for longer second."""
        desc = generate_description("Short.\n\nThis is the real first paragraph with enough content to be meaningful for the description.")
        assert len(desc) >= 20

    def test_strip_image_tags(self):
        """Image markdown should be removed."""
        desc = generate_description("![alt](image.jpg) Real content here with enough words to pass the minimum length check.")
        assert desc.startswith("Real content here with enough words")

    def test_strip_links_keep_text(self):
        """Link markdown should keep text but remove URL."""
        desc = generate_description("Check out [this link](https://example.com) for more.")
        assert "this link" in desc
        assert "example.com" not in desc

    def test_strip_html(self):
        """HTML tags should be removed."""
        desc = generate_description("<p>This has <strong>HTML</strong> tags and enough text to pass the minimum length check threshold.</p>")
        assert "HTML" in desc
        assert "<p>" not in desc
        assert "<strong>" not in desc

    def test_strip_bold_italic(self):
        """Bold and italic markers should be removed."""
        desc = generate_description("This is **bold** and *italic* text.")
        assert "bold" in desc
        assert "italic" in desc
        assert "**" not in desc
        assert "*" not in desc

    def test_strip_heading_markers(self):
        """Heading markers should be removed."""
        desc = generate_description("## This is a heading\n\nSome content after heading.")
        assert desc.startswith("Some content after")

    def test_strip_blockquote(self):
        """Blockquote markers should be removed."""
        desc = generate_description("> A quoted paragraph with enough content to be meaningful for description text.")
        assert not desc.startswith(">")

    def test_truncate_long_text(self):
        """Long text should be truncated at ~160 chars."""
        long_text = "This is a very long sentence that should definitely exceed the maximum description length of one hundred and sixty characters because it just keeps going and going without any sign of stopping anytime soon. " * 5
        desc = generate_description(long_text)
        assert len(desc) <= MAX_DESC_LENGTH + 3  # allow for '...'

    def test_truncate_at_sentence_boundary(self):
        """Truncation should prefer sentence boundaries."""
        text = "First sentence with enough content. Second sentence that completes the thought. Third sentence that goes on and on and on and on and on and on and on and on and on and on and on and on."
        desc = generate_description(text)
        # Should end with a period (sentence boundary) or '...'
        assert desc.endswith('.') or desc.endswith('...')

    def test_empty_body(self):
        """Empty body returns empty string."""
        assert generate_description('') == ''

    def test_only_images(self):
        """Body with only images returns empty string."""
        desc = generate_description("![img1](a.jpg)\n\n![img2](b.jpg)")
        assert desc == ''

    def test_only_html_empty_tags(self):
        """Body with only empty HTML."""
        desc = generate_description("<div></div><span></span>")
        assert desc == ''

    def test_mixed_content(self):
        """Realistic mixed markdown content."""
        text = """## Introduction

This is the **main** paragraph that describes the post. It has a [link](https://example.com) and some *emphasis*.

> A blockquote that continues with relevant context.

More content here.
"""
        desc = generate_description(text)
        assert "main paragraph" in desc
        assert "link" in desc
        assert "emphasis" in desc
        assert "**" not in desc
        assert ">" not in desc

    def test_unicode_and_special_chars(self):
        """Unicode characters should be preserved."""
        desc = generate_description("Café résumé naïve — em dash … ellipsis 🎉")
        assert "Café" in desc
        assert "🎉" in desc


# ─── process_file (integration) ──────────────────────────────────────────────

class TestProcessFile:
    def test_dry_run_returns_preview(self, temp_dir):
        """Dry run should return preview without modifying file."""
        fp = write_temp_post(temp_dir, 'test.md', SAMPLE_POST_NO_DESC)
        result = process_file(fp, dry_run=True)
        assert result is not None
        assert 'file' in result
        assert 'description' in result
        # File should NOT have been modified
        with open(fp, 'r') as f:
            content = f.read()
        assert content == SAMPLE_POST_NO_DESC

    def test_skip_existing_description(self, temp_dir):
        """Posts with existing Description should be skipped."""
        fp = write_temp_post(temp_dir, 'test.md', SAMPLE_POST_WITH_ALL)
        result = process_file(fp, dry_run=True)
        assert result is None

    def test_skip_no_frontmatter(self, temp_dir):
        """Posts without frontmatter should be skipped."""
        fp = write_temp_post(temp_dir, 'test.md', SAMPLE_POST_NO_FRONTMATTER)
        result = process_file(fp, dry_run=True)
        assert result is None

    def test_skip_empty_body(self, temp_dir):
        """Posts with empty body should be skipped."""
        fp = write_temp_post(temp_dir, 'test.md', SAMPLE_POST_EMPTY_BODY)
        result = process_file(fp, dry_run=True)
        assert result is None

    def test_adds_description_after_tags(self, temp_dir):
        """Description should be inserted after Tags: line."""
        fp = write_temp_post(temp_dir, 'test.md', SAMPLE_POST_NO_DESC)
        result = process_file(fp, dry_run=False)
        assert result is not None
        with open(fp, 'r') as f:
            content = f.read()
        assert 'Description:' in content
        # Description should be after Tags:
        tags_pos = content.index('Tags:')
        desc_pos = content.index('Description:')
        assert desc_pos > tags_pos

    def test_adds_description_before_summary(self, temp_dir):
        """Description should be inserted before Summary when Tags not present."""
        text = """Title: Test
Date: 2024-01-01
Slug: test
Category: Business
Summary: A summary. for this test post about Description insertion.

Body content here with enough words to pass the minimum length threshold for description generation.
"""
        fp = write_temp_post(temp_dir, 'test.md', text)
        result = process_file(fp, dry_run=False)
        assert result is not None
        with open(fp, 'r') as f:
            content = f.read()
        assert 'Description:' in content
        # Summary should still be there
        assert 'Summary:' in content

    def test_adds_description_at_end_no_summary(self, temp_dir):
        """Description should go at end if no Tags or Summary."""
        text = """Title: Test
Date: 2024-01-01
Slug: test
Category: Business

Body content here with enough words to pass the minimum length threshold for description generation.
"""
        fp = write_temp_post(temp_dir, 'test.md', text)
        result = process_file(fp, dry_run=False)
        assert result is not None
        with open(fp, 'r') as f:
            content = f.read()
        assert 'Description:' in content
        assert 'Business' in content

    def test_preserves_existing_content(self, temp_dir):
        """The body content should be preserved after adding Description."""
        fp = write_temp_post(temp_dir, 'test.md', SAMPLE_POST_NO_DESC)
        process_file(fp, dry_run=False)
        with open(fp, 'r') as f:
            content = f.read()
        assert "This is the first paragraph" in content
        assert "Here is another paragraph" in content

    def test_multiple_posts(self, temp_dir):
        """Process multiple files, only those missing Description."""
        fp1 = write_temp_post(temp_dir, 'has.md', SAMPLE_POST_WITH_ALL)
        fp2 = write_temp_post(temp_dir, 'missing.md', SAMPLE_POST_NO_DESC)
        fp3 = write_temp_post(temp_dir, 'nofm.md', SAMPLE_POST_NO_FRONTMATTER)

        r1 = process_file(fp1, dry_run=False)
        r2 = process_file(fp2, dry_run=False)
        r3 = process_file(fp3, dry_run=False)

        assert r1 is None  # already has description
        assert r2 is not None  # added
        assert r3 is None  # no frontmatter

    def test_idempotent(self, temp_dir):
        """Running twice should not double-add Description."""
        fp = write_temp_post(temp_dir, 'test.md', SAMPLE_POST_NO_DESC)
        process_file(fp, dry_run=False)
        with open(fp, 'r') as f:
            first_run = f.read()

        # Second run should skip since Description now exists
        result = process_file(fp, dry_run=False)
        assert result is None

        with open(fp, 'r') as f:
            second_run = f.read()
        assert first_run == second_run
