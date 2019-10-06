# -*- coding: utf-8 -*-

import os
import shutil
import sys
import datetime

from invoke import task
from invoke.util import cd
from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer
from pelican.settings import DEFAULT_CONFIG, get_settings_from_file

SETTINGS_FILE_BASE = 'pelicanconf.py'
SETTINGS = {
    'OUTPUT_PATH': 'output'
}
SETTINGS.update(DEFAULT_CONFIG)
LOCAL_SETTINGS = get_settings_from_file(SETTINGS_FILE_BASE)
SETTINGS.update(LOCAL_SETTINGS)

CONFIG = {
    'settings_base': SETTINGS_FILE_BASE,
    'settings_publish': 'publishconf.py',
    # Output path. Can be absolute or relative to tasks.py. Default: 'output'
    'deploy_path': SETTINGS['OUTPUT_PATH'],
    'content_path': SETTINGS['PATH'],
    'pelican_opts': '',
    # Github Pages configuration
    'github_pages_branch': 'gh-pages',
    'commit_message': "'Publish site on {}'".format(datetime.date.today().isoformat()),
    # Port for `serve`
    'port': SETTINGS['PORT'],
}

@task
def clean(c):
    """Remove generated files"""
    if os.path.isdir(CONFIG['deploy_path']):
        shutil.rmtree(CONFIG['deploy_path'])
        os.makedirs(CONFIG['deploy_path'])

@task
def build(c):
    """Build local version of site"""
    c.run('pelican {content_path} -s {settings_base} -o {deploy_path} {pelican_opts}'.format(**CONFIG))

@task
def devtheme(c):
    """Build Development Theme for Development Usage"""
    c.run('git clone https://github.com/FarrelF/Modified-Flex.git themes/Flex')
    c.run('pelican-themes -i themes/Flex')

@task
def rebuild(c):
    """`build` with the delete switch"""
    c.run('pelican {content_path} -d -s {settings_base} -o {deploy_path} {pelican_opts}'.format(**CONFIG))

@task
def static(c):
    """`devtheme` then `(re)build` """
    devtheme(c)
    rebuild(c)

@task
def regenerate(c):
    """Automatically regenerate site upon file modification"""
    c.run('pelican {content_path} -r -s {settings_base} -o {deploy_path} {pelican_opts}'.format(**CONFIG))

@task
def serve(c):
    """Serve site at http://localhost:$PORT/ (default port is 9001)"""

    class AddressReuseTCPServer(RootedHTTPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(
        CONFIG['deploy_path'],
        ('', CONFIG['port']),
        ComplexHTTPRequestHandler)

    sys.stderr.write('Serving on port {port} ...\n'.format(**CONFIG))
    server.serve_forever()

@task
def reserve(c):
    """`rebuild`, then `serve`"""
    rebuild(c)
    serve(c)

@task
def devserver(c):
    """`regenerate`, then `serve`"""
    c.run('pelican {content_path} -lr -s {settings_base} -o {deploy_path} {pelican_opts}'.format(**CONFIG))

@task
def preview(c):
    """Build production version of site"""
    c.run('pelican {content_path} -s {settings_publish} -o {deploy_path} {pelican_opts}'.format(**CONFIG))

@task
def livereload(c):
    """Automatically reload browser tab upon file modification."""
    from livereload import Server
    build(c)
    server = Server()
    # Watch the base settings file
    server.watch(CONFIG['settings_base'], lambda: build(c))
    # Watch content source files
    content_file_extensions = ['.md', '.rst']
    for extension in content_file_extensions:
        content_blob = '{0}/**/*{1}'.format(SETTINGS['PATH'], extension)
        server.watch(content_blob, lambda: build(c))
    # Watch the theme's templates and static assets
    theme_path = SETTINGS['THEME']
    server.watch('{}/templates/*.html'.format(theme_path), lambda: build(c))
    static_file_extensions = ['.css', '.js']
    for extension in static_file_extensions:
        static_file = '{0}/static/**/*{1}'.format(theme_path, extension)
        server.watch(static_file, lambda: build(c))
    # Serve output path on configured port
    server.serve(port=CONFIG['port'], root=CONFIG['deploy_path'])


@task
def theme_sync(c):
    """Make a fresh shallow copy of Modified-Flex theme"""
    c.run("rm -rf themes")
    c.run("git clone --jobs 8 --recurse-submodules --depth 1 --shallow-submodules https://github.com/FarrelF/Modified-Flex.git themes/Flex")

@task
def publish(c):
    """Publish to production"""
    theme_sync(c)
    c.run('pelican {content_path} -s {settings_publish} -o {deploy_path} {pelican_opts}'.format(**CONFIG))
    c.run('rm -rf output/drafts')

@task
def gh_pages(c):
    """Publish to GitHub Pages"""
    preview(c)
    c.run('ghp-import -b {github_pages_branch} '
          '-m {commit_message} '
          '{deploy_path} -p'.format(**CONFIG))
