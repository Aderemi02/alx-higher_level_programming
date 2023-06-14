#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdic = a_dictionary.copy()
    newlist = list(newdic.keys())
    for i in newlist:
        newdic[i] *= 2
    return (newdic)
