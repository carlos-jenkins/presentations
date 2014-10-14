#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 Carlos Jenkins <carlos@jenkins.co.cr>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""
Custom CSS minifier using webassets library.
"""

from os.path import dirname, abspath, join
from jsmin import jsmin

IMPORTS = 'imports.css'

INPUT = [
    's5-core.css',
    'framing.css',
    'pretty.css',
    'docutils.css',
    'hauntr.css',
    'pygments.css',
]

OUTPUT = 'slides.css'


def main():
    """
    Main minifying function.
    """
    path = lambda p: join(abspath(dirname(__file__)), p)
    minified = []

    # Prepend imports
    with open(path(IMPORTS)) as fd:
        minified.append(fd.read())

    # Read inputs
    for css in INPUT:
        with open(path(css)) as fd:
            minified.append(jsmin(fd.read()))

    # Write output
    with open(path(OUTPUT), 'w') as fd:
        fd.write('\n'.join(minified))

    print(path(OUTPUT))


if __name__ == '__main__':
    main()
