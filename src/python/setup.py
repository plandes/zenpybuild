import os
from os import path
from setuptools import setup

# also update in src/python/zensols/pybuild/cli.py
VERSION = '0.0.6'
README_FILE = 'README.md'
REQUIREMENTS_FILE = 'requirements.txt'


def get_packages(dnames):
    dirs = []
    for dname in dnames:
        for root, subdirs, files in os.walk(dname):
            root = path.relpath(root, dname)
            if root != '.':
                dirs.append(path.join(dname, root.replace(os.sep, '.')))
    return dirs


def get_curpath():
    return path.abspath(path.join(path.dirname(__file__)))


def get_root_dir():
    nname, dname = None, get_curpath()
    while nname != dname:
        nname, dname = dname, path.abspath(path.join(dname, path.pardir))
        if path.exists(path.join(dname, README_FILE)):
            break
    return dname


def get_long_description():
    dname = get_root_dir()
    with open(path.join(dname, README_FILE), encoding='utf-8') as f:
        return f.read()


def get_requires():
    req_file = path.join(path.dirname(__file__), REQUIREMENTS_FILE)
    with open(req_file, encoding='utf-8') as f:
        return [x.strip() for x in f.readlines()]


setup(
    name="zensols.pybuild",
    packages=get_packages(['zensols', 'zensols.pybuild']),
    version=VERSION,
    description='Inspect and iterate on git tags.  This manages tags in a git repository.',
    author='Paul Landes',
    author_email='landes@mailc.net',
    url='https://github.com/plandes/zenpybuild',
    download_url='https://github.com/plandes/zenpybuild/releases/download/v{}/zensols.pybuild-{}-py3-none-any.whl'.format(VERSION, VERSION),
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    install_requires=get_requires(),
    keywords=['tooling'],
    classifiers=[],
    entry_points={
        'console_scripts': [
            'zenpybuild=zensols.pybuild.cli:main'
        ]
    }
)
