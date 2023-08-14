#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    temp = my_list.reverse()
    for i in temp:
        print("{:d}".format(i))
