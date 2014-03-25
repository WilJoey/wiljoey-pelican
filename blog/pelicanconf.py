#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'WilJoey'
SITENAME = u'WilJoey holiucan'
SITEURL = u''

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = u'zh'

# Specify theme
THEME=u'Pelican-Themes/bootstrap/'

# Plugins
PLUGIN_PATH = 'Pelican-Plugins/'
PLUGINS = ['neighbors', 'summary']


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/WilJoey'),
          ('github', 'https://github.com/WilJoey'),)
TWITTER_USERNAME = 'WilJoey'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


GITHUB_URL = 'https://github.com/WilJoey'
TAG_FEEDATOM  = 'feeds/%s.atom.xml'

# Formatting for urls

ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

# Generate yearly archive
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

# Show most recent posts first
NEWEST_FIRST_ARCHIVES = False


# global metadata to all the contents
DEFAULT_METADATA = (('yeah', 'it is'),)

# static paths will be copied under the same name
STATIC_PATHS = ["pictures", ]

# A list of files to copy from the source to the destination
FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)

# custom page generated with a jinja2 template
TEMPLATE_PAGES = {'pages/jinja2_template.html': 'jinja2_template.html'}