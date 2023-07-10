#!/usr/bin/python3
"""
a function that returns:
True if the object is exactly an instance of the specified class;
otherwise False.
"""


def is_same_class(obj, a_class):
    """
    this checks the instance of a class using argument:
    obj object of the instance
    a_class the class to be using to check
    return true if exact, false otherwise
    """
    if type(obj) == a_class:
        return True
    else:
        return False
