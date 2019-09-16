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
CDN_STATIC_THEME_URL = f'https://cdn.statically.io/gh/FarrelF/Modified-Flex/{CDN_THEME_REPO_BRANCH}/static'
CDN_BLOG_BRANCH = '3b27c957'
CDN_STATIC_BLOG_URL = f'https://cdn.statically.io/gh/FarrelF/FarrelF-Blog/{CDN_BLOG_BRANCH}/static'
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

# Agar Berkas 'custom.css' ti buat di dalam folder 'output' saat di terbitkan nanti, jika menggunakan CDN
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
#GOOGLE_ANALYTICS = ""
