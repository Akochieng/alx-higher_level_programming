#!/usr/bin/python3
def uniq_add(my_list=[]):
    theset = set(my_list)
    aggr = 0
    for i in theset:
        aggr += i
    return aggr
