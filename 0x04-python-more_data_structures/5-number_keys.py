#!/usr/bin/python3
def number_keys(a_dictionary):
    newlist = sorted(a_dictionary.keys())
    for i in newlist:
        print("{}: {}".format(i, a_dictionary.get(i)))
