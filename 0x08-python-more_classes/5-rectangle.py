#!/usr/bin/python3
'''module contains a simple class'''


class Rectangle:
    '''This class is an empty definition of a Rectangle object'''
    def __init__(self, width=0, height=0):
        '''Initialises an instance of class rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Setter and getter functions  for the __width attribute

        Args:
            value (int): the width as received
        Returns: width
        Raises:
            TypeError: if the width is not an integer
            ValueError: if the value is less than 0
        '''
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Setter and getter functions for the __height attribute

        Args:
            value (int): the height as received
        Returns: height
        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        '''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        '''computes the area of the rectangle instance

        Returns (int): the area of the rectangle
        '''
        return self.__width * self.__height

    def perimeter(self):
        '''computes the perimeter of the rectangle instance

        Returns (int): the perimeter of the rectangle
        '''
        return (self.__width + self.__height) * 2

    def __str__(self):
        '''returns an unofficial string representation of an instance

        Returns: the string representation of the instance
        '''
        temp = ""
        num = 0
        while num < self.__height:
            temp + ("#" * self.__width)
            if num < (self.__height - 1):
                temp + "\n"
            num += 1
        return temp

    def __repr__(self):
        '''the representaion of the class that can be used to create
        an instance of the class using eval
        '''
        return f"Rectangle({width}, {height})"

    def __del__(self):
        '''action to be performed when an instance is deleted'''
        print("Bye rectangle...")
