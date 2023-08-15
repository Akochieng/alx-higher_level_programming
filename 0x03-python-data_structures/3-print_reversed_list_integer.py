#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None and len(my_list) > 0:
        temp = my_list[::-1]
        for i in temp:
            print("{:d}".format(i))
