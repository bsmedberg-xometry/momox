"""
Utility functions which are valid syntax in python 2 but not python 3.

This module is only imported when running in python 2.
"""


def reraise(exctype, value, trace=None):
    """re-raise an exception with the original traceback."""
    raise exctype, str(value), trace
