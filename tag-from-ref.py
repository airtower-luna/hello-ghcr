#!/usr/bin/python3

# MIT License
#
# Copyright (c) 2020 Fiona Klute
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import re
import sys

# The keys in tag_patterns are matched against the first command line
# parameter, which should be a git ref. If there is a match, the
# matching value and all non-empty capturing groups (if any) are used
# as tags. If multiple patterns match all resulting tags are used. If
# no pattern matches the output will be empty.

tag_patterns = {
    re.compile(r'^refs/heads/main$'): 'beta',
    re.compile(r'^refs/tags/((\d+)(?:\.\d+)+)'): 'latest',
}

ref = sys.argv[1]

tags = set()
for p in tag_patterns:
    m = p.match(ref)
    if m is not None:
        tags.add(tag_patterns[p])
        tags.update(t for t in m.groups() if t)

print(' '.join(tags))
