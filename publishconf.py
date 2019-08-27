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
USE_CDN = True
CDN_THEME_REPO_BRANCH = '87c9ad7'
CDN_STATIC_THEME_URL = f'https://cdn.statically.io/gh/FarrelF/Modified-Flex/{CDN_THEME_REPO_BRANCH}/static'
RELATIVE_URLS = False
CC_LICENSE['distribution-type'] = 'cdn'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

# Activating Cache
CACHE_PATH = 'cache'
CHECK_MODIFIED_METHOD = 'mtime'
CACHE_CONTENT = True
GZIP_CACHE = True
LOAD_CONTENT_CACHE = True

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "FarrelF-Blog"
#GOOGLE_ANALYTICS = ""
