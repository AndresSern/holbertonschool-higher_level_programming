#!/usr/bin/python3
"""Create A Class Called Base"""


class Base:
    """ This class is called Base, it will be used in the future"""
    __nb_objects = 0
    def __init__(self, id=None):
        """ This function is the initializacion """
        if (id is None):
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id

