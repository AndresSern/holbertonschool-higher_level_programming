#!/usr/bin/python3
"""Write a script that adds all arguments to a Python list, and then save
   them to a file:
        *If the file doesnt exist, it should be created
"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

i = len(argv)
if i == 1:
    save_to_json_file([], "add_item.json")
else:
    list_arguments = load_from_json_file("add_item.json")
    for counter in range(1, i):
        list_arguments.append(argv[counter])
    save_to_json_file(list_arguments, "add_item.json")
