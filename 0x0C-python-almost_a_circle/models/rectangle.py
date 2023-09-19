#!/usr/bin/python3
'''Defines the rectangle class'''
from models.base import Base


class Rectangle(Base):
    '''A simple representation of the geometric rectangle shape'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        initialises an instance of Rectangle

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
            x (int): displacement along the x axis
            y (int): displacement along the y axis
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''
        sets and receives the __width attribute

        Args:
            value (int): the new value of width to be set
        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is not greater than 0
        Returns:
            The value of self.__width if the getter is called
        '''
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, float):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''
        sets and receives the __height attribute

        Args:
            value (int): the new value of height to be set
        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is not greater than 0
        Returns:
            The value of self.__height if the getter is called
        '''
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, float):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''
        sets and receives the __x attribute

        Args:
            value (int): the new value of x to be set
        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less than 0
        Returns:
            The value of self.__x if the getter is called
        '''
        return self.__x

    @x.setter
    def x(self, value):
        if isinstance(value, float):
            if not isinstance(value, int):
                raise TypeError("x must be an integer")
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''
        sets and receives the __y attribute

        Args:
            value (int): the new value of y to be set
        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less than 0
        Returns:
            The value of self.__y if the getter is called
        '''
        return self.__y

    @y.setter
    def y(self, value):
        if isinstance(value, float):
            if not isinstance(value, int):
                raise TypeError("y must be an integer")
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''computes the area of the rectangle object

        Returns:
            the area of the rectangle object
        '''
        return self.__width * self.__height

    def display(self):
        '''displays a representation of the instance using
        the character #. Nothing should be displayed if
        either the width or the height is 0

        Returns: None
        '''
        char = "#"
        res = ""
        if self.__height == 0 or self.__width == 0:
            print(res)
            return
        res += (self.__y * "\n")
        for count in range(self.__height):
            res += (self.__x * " ")
            res += (char * self.__width)
            if count < self.__height - 1:
                res += "\n"
        print(res)

    def __str__(self):
        '''overloads the inbuild __str__ method

        Returns: a customised string representation of the
        rectangle object
        '''
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} \
- {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        '''updates an object's attributes

        Args:
            args (tuple): new values of the object attributes
            kwargs (dict): key word values of the object attributes

        Returns: None
        '''
        if args is not None:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.width = args[1]
                elif i == 2:
                    self.height = args[2]
                elif i == 3:
                    self.x = args[3]
                elif i == 4:
                    self.y = args[4]
        if kwargs is not None:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "width":
                    self.width = kwargs[key]
                elif key == "height":
                    self.height = kwargs[key]
                elif key == "x":
                    self.x = kwargs[key]
                elif key == "y":
                    self.y = kwargs[key]

    def to_dictionary(self):
        '''returns a dictionary representation of the object'''
        return {'id': self.id, 'width': self.width, 'height':
                self.height, 'x': self.x, 'y': self.y}
