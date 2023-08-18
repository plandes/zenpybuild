## makefile automates the build and deployment for python projects
#
## NOTE: this build can not include git.mk as a PROJ_MODULES, and therefore
## python-doc etc; this is because git.mk requires build.json be created and
## the environemnt, for which a propery setup.py is needed but not available
## since this library enables that functionality

# type of project
PROJ_TYPE =		python
PROJ_MODULES =		git python-doc python-doc-deploy
# make default python config happy
GIT_BUILD_INFO_BIN =	echo

PY_DOC_SOURCE_DEPS =	cpbuildinfo

include ./zenbuild/main.mk


# targets
.PHONY:			cpbuildinfo
cpbuildinfo:		$(GIT_BUILD_INFO)

$(GIT_BUILD_INFO):
			@echo "copying static build info to $(GIT_BUILD_INFO)"
			mkdir -p `dirname $(GIT_BUILD_INFO)`
			cp src/build.json $(GIT_BUILD_INFO)

.PHONY:			testdeps
testdeps:		deps
			$(PIP_BIN) install $(PIP_ARGS) -r $(PY_SRC)/requirements-test.txt

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
