#!/usr/bin/python3
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest

class Test_Square(unittest.TestCase):
    '''This module checks the square class'''

    def setUp(self):
        print("Setting up test case")
        s = Square(4)

    def tearDown(self):
        print("Tearing down test case")

    def test_init(self):
        '''check that correct values are assigned
        at init'''
        self.assertEqual(self.s.size, 4)
        self.assertEqual(self.s.x, 0)
        self.assertEqual(self.s.y, 0)
        self.assertEqual(self.s.id, 1)

    def test_size(self):
        with self.assertRaises(TypeError):
            s2 = Square("s")
        with self.assertRaises(TypeError):
            s2 = Square(None)
        with self.assertRaises(ValueError):
            s.size(-3)

if __name__ == '__main__':
    unittest.main()
