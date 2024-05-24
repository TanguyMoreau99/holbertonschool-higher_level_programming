#!/usr/bin/python3
"""
Module for checking if an object is an instance of a class
that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Return True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj: object to check
        a_class: class to check against

    Returns:
        True if obj is an instance of a class that inherited from a_class,
        False otherwise
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
