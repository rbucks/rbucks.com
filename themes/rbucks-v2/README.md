# rbucks v2 — Pelican theme

A newspaper-simple redesign of rbucks.com. Drop-in for your existing Pelican setup.

## What's in this folder

```
pelican-theme/
├── static/
│   └── css/
│       └── site.css            ← single stylesheet, all rules
└── templates/
    ├── base.html               ← masthead + nav + footer skeleton
    ├── index.html              ← homepage (lede + lead story + year-grouped list)
    ├── article.html            ← single post (centered head, deck, body, related)
    ├── archives.html           ← full chronological archive grouped by year
    ├── categories.html         ← list of all categories
    ├── category.html           ← single category page
    ├── tag.html                ← tag pages
    ├── page.html               ← About + other static pages
    └── search.html             ← Fuse.js client-side search
```

## Install (3 minutes)

### 1. Drop it into your Pelican site

Rename `pelican-theme/` to `rbucks-v2/` and put it in your themes folder:

```
rbucks.com/
├── content/
├── pelicanconf.py
├── plugins/
│   └── search_index_generator.py     ← already there, keep it
└── themes/
    ├── graymill/                     ← your old theme, leave it
    └── rbucks-v2/                    ← drop the unzipped folder here
```

### 2. Switch the theme in `pelicanconf.py`

Change one line:

```python
THEME = 'themes/rbucks-v2'    # was 'themes/graymill'
```

That's the minimum. Everything else you already have (`SITENAME`, `AUTHOR`, `LINKS`, `PLUGINS`, the article URL scheme, the `search_index_generator` plugin) keeps working unchanged.

### 3. Optional theme settings

Add any of these to `pelicanconf.py` to fine-tune the design:

```python
# Masthead chrome
MASTHEAD_VOLUME   = 'Vol. XVII'
MASTHEAD_LOCATION = 'Lafayette, California'
MASTHEAD_TAGLINE  = 'Writing since 2008'

# Homepage lede block (above the lead story)
HOMEPAGE_LEDE_TITLE = 'I like writing and building things.'
HOMEPAGE_LEDE       = ('Notes from a parallel entrepreneur — on companies, '
                       'family, climate, food, and the slow work of figuring '
                       'out what to do with the next ten years.')

# Per-category descriptions used on category.html and categories.html
CATEGORY_DESCRIPTIONS = {
    'Business':  'Founders, fundraising, failure, and the slow work of building.',
    'Personal':  'Birthdays, milestones, the inside of my head.',
    'Family':    'Marriage, kids, Lafayette.',
    'Politics':  'Housing, climate, Contra Costa County.',
    'Food':      'Recipes I want to remember.',
    'Health':    'Cancer, recovery, sleep.',
    'Lifestyle': 'Books, posts, and games.',
    'Technology':'AI, code, and tools.',
}

# Cache-bust the stylesheet on every build (recommended)
import time
SITE_VERSION = str(int(time.time()))

# Footer social links — already in your config as LINKS, the theme reads them.
LINKS = (
    ('Twitter',  'https://x.com/rbucks'),
    ('LinkedIn', 'https://www.linkedin.com/in/rbuckley'),
    ('Email',    'mailto:ryan@rbucks.com'),
)
```

### 4. Make `search.html` a direct template

So Pelican generates `/search.html` (the search page). Add `'search'` to your direct templates:

```python
DIRECT_TEMPLATES = ['index', 'archives', 'categories', 'search']
```

The page loads `/search_index.json`, which your existing `search_index_generator` plugin already builds — nothing else needed.

### 5. Build

```bash
pelican content
```

## Per-article front matter

Standard Pelican fields work as expected. Two optional extras the theme reads:

```markdown
Title:    The view from 35
Date:     2017-08-27
Category: Personal
Tags:     reflection, family, lafayette
Author:   Ryan Buckley
Summary:  A melancholy birthday in Boston, a contented one in Lafayette...

Subtitle: Reflection                ← optional, shows in article kicker
Deck:     A melancholy birthday...  ← optional, replaces Summary as the article deck
```

If `Deck:` isn't set, the theme uses `Summary:` as the deck. If neither is set, the deck is just omitted.

## Reading time (optional)

If you want the "X min read" line in the byline, install:

```bash
pip install pelican-readtime
```

and add to `PLUGINS`:

```python
PLUGINS = ['liquid_tags', 'search_index_generator', 'readtime']
```

Without the plugin, that part of the byline silently disappears.

## Customizing visuals

All design tokens live at the top of `static/css/site.css`:

```css
:root {
  --paper:    #ffffff;
  --ink:      #111111;
  --ink-mid:  #555555;
  --rule:     #e2e2e2;

  --display:  "Playfair Display", Times, serif;
  --serif:    "Source Serif 4", Georgia, serif;
  --sans:     "Inter", system-ui, sans-serif;

  --measure:      38rem;     /* article body width */
  --measure-wide: 56rem;     /* article head width */
}
```

Change those and the whole site re-themes.

## Switching back

`THEME = 'themes/graymill'` and rebuild. Nothing in `content/` changed.

## Notes

- **Fonts** load from Google Fonts inside `site.css`. No extra `<link>` tags needed.
- **Search** is fully client-side — uses your existing `search_index_generator` plugin and Fuse.js (loaded from jsDelivr).
- **URL structure** is preserved. The theme uses Pelican's standard URL helpers (`article.url`, `category.url`, `tag.url`), so your existing `ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'` rule keeps working and SEO doesn't move.
- **Pagination** works automatically when `DEFAULT_PAGINATION` is set.
- **Dates** in `archives.html` use `strftime('%b %-d')` (e.g. "Apr 14"). On Windows replace `%-d` with `%#d` if Pelican errors.
