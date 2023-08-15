#!/usr/bin/python3
def no_c(my_string):
    templist = list(my_string)
    tempcopy = templist[:]
    for i in tempcopy:
        if i in "Cc":
            templist.remove(i)
    my_string = "".join(templist)
    return (my_string)
