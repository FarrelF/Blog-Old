#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pymdownx import emoji, twemoji_db, highlight, inlinehilite, superfences, extra, magiclink, escapeall, details
from datetime import datetime, timezone, timedelta
from babel.dates import format_date, format_datetime, format_time
from dateutil import parser
import git

AUTHOR = 'Farrel Franqois'

# Mengenai Blog
PORT = 9001
SITENAME = 'Farrel Franqois Blog'
SITETITLE = 'Farrel Franqois Blog'
SITESUBTITLE = '(Bukan) Sekedar blog pribadi saya'
SITEDESCRIPTION = 'Ini adalah Blog saya, walaupun begitu, ini bukan berarti sekedar Blog Pribadi saja!'
SITEURL = 'http://localhost:{0}'.format(PORT)  # Saya isikan dengan 'localhost' agar blog bisa di akses secara Offline
FB_APP_ID = '1696840170451603'

IGNORE_FILES = ['.#*']  # Mengabaikan Berkas

DEFAULT_METADATA = {
    'status': 'draft',
    'author': AUTHOR
}

# Pengaturan Bahasa, Waktu dan Lokalisasi
TIMEZONE = 'Asia/Jakarta'  # Zona Waktu yang di gunakan
DEFAULT_DATE = 'fs'
DEFAULT_LANG = 'id'
OG_LOCALE = 'id_ID'
LOCALE = ('id_ID', 'id_ID.utf8', 'id_ID.UTF-8')
DATE_FORMATS = {
    'id': ('%A, %d %B %Y'),
}


def locale_date(d, locale_language=LOCALE[0]):
    date_time = parser.parse(str(d))
    date_format = str(
        format_date(
            date_time, format='full', locale=locale_language
        )
    )
    return date_format


def locale_datetime(d, locale_language=LOCALE[0]):
    date_time = parser.parse(str(d))
    time_zone = str(datetime.now(timezone(timedelta(0))).astimezone().tzinfo)
    date_format = str(
        format_datetime(
            date_time, "EEEE, dd LLLL yyyy, 'pukul' HH:mm:ss '{0}'".format(time_zone), locale=locale_language
        )
    )
    return date_format


JINJA_FILTERS = {'locale_date': locale_date}

# Pengaturan Font
USE_GOOGLE_CDN_FOR_FONTS = False
USE_MINIFIED_FONT_CSS = False
USE_MINIFIED_SCRIPTS = False
LINKS_IN_NEW_TAB = False

if USE_MINIFIED_SCRIPTS == True:
    CUSTOM_JS_NAME = 'custom.min.js'
else:
    CUSTOM_JS_NAME = 'custom.js'

DARK_MODE = True
USE_BOOTSTRAP = False

PATH = 'content'

ROBOTS = 'noindex, nofollow, noarchive'

# Artikel
ARTICLE_PATHS = ['articles']
ARTICLE_SAVE_AS = '{slug}/index.html'
ARTICLE_LANG_SAVE_AS = '{slug}/{lang}/index.html'
ARTICLE_URL = '{slug}'
ARTICLE_LANG_URL = '{slug}/{lang}'

# Penulis
AUTHOR_SAVE_AS = 'penulis/{slug}/index.html'
AUTHOR_URL = 'penulis/{slug}'

# Kategori
CATEGORY_URL = 'kategori/{slug}'
CATEGORY_SAVE_AS = 'kategori/{slug}/index.html'

# Tag
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAG_URL = 'tag/{slug}'

# Halaman
PAGE_PATHS = ['pages']
PAGE_SAVE_AS = '{slug}/index.html'
PAGE_LANG_SAVE_AS = '{slug}/{lang}/index.html'
PAGE_URL = '{slug}'
PAGE_LANG_URL = '{slug}/{lang}'

# Lokasi Berkas Statis
STATIC_PATHS = [
    'img',
    'extras/CNAME',
    'extras/favicon.ico',
    'extras/robots.txt',
    'extras/custom.css',
    'extras/custom.js'
]

EXTRA_PATH_METADATA = {
    'extras/CNAME': {'path': 'CNAME'},
    'extras/favicon.ico': {'path': 'favicon.ico'},
    'extras/robots.txt': {'path': 'robots.txt'},
    'extras/custom.css': {'path': 'custom.css'},
    'extras/custom.js': {'path': 'custom.js'}
}

# Pengaturan Tampilan
CUSTOM_CSS = 'custom.css'  # Menentukan lokasi Berkas CSS yang di buat sendiri
CUSTOM_JS = CUSTOM_JS_NAME  # Menentukan lokasi Berkas JS yang di buat sendiri
USE_CDN = False
LESS = {
    'use_less': True,
    'version': 'v3.11.1',
    'integrity_hash': 'sha256-KCxucWs2gUeLEgTy4loHeYPssoGZkc8XQo7KQGG16h8= sha384-TdzAi2gOpsVeVksJYStNkCNf8IoHUV8UxcIbT1psLelW9c13NSNTQf26SuL/+aNQ sha512-h7WSomHPKAh1xrFenQWhrjfYs1aBxFPEU80lPzLQ3dmC10Wn3UjuoslY+BrOpcMu0W9uiu8xgG3/SpGgqMxztQ=='
}

THEME = 'Flex'  # Menentukan Nama tema yang terinstall melalui pelican-themes, untuk keperluan pengembangan/Development
MAIN_MENU = True

# Menonaktifkan Tanda Pagar pada Link URL setiap ke artikel/halaman
DISABLE_URL_HASH = True
CHECK_MODIFIED_METHOD = 'sha256'

# Plugin dan Konfigurasi nya
PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'extended_sitemap', 
    'filetime_from_git',
    'more_categories', 
    'summary', 
    'pelican_htmlmin', 
    'interlinks'
]

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

HTMLMIN_OPTIONS = {
    'remove_comments': True,
    'remove_empty_space': True,
    'remove_optional_attribute_quotes': True,
    'keep_pre': True,
    'reduce_boolean_attributes': True
}

INTERLINKS = {
    'wikipedia_en': 'https://en.wikipedia.org/wiki/',
    'wikipedia_id': 'https://id.wikipedia.org/wiki/',
    'ddg': 'https://duckduckgo.com/search?q=',
    'google': 'https://www.google.com/search?q=',
    'google_images': 'https://www.google.com/search?tbm=isch&q=',
    'google_id': 'https://www.google.co.id/search?q=',
    'google_images_id': 'https://www.google.co.id/search?tbm=isch&q=',
    'stackoverflow_answer': 'https://stackoverflow.com/a/',
    'stackoverflow_question': 'https://stackoverflow.com/questions/',
    'askubuntu_answer': 'https://askubuntu.com/a/',
    'askubuntu_question': 'https://askubuntu.com/questions/'
}

# Pengaturan Google CSE (Custom Search Engine)
GOOGLE_SEARCH = {
    'activate': True,
    'partner_id': 'partner-pub-2432124491852819:4493745682',
    'options': {
        'using_google_searchbox': False,
        'search_style': ''  # Nilai ini akan berubah jika Opsi 'using_google_searchbox' berubah, jadi sebaiknya opsi ini tidak usah di isi
    }
}
SEARCHBOX_ON_SIDEBAR = True

if GOOGLE_SEARCH['options']['using_google_searchbox'] == True:
    GOOGLE_SEARCH['options']['search_style'] = 'gcse-searchresults-only'
else:
    GOOGLE_SEARCH['options']['search_style'] = 'gcse-search'

# Pengaturan Markdown
PYGMENTS_STYLE = 'monokai'  # Tampilan Pygments yang merupakan Syntax Highlighter
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.toc': {},
        'markdown.extensions.meta': {},
        'pymdownx.highlight': {
            'css_class': 'highlight',
            'pygments_style': PYGMENTS_STYLE,
            'guess_lang': False,
        },
        'pymdownx.extra': {},
        'pymdownx.escapeall': {},
        'pymdownx.emoji': {
            'emoji_index': emoji.twemoji,
            'emoji_generator': emoji.to_svg,
            'alt': 'short',
            'options': {
                'attributes': {
                    'height': '16px',
                    'width': '16px'
                },
                'classes': 'twemoji_emojis',
                'image_path': 'https://cdn.statically.io/gh/twitter/twemoji/v12.1.5/assets/svg/',
            },
        },
        'pymdownx.superfences': {},
        'pymdownx.inlinehilite': {},
        'pymdownx.magiclink': {},
        'pymdownx.details': {},
    },
    'output_format': 'html5',
}

# Hak Cipta

# Implementasi Lisensi dari Creative Commons
COPYRIGHT_YEAR = datetime.now().year
COPYRIGHT_NAME = AUTHOR
CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike (CC BY-SA)',
    'version': '4.0',
    'slug': 'by-sa',
    'distribution-type': 'local'
}

# Pengaturan Penampilan Commit Git di Akhir Blog
SHOW_LAST_COMMIT = True
COMMIT = str(git.Repo().head.commit)
SHORT_COMMIT = COMMIT[0:7]
COMMIT_DATETIME = locale_datetime(git.Repo().head.commit.authored_datetime)
REPO_SHORT = "FarrelF/Blog"
REPO_URL = "https://github.com/{0}".format(REPO_SHORT)

LAZYLOAD_IMAGES = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

GOOGLE_RECAPTCHA = {
    'activate': True,
    'site_key': '6Ldh-TAUAAAAAE468ek0vOM2Mc-BSsKFbA-XkErJ',
    'forms_id': {
        'hubungi-saya': 'contact-form'
    }
}

SITELOGO = '{0}/img/profile_avatar.jpg'.format(SITEURL)

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
    ('facebook', 'https://www.facebook.com/FarrelFranqois'),
    ('twitter', 'https://twitter.com/FarrelFranqois'),
    ('github', 'https://github.com/FarrelF'),
    ('gitlab', 'https://gitlab.com/FarrelF'),
    ('telegram', 'https://t.me/FarrelF'),
    ('keybase', 'https://keybase.io/farrelf'),
    ('paypal', 'https://paypal.me/FarrelF')
)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Using Imgix Luminous and Drift
LUMINOUS = {
    'activate': True,
    'version': 'v2.3.2',
    'script': {
        'integrity_hash': 'sha256-JtowJgZIxtr4WObMQMDqCojFv0TMRb438K2bLmjYS8Q= sha384-fycZFb7rivGKtu0pBXNMrvngmHPp+HqL5Sq+f7MzM0FfF9+Y2CD0o5tEksQlKVco sha512-m4kT2yNAKoSDZ6+orVQhqgrIMwAng5X/wBEiNeegedjIRhZRnlgyGzYqkzJ1HR1wn0aidznu8O4Yzz7bKTSrFQ=='
    },
    'style': {
        'integrity_hash': 'sha256-tPW9wLkspLEhKo1rCAUlqiMvw30PPoyOatV5gL8a+/M= sha384-3OHcGxAb4Xo6Ww7Dkrx9HUXO+FsWOI3pjdto83LFYUSpkwLlNeYZHSknlQHvpver sha512-qvPeSLkXsYxwQBnNswZ6Fri9TbDR2wOKSXzBFnuSFlOGbWob7KY8qrHU6F4YukwN6FmcdDWR1jYCbgWjf3nVkQ=='
    }
}

DRIFT = {
    'activate': False,
    'version': 'v1.4.0',
    'script': {
        'integrity_hash': 'sha256-aFEn7VlBa8PmHn8vQoltD9oX8Tkv124tmWKPvAuiHJo= sha384-5egwFCf6lmPdG3pnKadFiJi2Zt+bHNb2eC0jwPXTtWLyCNZXA8MezB5IxHeDv4a5 sha512-I3Ntq1EyOaSknyeFTaiXsNMIqDBLTIlCPWXyKMA+XdXvs0MAk3WlONybS7Iyn8TYn3jTGMhCikUdWT5ktEO3dw=='
    },
    'style': {
        'integrity_hash': 'sha256-0eMzyq5C4rYJJNmSv07Lvef7ceiOzf9MNVUrA9hiq+M= sha384-hT7xn1tOkpXuQj5+3w61i8ChdD1BhRxUf9Z3RZKDdggYEj/STnZ8ch8otrAp4TUg sha512-vtTM05wauWgmgm7bPHD1J1yJC9RLSn45zRazmqO4iAeoKe3GeSWCIVr8M+jqbRhtvBnhHJEJSYuSN05dB4xK8Q=='
    }
}
