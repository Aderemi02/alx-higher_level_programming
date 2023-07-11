#!/usr/bin/python3
"""
a function that appends a string at the end of a text file (UTF8)
and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """
    a function that writes to a textfile
    """

    with open(filename, 'a', encoding="UTF-8") as f:
        return f.write(text)
