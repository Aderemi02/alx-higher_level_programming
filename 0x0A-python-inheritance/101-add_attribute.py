#!/usr/bin/python3
"""a function that adds a new attribute
to an object if it’s possible
"""


def add_attribute(obj, attr, value):
    """
    this adds an atribute to an object if possible:
    attr - the attribute name
    value - the attribute value
    raises typeerror if its not possible
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
