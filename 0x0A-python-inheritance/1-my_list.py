#!/usr/bin/python3
'''class that demonstrates public instance methods in class inheritance'''


class MyList(list):
    '''simple class that is a subclass of the list object'''
    def __init__(self):
        '''class has not attributes'''
        super().__init__()

    def print_sorted(self):
        '''prints the sorted version of the list'''
        self.sort()
        print(self)
