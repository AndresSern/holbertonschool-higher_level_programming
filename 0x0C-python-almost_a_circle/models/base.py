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

    @staticmethod
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

    @classmethod
    def save_to_file(cls, list_objs):
        list_dicts = []
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            for my_class in list_objs:
                if isinstance(my_class, cls):
                    list_dicts.append(my_class.to_dictionary())
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dicts))
    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)


    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        if cls.__name__ == 'Square':
            dummy = cls(1)
        if cls.__name__ in ['Rectangle', 'Square']:
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        try:
            filename = cls.__name__ + ".json"
            with open(filename, 'r') as f:
                read_data = f.read()
                list_dicti = cls.from_json_string(read_data)
                my_list = []
                for i_dict in list_dicti:
                    my_list.append(cls.create(**i_dict))
                return my_list
        except FileNotFoundError:
            return []
