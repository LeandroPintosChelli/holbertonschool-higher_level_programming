#!/usr/bin/python3
"""Unittest for the max_integer module
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase for the max_integer function."""

    def test_max_end(self):
        self.assertEqual(max_integer([2, 3, 4]), 4)

    def test_max_beg(self):
        self.assertEqual(max_integer([6, 4, 2]), 6)

    def test_max_middle(self):
        self.assertEqual(max_integer([2, 3, 4]), 3)

    def test_one_negative(self):
        self.assertEqual(max_integer([2, -3, 4]), 3)

    def test_all_negative(self):
        self.assertEqual(max_integer([-2, -3, -4]), -2)

    def test_one_element_list(self):
        self.assertEqual(max_integer([2]), 2)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
