#!/usr/bin/python3
def no_c(my_string):
    templist = list(my_string)
    for i in templist:
        if i in "cC":
            templist.remove(i)
    my_string = "".join(templist)
    return (my_string)
