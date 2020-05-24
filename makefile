## makefile automates the build and deployment for python projects

# type of project
PROJ_TYPE=		python
PROJ_MODULES=		git python-doc

PY_DOC_SOURCE_DEPS =	cpbuildinfo

include ./zenbuild/main.mk


# targets
.PHONY:			cpbuildinfo
cpbuildinfo:		$(GIT_BUILD_INFO)

$(GIT_BUILD_INFO):
			@echo "copying static build info to $(GIT_BUILD_INFO)"
			mkdir -p `dirname $(GIT_BUILD_INFO)`
			cp src/build.json $(GIT_BUILD_INFO)

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

.PHONY:			testsetup
testsetup:
			make PY_SRC_TEST_PAT=test_setuputil.py test
