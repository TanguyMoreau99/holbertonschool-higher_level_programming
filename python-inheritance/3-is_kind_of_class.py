#!/usr/bin/python3
"""
Check if the object is an instance of, or if the object is an instance
of a class that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class.

    Args:
        obj: object to check
        a_class: class to check against

    Returns:
        True if obj is an instance of a_class or inherited from a_class,
        False otherwise
    """
    return isinstance(obj, a_class)
