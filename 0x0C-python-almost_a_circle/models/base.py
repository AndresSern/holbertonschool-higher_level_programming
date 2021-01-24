#!/usr/bin/python3
"""Create A Class Called Base"""
import json

class Base:
    """ This class is called Base, it will be used in the future """
    __nb_objects = 0
    def __init__(self, id=None):
        """ This function is the initializacion """
        if (id is None):
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id

    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        if type(list_dictionaries) is list:
            for dictionaries in list_dictionaries:
                if type(dictionaries) is not dict:
                    return "[]"
            return json.dumps(list_dictionaries)
        else:
            return "[]"


