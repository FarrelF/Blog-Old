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
USE_LESS = False
USE_MINIFIED_SCRIPTS = True
CDN_THEME_REPO_BRANCH = 'a5cf4eb'
CDN_STATIC_THEME_URL = 'https://cdn.statically.io/gh/FarrelF/Modified-Flex/{0}/static'.format(CDN_THEME_REPO_BRANCH)
CDN_BLOG_BRANCH = '8a61b9b'
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

# Nama Berkas-berkas tambahan yang akan di tambahkan
EXTRA_FILES_NAME = [
    '_headers',
    '_redirects',
    'ads.txt',
    'keybase.txt',
    'BingSiteAuth.xml'
]

EXTRA_FILES_DIR = 'extras' # Menentukan Lokasi Berkas Tambahan

# Menambahkan Berkas-berkas Tambahan saat di terbitkan nanti.
if type(EXTRA_FILES_NAME) is str:
    STATIC_PATHS.append('{0}/{1}'.format(EXTRA_FILES_DIR, EXTRA_FILES_NAME))
    EXTRA_PATH_METADATA['{0}/{1}'.format(EXTRA_FILES_DIR, EXTRA_FILES_NAME)] = {'path': '{0}'.format(EXTRA_FILES_NAME)}
elif type(EXTRA_FILES_NAME) is list:
    for values in EXTRA_FILES_NAME:
        STATIC_PATHS.append('{0}/{1}'.format(EXTRA_FILES_DIR, values))
        EXTRA_PATH_METADATA['{0}/{1}'.format(EXTRA_FILES_DIR, values)] = {'path': '{0}'.format(values)}

# Menambah Berkas HTML dari Google untuk Verifikasi saat di terbitkan nanti
GOOGLE_SITE_VERIFICATION_HTML_FILENAME = [
    'google71ef861592f6b855',
    'google0ec7ff3a4f28b0d2'
]

GOOGLE_SITE_VERIFICATION_HTML_DIR = EXTRA_FILES_DIR

if type(GOOGLE_SITE_VERIFICATION_HTML_FILENAME) is str:
    STATIC_PATHS.append('{0}/{1}.html'.format(GOOGLE_SITE_VERIFICATION_HTML_DIR, GOOGLE_SITE_VERIFICATION_HTML_FILENAME))
    EXTRA_PATH_METADATA['{0}/{1}.html'.format(GOOGLE_SITE_VERIFICATION_HTML_DIR, GOOGLE_SITE_VERIFICATION_HTML_FILENAME)] = {'path': '{0}.html'.format(GOOGLE_SITE_VERIFICATION_HTML_FILENAME)}
elif type(GOOGLE_SITE_VERIFICATION_HTML_FILENAME) is list:
    for values in GOOGLE_SITE_VERIFICATION_HTML_FILENAME:
        STATIC_PATHS.append('{0}/{1}.html'.format(GOOGLE_SITE_VERIFICATION_HTML_DIR, values))
        EXTRA_PATH_METADATA['{0}/{1}.html'.format(GOOGLE_SITE_VERIFICATION_HTML_DIR, values)] = {'path': '{0}.html'.format(values)}

# Agar Berkas 'custom.css' tidak di buat di dalam folder 'output' saat di terbitkan nanti, jika menggunakan CDN
if USE_CDN:
    STATIC_PATHS.remove('extras/custom.css')
    del EXTRA_PATH_METADATA['extras/custom.css']
    STATIC_PATHS.remove('extras/custom.js')
    del EXTRA_PATH_METADATA['extras/custom.js']

if USE_CDN:
    SITELOGO = '{0}/content/img/profile_avatar.jpg'.format(CDN_STATIC_BLOG_URL)
else:
    SITELOGO = '{0}/img/profile_avatar.jpg'.format(SITEURL)

SITELOGO_WIDTH = '140'
SITELOGO_HEIGHT = '143'
GOOGLE_SITE_VERIFICATION = [
    'gWpIShFtX8KQbZw1OOHRTXY4QhyanAIVfSfyo6faiw0', 
    'YHoyl7JPwHm7UBWzprZXnX0sQlLla1DjeULMGRqp6yA'
]

BING_SITE_VERIFICATION = '0BD80FDF817E3BE4D9E4C4149FF490BD'

# Pengaturan Tema
if USE_MINIFIED_SCRIPTS == True:
    CUSTOM_JS_NAME = 'custom.min.js'
else:
    CUSTOM_JS_NAME = 'custom.js'

# Mengatur Letak CSS yang di kustom
if USE_CDN:
    CUSTOM_CSS = 'content/extras/custom.min.css'
    CUSTOM_JS = 'content/extras/{0}'.format(CUSTOM_JS_NAME) 
    
else:
    CUSTOM_CSS = 'custom.min.css'
    CUSTOM_JS = CUSTOM_JS_NAME

THEME = 'themes/Flex' # Nama dan lokasi Tema yang di gunakan, ini akan di gunakan untuk penerbitan/produksi
ROBOTS = 'all'

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
DISQUS_LAZYLOAD = True
DISQUS_COMMENT_COUNT = True

# Google
GOOGLE_ANALYTICS = "UA-97506869-1"
GOOGLE_ADSENSE = {
    'ca_id': 'ca-pub-2432124491852819',
    'page_level_ads': True,
    'ads': {
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
