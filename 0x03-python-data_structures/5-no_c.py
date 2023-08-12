#!/usr/bin/python3
def no_c(my_string):
    for i in my_string:
        if i in "cC":
            my_string.remove(i)
