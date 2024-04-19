# Overview

`preoccupied.koji-typing` is an experimental distribution which
provides typing support for the [koji] package.

[koji]: https://pagure.io/koji

**This project is neither enodorsed, nor supported, by the upstream
[Koji] project**.

This repository exists because I had a number of opinions on how to
produce the typing support. There is an open [issue] in the upstream
to start including typing stubs. However, because koji still supports
Python 2, they are limited to only providing stubs. This means that
their `TypedDict` declarations are also constrained purely to the stub
definitions. The problem with this approach is that one cannot import
typing declarations from a stub for use in a non-stub. While [MyPy]
can infer some of the fields from the usage of the return values this
way, anything more complex than mutating the fields in the same
function they are obtained becomes un-checkable. One could not declare
helper functions and then annotate them to make it clear that they
operate specifically on the `BuildInfo` structure, because `BuildInfo`
could not be imported and used for the annotation during runtime
loading of the hypothetical module.

[issue]: https://pagure.io/koji/issue/3708


## Runtime package `koji_types`

The runtime-available `koji_types` package provides a number of
`TypedDict` definitions which provide structure for the numerous
dictionary result types returned by koji's `ClientSession`
interface. These types can be used to annotate your client code in
order to later perform anaylsis.


## Static analysis package `koji-stubs`

Following [PEP-561] guidelines, `koij-stubs` provides partial stub
annotations for use during static analysis with tools like
[MyPy]. This package relies on the `koji_types` package definitions in
order to supply accurate signatures for many of the dict-based
results.

[PEP-561]: https://peps.python.org/pep-0561/

[MyPy]: https://mypy-lang.org

Due to the dynamic nature of the `MultiCallSession` in koji, these
stubs optionally rely on the [`preoccupied.proxytype`][proxytype]
plugin. This is a purely analysis-time dependency. However in order to
generate accurate analysis of calls made against a `MultiCallSession`
this plugin will need to be enabled.

[proxytype]: https://github.com/obriencj/python-proxytype


## Contact

Author: Christopher O'Brien  <obriencj@preoccupied.net>

Original Git Repository: <https://github.com/obriencj/koji-typing>


## License

This library is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or (at
your option) any later version.

This library is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this library; if not, see <http://www.gnu.org/licenses/>.
