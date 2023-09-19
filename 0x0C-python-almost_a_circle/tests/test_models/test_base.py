#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class Test_base(unittest.TestCase):
    def setUp(self):
        '''Setting up the test environment for base class'''
        self.b1 = Base()
        self.b2 = Base(76)
        self.r = Rectangle(2, 3)
        self.s = Square(5)
    def test_init_noneid(self):
        '''
        test whether the init function is working as expected
        '''

if __name__ == "__main__":
    unittest.main()
