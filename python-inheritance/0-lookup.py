#!/usr/bin/python3
"""
Defines a 'lookup' function to retrieve attributes and methods of an object using 'dir()'.
"""
def lookup(obj):
    """Returns a list of attributes and methods associated with the given object."""
    return dir(obj)
