# Sorry that this Makefile is a bit of a disaster. Run `make help` to
# see a list of valid targets.


PYTHON ?= $(shell which python3 python 2>/dev/null | head -n1)
PYTHON := $(PYTHON)

TOX ?= $(shell which tox 2>/dev/null | head -n1)
TOX := $(TOX)


PROJECT := $(shell $(PYTHON) ./setup.py --name)
VERSION := $(shell $(PYTHON) ./setup.py --version)

WHEEL := dist/$(subst -,_,$(PROJECT))-$(VERSION)-py3-none-any.whl

DIRS := koji-stubs koji_cli-stubs koji_types
SOURCES := setup.cfg $(foreach d,$(DIRS),$(wildcard $(d)/*.py $(d)/*.pyi))


define checkfor
	@if ! which $(1) >/dev/null 2>&1 ; then \
		echo $(1) "is required, but not available" 1>&2 ; \
		exit 1 ; \
	fi
endef


##@ Basic Targets

default: mypy	## Runs the flake8 and mypy targets


help:  ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m\033[0m\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)


report-python:
	@echo "Using python" $(PYTHON)
	@$(PYTHON) -VV


##@ Local Build and Install

$(WHEEL): $(SOURCES)
	@$(TOX) -qe flake8 && $(TOX) -qe build

build: $(WHEEL)	## Produces a wheel using the default system python


install: $(WHEEL)	## Installs using the default python for the current user
ifeq ($(UID),"0")
	@$(PYTHON) -B -m pip.__main__ \
		install -IU --no-deps \
		$(WHEEL)
else
	$(PYTHON) -B -m pip.__main__ \
		install -IU --no-deps --user \
		$(WHEEL)

endif


uninstall:	## Uninstalls using the default python for the current user
	@$(PYTHON) -B -m pip.__main__ \
		uninstall $(PROJECT)


##@ Cleanup

purge:	clean
	@rm -rf .eggs .tox .mypy_cache


tidy:	## Removes stray eggs and .pyc files
	@rm -rf *.egg-info
	@$(call checkfor,find)
	@find -H . \
		\( -iname '.tox' -o -iname '.eggs' -prune \) -o \
		\( -type d -iname '__pycache__' -exec rm -rf {} + \) -o \
		\( -type f -iname '*.pyc' -exec rm -f {} + \)


clean-built:
	@rm -rf build/* dist/*


clean: clean-built tidy	## Removes built content, test logs, coverage reports
	@rm -rf .coverage* bandit.sarif htmlcov/* logs/*


##@ Testing

flake8:	requires-tox	## Launches flake8 via tox
	@$(TOX) -qe flake8


mypy:	requires-tox flake8	## Launches stubtest via tox
	@$(TOX) -qe mypy


koji-git: requires-tox flake8	## Launches stubtest via tox with koji from git
	@$(TOX) -qe koji-git


twine:	requires-tox build	## Launches twine via tox
	@$(TOX) -qe twine


##@ Documentation

docs: clean-docs requires-tox docs/overview.rst	## Build sphinx docs
	@$(TOX) -qe sphinx


overview: docs/overview.rst  ## rebuilds the overview from README.md


docs/overview.rst: README.md
	@$(call checkfor,pandoc)
	@pandoc --from=markdown --to=rst -o $@ $<


clean-docs:	## Remove built docs
	@rm -rf build/sphinx


preview-docs: docs	## Build and hosts docs locally
	@$(PYTHON) -B -m http.server -d build/sphinx \
	  -b 127.0.0.1 $(PORT)


##@ Workflow Features

project:	## project name
	@echo $(PROJECT)

version:	## project version
	@echo $(VERSION)

python:		## detected python executable
	@echo $(PYTHON)

release-notes:	## markdown variation of current version release notes
	@$(call checkfor,pandoc)
	@pandoc --from=rst --to=markdown -o - \
		docs/release_notes/v$(VERSION).rst


requires-git:
	@$(call checkfor,git)

requires-tox:
	@$(call checkfor,$(TOX))


.PHONY: build clean clean-built clean-docs default deploy-docs docs flake8 help koji-git mypy overview project python quick-test release-notes report-python requires-git requires-tox stage-docs test tidy version


# The end.
