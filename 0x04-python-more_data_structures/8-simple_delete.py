#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    search = str(key)
    if search in a_dictionary:
        a_dictionary.pop(search)
    return a_dictionary
