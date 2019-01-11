# Copyright 2016 MongoDB, Inc., 2019 Xometry, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys

PY3 = sys.version_info[0] == 3

def with_metaclass(metaclass, *bases):
    """
    This is a python2 and python3 compatible metaclass wrapper. Usage:
    class(with_metaclass(metaclass, base1, base2...)):
    """
    class InterposedMetaClass(metaclass):
        def __new__(mcls, name, new_bases, attrs):
            return metaclass(name, bases, attrs)
    return type.__new__(InterposedMetaClass, 'Dummy', (), {})

if PY3:
    string_types = str,
    text_type = str
    integer_types = int

    def reraise(exctype, value, trace=None):
        raise exctype(str(value)).with_traceback(trace)
else:
    from .compat_py2 import reraise

    string_types = basestring,
    text_type = unicode
    integer_types = (int, long)
