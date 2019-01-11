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

"""
Utilities to make momox usable from both Python 2 and Python 3 code.

This package is not meant to be used externally to momox.
"""

import sys

PY3 = sys.version_info[0] == 3


def with_metaclass(metaclass, *bases):
    """
    Construct a base class with metaclass compatible with python2 and python3.

    Usage:
    ```
    class(with_metaclass(metaclass, base1, base2...)):
        ....
    ```
    """

    class InterposedMetaClass(metaclass):
        def __new__(mcls, name, new_bases, attrs):
            return metaclass(name, bases, attrs)
    return type.__new__(InterposedMetaClass, 'Dummy', (), {})


if PY3:
    string_types = (str,)
    text_type = str
    integer_types = int

    def reraise(exctype, value, trace=None):
        """re-raise an exception with the original traceback."""
        raise exctype(str(value)).with_traceback(trace)


else:
    from .compat_py2 import reraise  # noqa: F401

    string_types = (basestring,)  # noqa: F821
    text_type = unicode  # noqa: F821
    integer_types = (int, long)  # noqa: F821
