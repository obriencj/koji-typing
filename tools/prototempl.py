#! /usr/bin/env python3

# This library is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This library is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this library; if not, see <http://www.gnu.org/licenses/>.


"""
Protocol Templater

This is a build-time tool which generates `koji_types/protocols.pyi`
based on the type signatures found in `kojihub-stubs/kojihub.pyi`

This script is meant to be invoked by the top-level Makefile, via eg.
`make protocol`

The generated `protocols.pyi` file should be committed in git when it
changes. This script is only a dependency for active development of
this project, not for the build process.

:author: Christopher O'Brien <obriencj@gmail.com>
:license: GPL v3
"""


import sys

from argparse import ArgumentParser
from ast import (
    arg, parse, ClassDef, Constant, Expr, FunctionDef,
    Name, Subscript, _Unparser
)
from copy import copy


TEMPLATE_PATH = "koji_types/protocols.in"
KOJIHUB_PATH = "kojihub-stubs/kojihub.pyi"
OUTPUT_PATH = "koji_types/protocols.pyi"


class UnparseBetter(_Unparser):
    pass


def load_heading(filename):
    found = []
    with open(filename, "rt") as f:
        for line in f:
            if not line.startswith("#"):
                break
            found.append(line)

    found.append("\n\n")
    return "".join(found)


def load_ast(filename):
    with open(filename, "rt") as f:
        return parse(f.read(), filename=filename, type_comments=True)


def dump_ast(filename, tree, heading, footer):
    with open(filename, "wt") as f:
        f.write(heading)
        format_ast(f, tree)
        f.write(footer)


def format_ast(f, tree):
    f.write(UnparseBetter().visit(tree))


def find_classdef(mod, name):
    for node in mod.body:
        if isinstance(node, ClassDef):
            if node.name == name:
                return node
    else:
        raise Exception(f"node {name} not found")


def pop_staticmethod(node):
    for offset, dec in enumerate(node.decorator_list):
        if isinstance(dec, Name) and dec.id == "staticmethod":
            break
    else:
        return False

    node.decorator_list = copy(node.decorator_list)
    node.decorator_list.pop(offset)
    return True


def inject_self(node):
    node.args = copy(node.args)
    node.args.args = copy(node.args.args)

    selfarg = arg('self')
    selfarg.lineno = 0
    selfarg.col_offset = 0

    node.args.args.insert(0, selfarg)


def update_session(node, orig):
    # remove the ellipsis if any
    if node.body:
        last = node.body[-1]
        if isinstance(last, Expr) \
           and isinstance(last.value, Constant) \
           and last.value.value == ...:
            node.body.pop()

    for fn in orig.body:
        if not isinstance(fn, FunctionDef):
            continue

        fn = copy(fn)
        if pop_staticmethod(fn):
            inject_self(fn)

        node.body.append(fn)


def update_multicall(node, orig):
    if node.body:
        last = node.body[-1]
        if isinstance(last, Expr) \
           and isinstance(last.value, Constant) \
           and last.value.value == ...:
            node.body.pop()

    for fn in orig.body:
        if not isinstance(fn, FunctionDef):
            continue

        vc = Name("VirtualCall")
        vc.lineno = 0
        vc.col_offset = 0
        vc.ctx = None

        ss = Subscript(vc, fn.returns)
        ss.lineno = 0
        ss.col_offset = 0
        ss.ctx = None

        fn = copy(fn)
        fn.returns = ss

        node.body.append(fn)


def update_template(tmpl, root):

    session = find_classdef(tmpl, "ClientSession")
    host = find_classdef(tmpl, "Host")

    # generate our session and host from the root exports
    update_session(session, find_classdef(root, "RootExports"))
    update_session(host, find_classdef(root, "HostExports"))

    # then further generate our multicall variations from the session
    # and host we just manifested
    update_multicall(find_classdef(tmpl, "MultiCallSession"),
                     session)
    update_multicall(find_classdef(tmpl, "MultiCallHost"),
                     host)


def cli(options):
    heading = load_heading(TEMPLATE_PATH)
    tmpl = load_ast(TEMPLATE_PATH)
    root = load_ast(KOJIHUB_PATH)

    update_template(tmpl, root)

    dump_ast(OUTPUT_PATH, tmpl,
             heading=heading,
             footer="\n\n\n# The end.\n")


def create_parser(name):
    parser = ArgumentParser(name)
    return parser


def main(argv):

    called_by, *args = argv
    parser = create_parser(called_by)
    options = parser.parse_args(args)

    try:
        cli(options)

    except KeyboardInterrupt:
        return 130

    else:
        return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))


# The end.
