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
	@rm -rf .eggs .tox .mypy_cache tools/koji/


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


mypy:	requires-tox flake8 protocols	## Launches stubtest via tox
	@$(TOX) -qe mypy


koji-git: requires-tox flake8 protocols tools/koji	## Launches stubtest via tox with koji from git
	@$(TOX) -qe koji-git


twine:	requires-tox build	## Launches twine via tox
	@$(TOX) -qe twine


tools/koji:	requires-git
	@if [ ! -d tools/koji ] ; then \
		git clone https://pagure.io/koji.git tools/koji ; \
	elif [ "$(SKIP_PULL)" != "1" ] ; then \
		git -C tools/koji pull ; \
	fi


kojihub: requires-tox protocols tools/koji
	@$(TOX) -qe kojihub


##@ Development Workflow

koji_types/protocols.pyi:	kojihub-stubs/kojihub.pyi koji_types/protocols.in
	@$(PYTHON) tools/prototempl.py


protocols:	koji_types/protocols.pyi	## regenerates protocols stub if needed


build:	clean-built protocols
	@$(TOX) -qe build


##@ Workflow Features

project:	## project name
	@echo $(PROJECT)

version:	## project version
	@echo $(VERSION)

python:		## detected python executable
	@echo $(PYTHON)

requires-tox:
	@$(call checkfor,$(TOX))


.PHONY: build clean clean-built default flake8 help koji-git kojihub mypy project purge python report-python requires-git requires-tox tidy twine version


# The end.
