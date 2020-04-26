## makefile automates the build and deployment for python projects

PROJ_TYPE=		python
PY_SRC_TEST_PKGS=	tagutil

include ./zenbuild/main.mk

.PHONY:			help
help:
			make PYTHON_BIN_ARGS='--help' run

.PHONY:			last
last:
			make PYTHON_BIN_ARGS='last' run

.PHONY:			repoinfo
repoinfo:
			make PYTHON_BIN_ARGS='info' run

.PHONY:			create
create:
			make PYTHON_BIN_ARGS='create -m some' run

.PHONY:			del
del:
			make PYTHON_BIN_ARGS='del' run

.PHONY:			printsetup
printsetup:
			make PYTHON_BIN_ARGS='prsetup -n zensols.someproj -u plandes -p someproj' run
