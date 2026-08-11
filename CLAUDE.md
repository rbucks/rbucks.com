# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is Ryan Buckley's personal blog website (rbucks.com) built with Pelican, a Python-based static site generator. The site uses a custom theme called "rbucks-v2" and is deployed via GitHub Pages with automated CI/CD.

## Architecture

**Static Site Generation**: Pelican processes Markdown content files into static HTML using Jinja2 templates.

**Content Structure**: Blog posts are Markdown files in `/content/` with metadata headers (Title, Date, Slug, Category, Tags, Description, Summary). The site maintains WordPress-style URL structure for SEO preservation: `{year}/{month}/{day}/{slug}/`.

**Theme System**: Uses custom "rbucks-v2" theme in `/themes/rbucks-v2/`, set via `THEME` in `pelicanconf.py`. A newspaper-style design with:
- A single stylesheet, `static/css/site.css` — there is no sidebar anywhere in this theme
- Centered, measure-constrained columns (`--measure` for body, `--measure-wide` for heads)
- A masthead with volume/location/tagline, a top nav, and a footer
- Nine Jinja2 templates, one per page type
- A dedicated `/search.html` page (Fuse.js), not a sidebar widget

`/themes/graymill/` is the previous theme. It is retained but inactive — do not edit it expecting changes to appear on the site. `themes/rbucks-v2/README.md` documents the theme's own settings in more detail.

**Deployment Strategy**: Fully automated via GitHub Actions - never edit `/docs/` directly. The workflow builds the site using `publishconf.py` and deploys to GitHub Pages.

## Essential Commands

**Local Development**:
```bash
# Development server with auto-reload
make devserver

# Build for development (relative URLs)
make html

# Build for production
make publish

# Clean generated files
make clean
```

**Running Tests**:
```bash
# Run all tests (activate venv first)
source .venv/bin/activate && make test

# Or run directly
source .venv/bin/activate && python3 -m pytest tests/ -v

# Run a specific test file
source .venv/bin/activate && python3 -m pytest tests/test_add_descriptions.py -v

# Run a specific test class
source .venv/bin/activate && python3 -m pytest tests/test_add_descriptions.py::TestGenerateDescription -v
```

**Content Management**:
```bash
# Add new blog post
# Create .md file in /content/ with metadata header:
# Title: Post Title
# Date: YYYY-MM-DD HH:MM
# Slug: post-slug
# Category: category-name
# Tags: tag1, tag2
# Description: Optional SEO-friendly description (used in search results)
# Summary: Optional auto-displayed summary on listing pages

# Auto-generate Description for posts missing it
source .venv/bin/activate && python3 add_descriptions.py

# Save as draft (won't be published)
# Add Status: draft to metadata header:
# Title: Post Title
# Date: YYYY-MM-DD HH:MM
# Slug: post-slug
# Category: category-name
# Tags: tag1, tag2
# Description: Optional description
# Summary: Optional summary
# Status: draft
```

**Deployment**:
```bash
# Deploy changes (triggers GitHub Actions)
git add .
git commit -m "Description of changes"
git push origin main
```

## Configuration Files

- `pelicanconf.py`: Development settings with relative URLs
- `publishconf.py`: Production settings with absolute URLs, inherits from pelicanconf.py
- `Makefile`: Build and development commands
- `.github/workflows/pelican.yml`: Automated deployment pipeline

## Content Guidelines

**URL Structure**: Maintains WordPress format `/{year}/{month}/{day}/{slug}/` for SEO continuity.

**Categories**: Exactly eight, capitalized as shown — Business, Family, Food, Health, Lifestyle, Personal, Politics, Technology. Each has a description in `CATEGORY_DESCRIPTIONS` in `pelicanconf.py`, keyed on these exact strings. Adding a new category means adding it there too, or its pages render without a description.

**Metadata**: All posts require Title, Date, Slug, Category, and Tags in the header. Optional fields: Description (SEO/search snippet auto-generated from first paragraph if missing), Summary (shown on listing pages).

**Search**: The site has a dedicated client-side search page at `/search.html` powered by Fuse.js, reachable from the top nav. Every build generates `/search_index.json` with article metadata. The search covers: title, category, tags, description (from explicit `Description:` field), and summary (from `Summary:` field or auto-generated).

**Description Auto-Generation**: Run `source .venv/bin/activate && python3 add_descriptions.py` to backfill `Description:` frontmatter on any posts missing it. The script extracts the first paragraph from the post body, strips markdown, and truncates at ~160 chars.

## Theme Customization

**CSS**: All styles live in one file, `/themes/rbucks-v2/static/css/site.css` (~735 lines). Design tokens are defined in `:root` at the top — change them and the whole site re-themes:

```css
--paper, --ink, --ink-soft, --ink-mid, --ink-faint, --rule, --rule-mid   /* color */
--display  /* Playfair Display — headlines */
--serif    /* Source Serif 4 — body */
--sans     /* Inter — UI/meta */
--measure       /* 38rem — article body width */
--measure-wide  /* 56rem — article head width */
```

The stylesheet is cache-busted per build via `SITE_VERSION` in `pelicanconf.py`, appended as `site.css?v=...`.

**Templates**: Located in `/themes/rbucks-v2/templates/`
- `base.html`: masthead (volume/location/tagline), top nav (Home, Archives, Categories, static pages, Search), and footer with `LINKS`
- `index.html`: homepage — lede block, lead story, then posts grouped by year
- `article.html`: single post — kicker, deck, byline, body, and up to 3 related posts from the same category
- `categories.html` / `category.html`: both read `CATEGORY_DESCRIPTIONS` from `pelicanconf.py` via an **exact string key** (`CATEGORY_DESCRIPTIONS[category|string]`), which is why `Category:` casing must match the dict keys exactly
- `archives.html`, `tag.html`, `page.html`, `search.html`

**Theme settings in `pelicanconf.py`**: `MASTHEAD_VOLUME`, `MASTHEAD_LOCATION`, `MASTHEAD_TAGLINE`, `HOMEPAGE_LEDE_TITLE`, `HOMEPAGE_LEDE`, `CATEGORY_DESCRIPTIONS`, `SITE_VERSION`, `LINKS`.

**Optional per-article frontmatter the theme reads**: `Subtitle:` (shows in the article kicker) and `Deck:` (replaces `Summary:` as the article deck). If neither `Deck:` nor `Summary:` is set, the deck is omitted.

**External assets**: Fonts load from Google Fonts via `@import` at the top of `site.css`. Fuse.js loads from jsDelivr in `search.html`. Both are the only external dependencies.

**Static Assets**: `STATIC_PATHS = ['images']`, so `content/images/` is copied to the output root. Post images are referenced as `{static}/images/{year}/{month}/name.jpeg`. Note: `rbucks-v2` does not currently link a favicon — the only `favicon.ico` in the repo belongs to the inactive `graymill` theme.

## Deployment Notes

**Never Edit `/docs/` Directly**: This directory is auto-generated by GitHub Actions. Always edit source files and push to trigger deployment.

**GitHub Actions Workflow**: Automatically triggered on push to main branch, builds site with production settings, and deploys to GitHub Pages.

**Custom Domain**: Site uses `rbucks.com` domain configured via CNAME file generated during build.

## Collaborative Writing Workflow

**Notation System**: Use `<<Claude: action>>` format to leave editing notes for Claude to process.

**Examples:**
```markdown
I used to believe venture capital was bad <<Claude: link to post about venture capital or funding>> but now I think differently.

The history of venture capital is complex <<Claude: explain venture capital history in 3 sentences>>.

I wrote about this before <<Claude: find post about entrepreneurship and funding>>.

This reminds me of what happened with Scripted <<Claude: link to "being the other co-founder" post>>.
```

**Action Types:**
- `<<Claude: link to post about [topic]>>` - Find and link to relevant post
- `<<Claude: find post titled "[title]">>` - Link to specific post by title
- `<<Claude: explain [topic] in X sentences>>` - Add explanatory content
- `<<Claude: research [topic]>>` - Add factual information
- `<<Claude: expand on [topic]>>` - Add more detail
- `<<Claude: fact-check this>>` - Verify information

**Processing Workflow:**
1. You write with `<<Claude: action>>` notes in your draft
2. Claude searches `/content/` directory for relevant posts by keywords, titles, categories, tags, and content similarity
3. Claude replaces notes with actual Markdown links `[text](url)` or requested content
4. Claude ensures that all SEO frontmatter exists and is complete:
   - Required: Title, Date, Slug, Category, Tags
   - Optional but recommended: Description, Summary
   - For category, use ONLY these categories, capitalized exactly as shown: Business, Family, Food, Health, Lifestyle, Personal, Politics, Technology
   - Capitalization matters: `CATEGORY_DESCRIPTIONS` in `pelicanconf.py` is keyed on these exact strings. A lowercase `Category:` value silently drops the description on the category pages and displays the category in lowercase.
5. Claude returns the word count, readability, and overall assessment of the post.
6. You review changes before committing

**Note on Description**: If no `Description:` field exists, Claude should generate one from the first paragraph of content (stripping markdown, truncating at ~160 chars at a sentence boundary). The Description is used for search results and SEO.

## Draft Workflow

**Saving Drafts**: Add `Status: draft` to the frontmatter to prevent posts from being published while you're working on them.

**Draft Examples:**
```markdown
Title: My Unfinished Post  
Date: 2025-06-30 14:30
Slug: my-unfinished-post
Category: Personal
Tags: writing, draft
Description: Optional description for search
Status: draft

Content with <<Claude: action>> notes...
```

**Publishing Drafts**: Remove the `Status: draft` line when ready to publish.

**Testing**: Run `make html` locally to verify draft posts are excluded from the build.

## File Structure Context

- `/content/`: Markdown blog posts with metadata headers
- `/themes/rbucks-v2/`: The active theme — templates, `static/css/site.css`, and its own README
- `/themes/graymill/`: Previous theme, inactive (kept for reference only)
- `/plugins/search_index_generator.py`: Pelican plugin that generates `search_index.json` for client-side search
- `/add_descriptions.py`: Script to auto-generate Description frontmatter on posts missing it
- `/docs/`: Auto-generated output directory (do not edit manually)
- `/plugins/`: Pelican plugins for custom features
- `tests/`: Test suite (pytest) for search plugin and description script

## GitHub Actions

**Deployment Workflow**:
- The publishing GitHub Actions flow automates the entire site deployment process
- Triggered automatically on push to the main branch
- Builds the site using production configuration
- Generates static files and deploys to GitHub Pages
- Ensures consistent and reproducible site builds
- Handles custom domain configuration
- Automatically applies production-level optimizations