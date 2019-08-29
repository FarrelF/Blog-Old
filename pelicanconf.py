#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import pymdownx.emoji as emojis
from datetime import datetime

AUTHOR = 'Farrel Franqois'

# Mengenai Blog
SITENAME = 'Farrel Franqois Blog'
SITETITLE = 'Farrel Franqois Blog'
SITESUBTITLE = 'Sekedar blog pribadi saya'
SITEURL = 'http://localhost:8000' # Saya isikan dengan 'localhost:8000' agar blog bisa di akses secara Offline

IGNORE_FILES = ['.#*', '*draf*'] # Mengabaikan Berkas

DEFAULT_METADATA = {
    'status': 'draft',
    'author': 'Farrel Franqois'
}

USE_CDN = False

PATH = 'content'

# Artikel
ARTICLE_PATHS = ['artikel']
ARTICLE_SAVE_AS = '{slug}.html'
ARTICLE_LANG_SAVE_AS = '{slug}/{lang}.html'
ARTICLE_URL = '{slug}'
ARTICLE_LANG_URL = '{slug}/{lang}'

# Penulis
AUTHOR_SAVE_AS = 'penulis/{slug}.html'
AUTHOR_URL = 'penulis/{slug}'

# Kategori
CATEGORY_URL = 'kategori/{slug}'
CATEGORY_SAVE_AS = 'kategori/{slug}.html'

#Tag
TAG_SAVE_AS = 'tag/{slug}.html'
TAG_URL = 'tag/{slug}'

# Halaman
PAGE_PATHS = ['halaman']
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_SAVE_AS = '{slug}/{lang}.html'
PAGE_URL = '{slug}'
PAGE_LANG_URL = '{slug}/{lang}'

# Lokasi Berkas Statis
STATIC_PATHS = [
    'img',
    'extras/CNAME',
    'extras/favicon.ico',
    'extras/robots.txt'
]

EXTRA_PATH_METADATA = {
    'extras/CNAME': {'path': 'CNAME'},
    'extras/favicon.ico': {'path': 'favicon.ico'},
    'extras/robots.txt': {'path': 'robots.txt'}
}

THEME = 'Flex' # Nama Tema yang di gunakan
MAIN_MENU = True

# Pengaturan Waktu
TIMEZONE = 'Asia/Jakarta' # Zona Waktu yang di gunakan
DEFAULT_DATE = 'fs'

DISABLE_URL_HASH = True # Menonaktifkan Tanda Pagar pada Link URL setiap ke artikel/halaman
CHECK_MODIFIED_METHOD = 'sha256'

# Plugin dan Konfigurasi nya
PLUGIN_PATHS = ['plugins']
PLUGINS = ['extended_sitemap']
EXTENDED_SITEMAP_PLUGIN = {
    'priorities': {
        'index': 1.0,
        'articles': 0.8,
        'pages': 0.5,
        'others': 0.4
    },
    'changefrequencies': {
        'index': 'daily',
        'articles': 'weekly',
        'pages': 'monthly',
        'others': 'monthly',
    }
}

# Pengaturan Markdown
MARKDOWN = {
  'extension_configs': {
    'markdown.extensions.toc': {
      'title': 'Daftar Isi:'
    },
    'markdown.extensions.codehilite': {'css_class': 'highlight'},
    'markdown.extensions.meta': {},
    'pymdownx.emoji': {
      'emoji_index': emojis.twemoji,
      'emoji_generator': emojis.to_svg,
      'alt': 'short',
      'options': {
        "attributes": {
            "height": "20px",
            "width": "20px"
        },
        'classes': 'twemoji_emojis',
        "image_path": "https://cdn.statically.io/libs/twemoji/12.0.4/2/svg/",
      },
    },
  },
  'output_format': 'html5',
}

# Hak Cipta
COPYRIGHT_YEAR = f'{datetime.now().year}'
COPYRIGHT_NAME = 'Farrel Franqois'
CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike (CC BY-SA)',
    'version': '4.0',
    'slug': 'by-sa',
    'distribution-type': 'local'
} # Implementasi Lisensi dari Creative Commons

# Pengaturan Bahasa dan Lokalisasi
DEFAULT_LANG = 'id'
OG_LOCALE = 'id_ID'
LOCALE = 'id_ID'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PYGMENTS_STYLE = 'friendly' # Tampilan Pygments yang merupakan Syntax Highlighter

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
