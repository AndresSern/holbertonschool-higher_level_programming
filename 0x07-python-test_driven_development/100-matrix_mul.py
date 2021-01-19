#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for index in m_a:
        if type(index) is not list:
            raise ValueError("m_a can't be empty")
    for index in m_b:
        if type(index) is not list:
            raise ValueError("m_b can't be empty")

    for lists in m_a:
        for index in lists:
            if type(index) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")

    for lists in m_b:
        for index in lists:
            if type(index) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
    return m_a
