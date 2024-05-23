#!/usr/bin/python3
def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings representing the object's attributes and methods.
    """
    # Use the built-in `dir` function to get the list of attributes and methods
    return dir(obj)
