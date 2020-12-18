#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_newlist = []
    for array in my_list:
        if array == search:
            my_newlist.append(replace)
        else:
            my_newlist.append(array)
    return my_newlist
