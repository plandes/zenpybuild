# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).


## [Unreleased]


## [0.1.1] - 2023-12-02
### Changed
- Replace old [zensols.util] `actioncli` CLI API with `plac`.

### Removed
- Dependency on [zensols.util].


## [0.1.0] - 2023-08-18
### Added
- Sphinx documentation, which includes API docs.

### Changed
- Fixed security vulnerability.
- Fixed setuputils warnings.


## [0.0.7] - 2020-05-23
### Added
- External client use via sourcing (source the `setup.py` with Python's
  `exec`).
- Additional project metadata useful for external clients, such as: short
  description taken from the `README.md`, git remotes, author and other data.
- A better write formatting that now includes a full JSON dump.  Again, this is
  useful to external clients.
- Update `zenbuild`, which heavily uses this project now.


## [0.0.6] - 2020-04-24
### Changed
- Update to [zensols.util] from `zensols.actioncli`.
- Fixed regular expression
- Nascent git repo no tag state bug fix.


## [0.0.5] - 2018-09-14
### Added
- Specify no entry points.


## [0.0.3] - 2018-08-19
### Changed
- Version sorting bug.


## [0.0.3] - 2018-08-19
### Changed
- Version sorting bug.


## [0.0.1] - 2018-08-11
### Added
- Initial version


[Unreleased]: https://github.com/plandes/zenpybuild/compare/v0.1.1...HEAD
[0.1.1]: https://github.com/plandes/zenpybuild/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/plandes/zenpybuild/compare/v0.0.7...v0.1.0
[0.0.7]: https://github.com/plandes/zenpybuild/compare/v0.0.6...v0.0.7
[0.0.6]: https://github.com/plandes/zenpybuild/compare/v0.0.5...v0.0.6
[0.0.5]: https://github.com/plandes/zenpybuild/compare/v0.0.4...v0.0.5
[0.0.4]: https://github.com/plandes/zenpybuild/compare/v0.0.3...v0.0.4
[0.0.3]: https://github.com/plandes/zenpybuild/compare/v0.0.2...v0.0.3
[0.0.2]: https://github.com/plandes/zenpybuild/compare/v0.0.1...v0.0.2


<!-- links -->
[zensols.util]: https://github.com/plandes/util
