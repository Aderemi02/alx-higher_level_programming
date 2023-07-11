#!/usr/bin/python3
"""
Writing a script that adds all arguments to a
Python list, and then save them to a file
"""
from sys import argv


if __name__ == "__main__":
    save_JSONfile = __import__("5-save_to_json_file").save_to_json_file
    load_JSONfile = __import__("6-load_from_json_file").load_from_json_file

    try:
        new_list = load_JSONfile("add_item.json")
    except FileNotFoundError:
        new_list = []
    for a in argv[1:]:
        new_list.append(a)

    save_JSONfile(new_list, "add_item.json")
