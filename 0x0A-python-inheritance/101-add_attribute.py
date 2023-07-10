#!/usr/bin/python3
"""a function that adds a new attribute
to an object if it’s possible
"""


def add_attribute(obj, name_attr, value):
    """
    this adds an atribute to an object if possible:
    name_attr - the attribute name
    value - the attribute value
    raises typeerror if its not possible
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("Can't add new attribute")
    setattr(obj, name_attr, value)
