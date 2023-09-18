#!/usr/bin/python3
from models.base import Base
from models.rectangle import Rectangle
import unittest

class Test_Rectangle(unittest.TestCase):
    def setup(self):
        '''Set up a sample Rectangle object for the
        test cases
        '''
        self.r = Rectangle(2, 3)

    def test_init(self):
        '''Test the accuracy of the attributes assigned
        by init function of the Rectangle class
        '''
        self.assert(self.r.width, 2)
        self.assert(self.r.height, 3)
        self.assert(self.r.id, 1)
        self.assert(self.r.x, 0)
        self.assert(self.r.y, 0)

    def test_width(self):
        '''Test the width getter and setter methods
        to ensure that only integer values greater
        than 0 can be assigned
        '''
        with self.assertRaises(TypeError):
            self.r.width('r')
        with self.assertRaises(TypeError):
            r1 = Rectangle(None, 5)
        with self.assertRaises(ValueError):
            self.r.width(0)
        with self.assertRaises(ValueError):
            self.r.width(-4)
        with self.assertRaises(ValueError):
            r1 = Rectangle(-2, 5)

    def test_height(self):
        '''Test the getter and setter methods to ensure
        only integer values greater than 0 can be
        assigned.
        '''
        with self.assertRaises(TypeError):
            self.r.height('h')
        with self.assertRaises(TypeError):
            r1 = Rectangle(5, None)
        with self.assertRaises(ValueError):
            self.r.height(0)
        with self.assertRaises(ValueError):
            self.r.height(-4)
        with self.assertRaises(ValueError):
            r1 = Rectangle(2, -5)

    def test_x(self):
        '''Test the x setter and getter methods to
        ensure only integer values >= 0 are accepted
        '''
        with self.assertRaises(TypeError):
            self.r.x('x')
        with self.assertRaises(TypeError):
            r1 = Rectangle(5, 3, None, 2)
        with self.assertRaises(ValueError):
            self.r.x(-4)
        with self.assertRaises(ValueError):
            r1 = Rectangle(5, 3, -1, 2)

    def test_y(self):
        '''Test the y setter and getter methods to
        ensure only integer values >= 0 are accepted
        '''
        with self.assertRaises(TypeError):
            self.r.y('h')
        with self.assertRaises(TypeError):
            r1 = Rectangle(5, 3, 2, None)
        with self.assertRaises(ValueError):
            self.r.y(-4)
        with self.assertRaises(ValueError):
            r1 = Rectangle(5, 3, 1, -2)

    def test_area(self):
        '''Test the area method for accuracy'''
        self.assert(self.r.area(), 5)


if __name__ = "__main__":
    unittest.main()
