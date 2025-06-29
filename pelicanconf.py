AUTHOR = 'Ryan Buckley'
SITENAME = 'rbucks.com'
SITEURL = 'https://www.rbucks.com'

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
    ('Twitter', 'https://twitter.com/rbucks'),
)

# Social widget - Graymill theme format
SOCIAL = (
    ('linkedin', 'https://www.linkedin.com/in/rbuckley'),
    ('twitter', 'https://twitter.com/rbucks'),
    ('facebook', 'https://www.facebook.com/rbucks'),
)

DEFAULT_PAGINATION = 8

# Graymill theme specific settings
SITEDESCRIPTION = 'Entrepreneur, writer, and builder'
DISPLAY_SUMMARY = True
DISPLAY_PAGES_ON_MENU = True

# Use relative URLs for development
RELATIVE_URLS = True

# Theme
THEME = 'themes/graymill'

# Article settings - preserve WordPress URL structure for SEO
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Page settings
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Static paths
STATIC_PATHS = ['images', 'extra']

# Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = []

# Markdown extensions
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}