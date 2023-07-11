#!/usr/bin/python3
"""
Write a function that inserts a line of text to a file,
after each line containing a specific string (see example)
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserting a new line of text to a textfile
    """

    line = ""
    with open(filename, 'r', encoding="UTF-8") as f:
        for string in f:
            line += string
            if search_string in string:
                line += new_string
    with open(filename, 'w', encoding="UTF-8") as f:
        f.write(line)
