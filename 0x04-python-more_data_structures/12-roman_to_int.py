#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    my_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    actual = 0
    anterior = 0
    for i in roman_string:
        if i in my_dict:
            actual += my_dict[i]
            if anterior < my_dict[i]:
                actual -= anterior * 2
            anterior = my_dict[i]
    return actual
