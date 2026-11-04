#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
# For GitHub Pages with custom domain
SITEURL = 'https://rbucks.com'
# For GitHub Pages without custom domain, use:
# SITEURL = 'https://rbucks.github.io/rbucks.com'

RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Drafts remain available for local preview, but must not reach GitHub Pages.
# Status: draft alone still generates publicly accessible /drafts/ pages.
DRAFT_SAVE_AS = ''
DRAFT_LANG_SAVE_AS = ''
DRAFT_PAGE_SAVE_AS = ''
DRAFT_PAGE_LANG_SAVE_AS = ''

# GitHub Pages specific settings
OUTPUT_PATH = 'docs/'

# Following items are often useful when publishing
# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""
