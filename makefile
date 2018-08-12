## makefile automates the build and deployment for python projects

PROJ_TYPE=	python
PY_SRC_TEST_PKGS=	tagutil

# make build dependencies
_ :=	$(shell [ ! -d .git ] && git init ; [ ! -d zenbuild ] && \
	  git submodule add https://github.com/plandes/zenbuild && make gitinit )

include ./zenbuild/main.mk

.PHONY:		help
help:
		make PYTHON_BIN_ARGS='--help' run

.PHONY:		last
last:
		make PYTHON_BIN_ARGS='last' run

.PHONY:		repoinfo
repoinfo:
		make PYTHON_BIN_ARGS='info' run

.PHONY:		create
create:
		make PYTHON_BIN_ARGS='create -m some' run

.PHONY:		del
del:
		make PYTHON_BIN_ARGS='del' run

.PHONY:		printsetup
printsetup:
		make PYTHON_BIN_ARGS='prsetup -n zensols.someproj -u plandes -p someproj' run

.PHONY:		tmp
tmp:
		make PYTHON_BIN_ARGS='info -r /Users/landes/view/util/grsync -w 2' run
