"""
Search Index Generator Plugin for Pelican

Generates a search_index.json file with article metadata (title, slug, url,
category, tags, date, description/summary) for client-side search via Fuse.js.

The search index includes both:
  - summary: from Pelican's auto-generated or explicit Summary: field
  - description: from explicit Description: frontmatter field (if present)
"""
import json
import os
import re
from pelican import signals


def strip_html(text):
    """Remove HTML tags from text."""
    return re.sub(r'<[^>]+>', '', text).strip()


def get_article_summary(article):
    """Get article summary without triggering {static} resolution.

    For articles with an explicit Summary: field, use the metadata value.
    For auto-generated summaries, extract from raw content to avoid
    triggering full content rendering (which would warn about missing
    static files before the static generator has run).
    """
    if 'summary' in article.metadata:
        # Use explicit summary from frontmatter
        return strip_html(article.metadata['summary'])
    # Fall back to raw content for a simple text summary
    raw = getattr(article, '_content', '') or ''
    if not raw:
        return ''
    # Strip markdown-ish formatting and truncate
    text = re.sub(r'!\[.*?\]\(.*?\)', '', raw)  # images
    text = re.sub(r'\[([^\]]*?)\]\(.*?\)', r'\1', text)  # links
    text = re.sub(r'<[^>]+>', '', text)  # HTML
    text = re.sub(r'[#>*_]+', '', text)  # headings, bold, lists
    text = re.sub(r'\s+', ' ', text).strip()
    return text[:300]  # reasonable summary length


def generate_search_index(generator):
    """Build a search index JSON file from all articles."""
    articles = generator.context.get('articles', [])
    siteurl = generator.settings.get('SITEURL', '')

    index = {
        'articles': [
            {
                'title': article.title,
                'slug': article.slug,
                'url': '/' + article.url,
                'category': article.category.name if article.category else '',
                'tags': [tag.name for tag in article.tags],
                'date': article.date.strftime('%Y-%m-%d'),
                'description': article.metadata.get('description', None),
                'summary': get_article_summary(article),
            }
            for article in articles
        ]
    }

    output_path = generator.settings['OUTPUT_PATH']
    os.makedirs(output_path, exist_ok=True)
    with open(os.path.join(output_path, 'search_index.json'), 'w',
              encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)


def register():
    signals.article_generator_finalized.connect(generate_search_index)
