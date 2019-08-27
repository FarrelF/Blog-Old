#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = 'Farrel Franqois'
SITENAME = 'Farrel Franqois Blog'
SITETITLE = 'Farrel Franqois Blog'
SITESUBTITLE = 'Sekedar blog pribadi saya'
SITEURL = 'http://localhost:8000'
STATIC_PATHS = ['../CNAME']
EXTRA_PATH_METADATA = {'../CNAME': {'path': 'CNAME'}}
IGNORE_FILES = ['.#*', '*draf*']

USE_CDN = False

PATH = 'content'
ARTICLE_PATHS = ['artikel']
ARTICLE_SAVE_AS = '{slug}.html'
ARTICLE_LANG_SAVE_AS = '{slug}/{lang}.html'
ARTICLE_URL = '{slug}'
ARTICLE_LANG_URL = '{slug}/{lang}'

AUTHOR_SAVE_AS = 'penulis/{slug}.html'
AUTHOR_URL = 'penulis/{slug}'

CATEGORY_URL = 'kategori/{slug}'
CATEGORY_SAVE_AS = 'kategori/{slug}.html'

TAG_SAVE_AS = 'tag/{slug}.html'
TAG_URL = 'tag/{slug}'

PAGE_PATHS = ['halaman']
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_SAVE_AS = '{slug}/{lang}.html'
PAGE_URL = '{slug}'
PAGE_LANG_URL = '{slug}/{lang}'

STATIC_PATHS = ['gambar']
THEME = 'Flex'
TIMEZONE = 'Asia/Jakarta'
MAIN_MENU = True

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike (CC BY-SA)',
    'version': '4.0',
    'slug': 'by-sa',
    'distribution-type': 'local'
}

DISABLE_URL_HASH = True

COPYRIGHT_YEAR = f'{datetime.now().year}'
COPYRIGHT_NAME = 'Farrel Franqois'

DEFAULT_LANG = 'id'
OG_LOCALE = 'id_ID'
LOCALE = 'id_ID'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PYGMENTS_STYLE = 'friendly'

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
          ('facebook', 'https://www.facebook.com/FarrelFranqois'),
          ('twitter', 'https://twitter.com/FarrelFranqois'),
         )

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
