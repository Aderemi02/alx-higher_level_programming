#!/usr/bin/python3
"""
a function that creates an Object
from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    a function that writes an object
    to a file using a JSON rep
    """

    with open(filename, 'r', encoding="UTF-8") as f:
        return json.load(f)
