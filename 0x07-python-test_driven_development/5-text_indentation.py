#!/usr/bin/python3
"""
This is the function about  5-text_indentation.py
"""
def text_indentation(text):
    '''Function that a text with 2 new lines
    after each of these characters: .,? and :
    '''

    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0
    len_text = len(text)
    while i < len_text:
        if text[i] in ('.', '?', ':'):
            print("{}\n".format(text[i]))
            while i + 1 < len_text and text[i + 1] == " ":
                i += 1
        else:
            print(text[i], end='')
        i += 1
