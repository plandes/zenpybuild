# Inspect and iterate on git tags and invoke setup utils

[![Travis CI Build Status][travis-badge]][travis-link]
[![PyPI][pypi-badge]][pypi-link]
[![Python 3.7][python37-badge]][python37-link]

Inspect and iterate on git tags.  This manages tags in a git repository and
invokes setup utils.  This is used in the [zen build setup] as well.


## Documentation

See the [full documentation](https://plandes.github.io/zenpybuild/).


## Obtaining

The easist way to install the command line program is via the `pip` installer:
```bash
pip install zensols.pybuild
```

Binaries are also available on [pypi].


## Usage

See the [zotsite setup.py] file for an example of how to use it as in setup
tools.


## Changelog

An extensive changelog is available [here](CHANGELOG.md).


## License

[MIT License](LICENSE.md)

Copyright (c) 2018 - 2020 Paul Landes


<!-- links -->
[travis-link]: https://travis-ci.org/plandes/zenpybuild
[travis-badge]: https://travis-ci.org/plandes/zenpybuild.svg?branch=master
[pypi]: https://pypi.org/project/zensols.pybuild/
[pypi-link]: https://pypi.python.org/pypi/zensols.pybuild
[pypi-badge]: https://img.shields.io/pypi/v/zensols.pybuild.svg
[python37-badge]: https://img.shields.io/badge/python-3.7-blue.svg
[python37-link]: https://www.python.org/downloads/release/python-370

[zen build setup]: https://github.com/plandes/zenbuild
[zotsite setup.py]: https://github.com/plandes/zotsite/blob/master/src/python/setup.py
