#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_Empty(self):
        """ Test if a list is empty"""
        result = max_integer()
        self.assertIsNone(result)

    def test_endInteger(self):
        """ Test for "max at the end" exists"""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(4, result)

    def test_firstInteger(self):
        """ Test for "max at the beggining" exists"""
        result = max_integer([4, 3, 2, 1])
        self.assertEqual(4, result)

    def test_only_negative_Number(self):
        """ Test for "one negative number in the list" exists"""
        result = max_integer([1, -4, 20, 10])
        self.assertEqual(20, result)

    def test_only_negative_numbers(self):
        """ Test for only negative numbers in the list exists"""
        result = max_integer([-2, -1, -4, -8])
        self.assertEqual(-1, result)

    def test_one_element(self):
        """"Test for list of one element exists"""
        result = max_integer([2])
        self.assertEqual(2, result)

    def test_max_in_the_middle(self):
        """Test for max in the middle exists"""
        result = max_integer([1, 2, 8, 5, 3])
        self.assertEqual(8, result)

if __name__ == '__main__':
    unittest.main()

