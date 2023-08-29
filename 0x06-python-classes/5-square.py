#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        '''The class square implements a typical square

        The following parameters are initialised when the class
        is first initialised.

        Args:
            size (float): the length or width of the square
            '''
        self.__size = size

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, newsize):
        if not isinstance(newsize, int):
            raise TypeError("size must be an interger")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = newsize

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        times = 0
        if self.__size == 0:
            print("")
        else:
            c = "#" * self.__size
            while times < self.__size:
                print(f"{c}")
                times += 1
