#!/usr/bin/python3
"""
a function that returns:
True if the object is an instance of, 
or if the object is an instance of a class that inherited from, 
the specified class; 
otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    function that returns true if arguement:
    obj: is the object of an instance
    or 
    a_class: object of an instance of a class
    otherwise false
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
