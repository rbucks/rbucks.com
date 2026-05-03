"""Shared fixtures for tests."""
import os
import tempfile
import pytest


# Sample markdown posts for testing

SAMPLE_POST_WITH_ALL = """Title: Test Post
Date: 2024-01-15 10:00
Slug: test-post
Category: Business
Tags: testing, pytest
Description: Custom SEO description for test post.
Summary: A short summary for listing pages.

This is the first paragraph of the post. It has some interesting content that describes what the post is about.

This is the second paragraph. It goes into more detail about the topic.
"""

SAMPLE_POST_NO_DESC = """Title: Missing Description
Date: 2023-06-01 14:30
Slug: missing-description
Category: Personal
Tags: writing, thoughts
Summary: A summary without a description.

This is the first paragraph of the post body. It contains the main idea and should be used as the auto-generated description.

Here is another paragraph that continues the discussion.
"""

SAMPLE_POST_NO_SUMMARY = """Title: No Summary Either
Date: 2025-12-29 10:00
Slug: no-summary
Category: Technology
Tags: AI, coding

I haven't written anything here about artificial intelligence, even though I use it every day. My work life is entirely dependent on it now.
"""

SAMPLE_POST_MARKDOWN = """Title: Markdown Heavy
Date: 2022-03-15 08:00
Slug: markdown-heavy
Category: Business
Tags: testing

This post has **bold text**, *italic text*, and a [link to somewhere](https://example.com).

> A blockquote that should be stripped.

![An image]({static}/images/photo.jpg)

More regular content here.
"""

SAMPLE_POST_EMPTY_BODY = """Title: Empty Body
Date: 2024-01-01 00:00
Slug: empty-body
Category: Personal
Tags: test
"""

SAMPLE_POST_ONELINE = """Title: One Liner
Date: 2024-06-15 12:00
Slug: one-liner
Category: Business
Tags: short

Short.
"""

SAMPLE_POST_EXACT_LENGTH = """Title: Long Content
Date: 2024-01-01 00:00
Slug: long-content
Category: Technology
Tags: testing

""" + ("This is a very long sentence that should definitely exceed the maximum description length of one hundred and sixty characters because it just keeps going and going without any sign of stopping anytime soon. " * 5)

SAMPLE_POST_HTML_IN_BODY = """Title: HTML Content
Date: 2024-01-01 00:00
Slug: html-content
Category: Technology
Tags: html

<p>This paragraph has <strong>HTML tags</strong> that should be stripped from the description.</p>
<p>Second paragraph with more content.</p>
"""

SAMPLE_POST_NO_FRONTMATTER = """This is a post with no frontmatter at all.

It just starts with content directly.
"""

SAMPLE_POST_HEADER_IN_CONTENT = """Title: Header Content
Date: 2024-01-01 00:00
Slug: header-content
Category: Business
Tags: testing

## This is a heading

And this is a paragraph after a heading.
"""


@pytest.fixture
def temp_dir():
    """Create a temporary directory for test files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir


def write_temp_post(temp_dir, filename, content):
    """Write a test markdown file to a temp directory."""
    filepath = os.path.join(temp_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return filepath
