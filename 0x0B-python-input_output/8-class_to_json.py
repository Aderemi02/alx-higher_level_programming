#!/usr/bin/python3
"""
Write a function that returns the dictionary description
with simple data structure (list, dictionary, string,
integer and boolean) for JSON serialization of an object
"""


def class_to_json(obj):
    """
    this returns a dict desp of an obj
    """

    new = {}
    if hasattr(obj, "__dict__"):
        new = obj.__dict__.copy()
    return new
