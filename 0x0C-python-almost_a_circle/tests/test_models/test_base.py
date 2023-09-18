#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle

class Test_base(unittest.TestCase):
    def setup(self):
        self.b1 = base()
        self.b2 = base(76)
        self.r = Rectangle(2, 3)
        self.s = Square(5)
    def test_init_noneid(self):
        '''
        test whether the init function is working as expected
        '''
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(selft.b2.id, 76)
        self.assertEqual(self.r.id, 2)
        self.assertEqual(self.r.id, 5)

def __name__ = "__main__":
    unittest.main()
