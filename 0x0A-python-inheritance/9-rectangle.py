#!/usr/bin/python3
'''module demonstrates inheritance'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''sub class of the base geometry class'''
    def __init__(self, width, height):
        '''

        Args:
            width: the width of the rectangle
            height: the length of the rectangle
        Raises:
            Exception if either width or height is not an integer
        '''
        try:
            self.integer_validator("width", width)
        except Exception as e:
            raise e
        else:
            self.__width = width

        try:
            self.integer_validator("height", height)
        except Exception as e:
            raise e
        else:
            self.__height = height

    def area(self):
        '''Computes the area of the rectangle

        Returns:
            the area of the rectangle
        '''
        return (self.__width * self.__height)

    def __str__(self):
        '''returns informal str representation of the class'''
        return f"[Rectangle] {self.__width}/{self.__height}"
