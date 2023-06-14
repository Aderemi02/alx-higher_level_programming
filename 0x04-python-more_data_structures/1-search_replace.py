#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = my_list.copy()
    newlist = list(map(lambda x: replace if x == search else x, newlist))
    return (newlist)
