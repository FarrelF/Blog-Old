#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://farrel.franqois.id'

# Penggunaan CDN
USE_CDN = True
CDN_THEME_REPO_BRANCH = 'b38b66f'
CDN_STATIC_THEME_URL = 'https://cdn.statically.io/gh/FarrelF/Modified-Flex/{0}/static'.format(CDN_THEME_REPO_BRANCH)
CDN_BLOG_BRANCH = '0d69c25'
CDN_STATIC_BLOG_URL = 'https://cdn.statically.io/gh/FarrelF/FarrelF-Blog/{0}'.format(CDN_BLOG_BRANCH)
CC_LICENSE['distribution-type'] = 'cdn'

# Pengaturan Font
USE_GOOGLE_CDN_FOR_FONTS = False
USE_MINIFIED_FONT_CSS = True

# URL Relatif
RELATIVE_URLS = False

# Feed/RSS
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

# Menambahkan Header saat di terbitkan nanti
STATIC_PATHS.append('extras/_headers')
EXTRA_PATH_METADATA['extras/_headers'] = {'path': '_headers'}

# Menambah Fitur Pengalihan saat di terbitkan nanti
STATIC_PATHS.append('extras/_redirects')
EXTRA_PATH_METADATA['extras/_redirects'] = {'path': '_redirects'}

# Menambah Berkas 'ads.txt' saat di terbitkan nanti
STATIC_PATHS.append('extras/ads.txt')
EXTRA_PATH_METADATA['extras/ads.txt'] = {'path': 'ads.txt'}

# Agar Berkas 'custom.css' tidak di buat di dalam folder 'output' saat di terbitkan nanti, jika menggunakan CDN
if USE_CDN:
    STATIC_PATHS.remove('extras/custom.css')
    del EXTRA_PATH_METADATA['extras/custom.css']

# Pengaturan Tema

# Mengatur Letak CSS yang di kustom
if USE_CDN:
    CUSTOM_CSS = 'content/extras/custom.min.css' 
else:
    CUSTOM_CSS = 'custom.min.css'
THEME = 'themes/Flex' # Nama dan lokasi Tema yang di gunakan, ini akan di gunakan untuk penerbitan/produksi

# Activating Cache
CACHE_PATH = '__cache__'
CACHE_CONTENT = True
GZIP_CACHE = True
LOAD_CONTENT_CACHE = True

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# Disqus
DISQUS_SITENAME = "FarrelF-Blog"
DISQUS_IN_PAGES = True # Mengaktifkan Disqus di dalam Laman

# Google
GOOGLE_ANALYTICS = "UA-97506869-1"
GOOGLE_ADSENSE = {
    'ca_id': 'ca-pub-2432124491852819',
    'page_level_ads': True,
    'ads': {
        'article_top': {                    # Iklan di Awal Artikel
            'slot_id': '6206076082',
            'ad_layout': 'in-article',
            'ad_format': 'fluid'
        },
        'article_bottom': {                 # Iklan di Akhir Artikel
            'slot_id': '5647672882',
            'ad_layout': 'in-article',
            'ad_format': 'fluid'
        },
        'aside': {                          # Iklan di Sidebar
            'slot_id': '2394022882',
            'ad_format': 'auto',
            'full_width_responsive': True
        },
        'index_top': {                      # Iklan di atas Artikel, di halaman Awal (Index)
            'slot_id': '1178400983',
            'ad_format': 'fluid',
            'ad_layout_key': '-e8+58+j-dt+vr'
        }
    }
}
