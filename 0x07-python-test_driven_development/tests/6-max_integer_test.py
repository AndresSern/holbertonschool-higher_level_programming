#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_Empty(self):
        x = max_integer()
        self.assertIsNone(x)
    def test_MaxIntenger(self):
        maxIntenger = max_integer([1, 2, 3, 4])
        self.assertEqual(4, maxIntenger)

