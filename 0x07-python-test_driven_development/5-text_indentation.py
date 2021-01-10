#!/usr/bin/python3
"""
This is the function about  5-text_indentation.py
"""

def text_indentation(text):
    """function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    """

    b = 0
    if type(text) != str:
        raise TypeError("text must be a string")

    lenght = len(text)
    while b < lenght:
        print(text[b], end="")
        if text[b] is '.' or text[b] is '?' or text[b] is ':':
            print("\n")
            if (b + 1) < lenght:
                while text[b + 1] is " ":
                    b += 1
        b += 1
