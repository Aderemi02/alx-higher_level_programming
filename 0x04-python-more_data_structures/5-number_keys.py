#!/usr/bin/python3
def number_keys(a_dictionary):
    result = 0
    newlist = sorted(a_dictionary.keys())
    for i in newlist:
        result += 1
    return (result)
