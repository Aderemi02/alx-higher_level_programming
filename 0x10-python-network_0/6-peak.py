#!/usr/bin/python3
"""
a function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    finds list of integer in an unsorted list
    """
    if list_of_integers:
        newList = sorted(list_of_integers)
        num = len(newList) - 1
        return newList[num]
