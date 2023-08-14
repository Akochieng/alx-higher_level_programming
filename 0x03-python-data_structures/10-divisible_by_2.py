#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bolist = []
    for i in my_list:
        if i % 2 == 0:
            bolist.append(True)
        else:
            bolist.append(False)
    return(bolist)
