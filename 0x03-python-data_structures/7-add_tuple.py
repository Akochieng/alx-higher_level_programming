#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x = extend_tuple(tuple_a)
    y = extend_tuple(tuple_b)
    return (x[0] + y[0], x[1] + y[1])


def extend_tuple(tuple_c=()):
    if len(tuple_c) == 1:
        d = tuple_c[0], 0
    elif len(tuple_c) == 0:
        d = 0, 0
    else:
        d = tuple_c[:2]
    return (d)
