PY?=python3
PELICAN?=pelican
PELICANTHEMES?=$(PELICAN)-themes
PELICANOPTS=
THEME?=Flex
THEMEREPO?=https://github.com/FarrelF/Modified-Flex.git

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
THEMEPATH=$(BASEDIR)/themes/$(THEME)
PUBLISHCONF=$(BASEDIR)/publishconf.py
DEVPUBLISHCONF=$(BASEDIR)/dev_publishconf.py

GITHUB_PAGES_BRANCH=gh-pages

INSTALLER ?= poetry
INSTALLOPT=
WITH_YARN ?= 0
YARN_FLAGS=
PRODUCTION ?= 0

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

ifeq ($(PRODUCTION), 1)
	YARN_FLAGS += --production
	INSTALLOPT += --no-dev
endif

REBUILD ?= 0
ifeq ($(REBUILD), 1)
	PELICANOPTS += --delete-output-directory
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

ifeq ($(origin PORT),undefined)
	PORT := 9001
endif

ifeq ($(origin SERVER),undefined)
	SERVER := 0.0.0.0
endif

help:
	@echo 'Makefile for a pelican Web site                                                                                '
	@echo '                                                                                                               '
	@echo 'Usage:                                                                                                         '
	@echo '   make install [PRODUCTION=0]                   Install the packages and all of its dependencies (with Pipenv)'
	@echo '   make html [REBUILD=0]                         (re)generate the web site                                     '
	@echo '   make clean                                    remove the generated files                                    '
	@echo '   make regenerate [REBUILD=0]                   regenerate files upon modification                            '
	@echo '   make publish [REBUILD=0]                      generate using production settings                            '
	@echo '   make preview [REBUILD=0]                      Make/Generate a Preview Website/Blog before you can Publish it'
	@echo '   make serve [PORT=$(PORT)]                        serve site at http://localhost:$(PORT)                     '
	@echo '   make serve-global [SERVER=$(SERVER)]            serve (as root) to $(SERVER):80                             '
	@echo '   make devserver [REBUILD=0] [PORT=$(PORT)]        serve and regenerate together                              '
	@echo '   make devtheme                                 Build the Theme for Development                               '
	@echo '   make static-files [REBUILD=0]                 make devtheme + make html                                     '
	@echo '   make github                                   upload the web site via gh-pages                              '
	@echo '                                                                                                               '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html                                        '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                                                         '
	@echo 'Set the REBUILD variable to 1 to Delete Output first before building                                           '
	@echo 'Set the PRODUCTION variable to 1 if you want using a command for production purpose                            '

install:
	@echo 'Installing the Website/Blog packages and its dependencies, please wait....'
ifeq ($(WITH_YARN), 1)
	$(INSTALLER) install $(INSTALLOPT) && $(INSTALLER) shell
	yarn install $(YARN_FLAGS)
else
	$(INSTALLER) install $(INSTALLOPT) && $(INSTALLER) shell
endif


html:
	@echo 'Making HTML Files to Output Directory....'
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	@echo 'Cleaning Output Directory....'
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

regenerate:
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
ifdef PORT
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT)
else
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)
endif

serve-global:
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT) -b $(SERVER)

devserver:
ifdef PORT
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT)
else
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)
endif

devtheme:
	@echo 'Building and Installing the Theme, please wait....'
	git clone --depth 1 $(THEMEREPO) $(THEMEPATH)
	$(PELICANTHEMES) -i $(THEMEPATH)

static-files: devtheme html

publish:
	@echo 'Publishing your Website/Blog, please wait....'
	rm -rf themes
	git clone --jobs 8 --recurse-submodules --depth 1 --shallow-submodules $(THEMEREPO) $(THEMEPATH)
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

preview:
	@echo 'Making a Preview Website/Blog, please wait....'
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(DEVPUBLISHCONF) $(PELICANOPTS)

github: publish
	@echo ''
	@echo 'Importing Output to GitHub Pages....'
	ghp-import -m "Generate Pelican site" -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)
	git push origin $(GITHUB_PAGES_BRANCH)


.PHONY: install html help clean regenerate serve serve-global devserver devtheme static-files publish preview github
