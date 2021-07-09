#!/usr/bin/python3
def islower(c):
    codeUnicode = ord(c)
    if (codeUnicode >= 97) and (codeUnicode <= 122):
        return True
    return False
