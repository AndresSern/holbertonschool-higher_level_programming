#!/usr/bin/python3
class MyInt(int):
    def __ne__(self, other):
        return not self.__eq__(other)
