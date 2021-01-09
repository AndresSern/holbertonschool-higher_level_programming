#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_Empty(self):
        x = max_integer()
        self.assertIsNone(x)

    def test_endInteger(self):
        endInteger = max_integer([1, 2, 3, 4])
        self.assertEqual(4, endInteger)

    def test_firstInteger(self):
        firstInteger = max_integer([4, 3, 2, 1])
        self.assertEqual(4, firstInteger)
    def test_only_negative_Number(self):
        my_list = max_integer([1, -4, 20, 10])
        self.assertEqual(20, my_list)

if __name__ == '__main__':
    unittest.main()

