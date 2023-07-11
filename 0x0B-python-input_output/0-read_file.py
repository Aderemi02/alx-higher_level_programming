#!/usr/bin/python3
"""
a function that reads a text file (UTF8)
and prints it to stdout
"""



def read_file(filename=""):
    """
    a function that reads a textfile
    """

    with open(filename, 'r', encoding="UTF-8") as f:
        f.read()
        print(f.read(), end="")
