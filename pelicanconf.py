AUTHOR = 'Ryan Buckley'
SITENAME = 'rbucks.com'
SITEURL = 'https://rbucks.com'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('LinkedIn', 'https://www.linkedin.com/in/rbuckley'),
    ('Twitter/X', 'https://x.com/rbucks'),
)

DEFAULT_PAGINATION = 8

# Graymill theme specific settings
SITEDESCRIPTION = 'I like writing and building things.'
DISPLAY_SUMMARY = True
DISPLAY_PAGES_ON_MENU = True

# Use relative URLs for development
RELATIVE_URLS = True

# Theme
THEME = 'themes/rbucks-v2'

# Article settings - preserve WordPress URL structure for SEO
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Page settings
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Static paths
STATIC_PATHS = ['images']

# Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['liquid_tags', 'search_index_generator', 'readtime']

# Liquid tags configuration
LIQUID_TAGS = ["youtube"]

# Markdown extensions
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

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
    ('Email',    'mailto:rbucks@gmail.com'),
)

DIRECT_TEMPLATES = ['index', 'archives', 'categories', 'search']