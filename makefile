## makefile automates the build and deployment for python projects
#
## NOTE: this build can not include git.mk as a PROJ_MODULES, and therefore
## python-doc etc; this is because git.mk requires build.json be created and
## the environemnt, for which a propery setup.py is needed but not available
## since this library enables that functionality


## Build system
#
PROJ_TYPE =		python
PROJ_MODULES =		git python-doc python-doc-deploy
# make default python config happy
GIT_BUILD_INFO_BIN =	echo
PY_DOC_SOURCE_DEPS =	cpbuildinfo


## Includes
include ./zenbuild/main.mk


## Targets
#
.PHONY:			cpbuildinfo
cpbuildinfo:		$(GIT_BUILD_INFO)

$(GIT_BUILD_INFO):
			@echo "copying static build info to $(GIT_BUILD_INFO)"
			mkdir -p `dirname $(GIT_BUILD_INFO)`
			cp src/build.json $(GIT_BUILD_INFO)
