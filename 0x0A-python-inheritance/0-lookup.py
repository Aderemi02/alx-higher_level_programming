#!/usr/bin/python3
"""
this is a function that returns the list of available attribute
and methods of an object
"""


def lookup(obj):
    """ this returns list of object using the argument:
    obj as the parameter
    returns list of attributes and methods
    """
    return dir(obj)
