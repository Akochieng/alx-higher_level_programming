#!/usr/bin/python3
import unittest
'''This module is a sample test case'''


class TestMaxInteger(unittest.TestCase):
    '''simple test case for max_integer function'''
    def test_max(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_none(self):
        self.assertEqual(max_integer([], None))
