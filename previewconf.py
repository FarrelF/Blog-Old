#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from publishconf import *

THEME = "Flex"  # Menentukan Nama tema yang terinstall melalui pelican-themes, untuk keperluan pengembangan
ROBOTS = 'noindex, nofollow, noarchive'

# Meng-hapus berkas yang tidak terpakai
STATIC_PATHS.remove('extras/robots.txt')
del EXTRA_PATH_METADATA['extras/robots.txt']
STATIC_PATHS.remove('extras/ads.txt')
del EXTRA_PATH_METADATA['extras/ads.txt']

# Google
GOOGLE_ANALYTICS = ""
GOOGLE_ADSENSE = ''
