#!/usr/bin/python3
magic_string = __import__('100-magic_string').magic_string

for i in range(10):
    print("--(({})----{})---".format(magic_string(), i))
    print(id(magic_string()))


print(id(magic_string()))
