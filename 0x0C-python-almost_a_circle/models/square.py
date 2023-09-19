#!/usr/bin/python3
'''this class is part of the models module'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Class square extends from the Rectangle class.

    Unlike the Rectangle class, the height and width
    are always equal
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''only the parent's init function is called because
        all arguments are similar'''

        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''returns the string representation of the square object'''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        '''ensures that size meets the requirements for length and width
        as defined in the rectangle object

        Args:
            value (int): the length and width of the square
        Returns: the value of the value of self.__width when called without
        args

        Raises:
            TypeError: if value is not of type int
            ValueError: if value is not greater than 0
        '''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''takes in variable arguments to be used as new parameters for the
        square object.

        Args:
            args (tuple): contains the new id, size, x and y values for the
            square object
            kwargs (dict): key word values for id, size, x and y values
        Raises:
            TypeError: as defined in the respective setter functions
            ValueError: as defined in the respective setter functions
        '''
        if args is not None:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        if kwargs is not None:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "size":
                    self.size = kwargs[key]
                elif key == "x":
                    self.x = kwargs[key]
                elif key == "y":
                    self.y = kwargs[key]

    def to_dictionary(self):
        '''returns a dictionary representation of the square. It includes
        all the key arguments that defines a square object.
        '''
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
