#!/usr/bin/python3
"""A module that contains just one function that returns True if the object
is exactly an instance of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """a function that returns True if the object is exactly an instance
    of the specified class; otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    return False
