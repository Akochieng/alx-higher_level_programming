#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    res = []
    while i < list_length:
        try:
            val = my_list_1[i] / my_list_2[i]
        except TypeError:
            val = 0
            print("wrongtype")
        except ZeroDivisionError:
            val = 0
            print("division by 0")
        except IndexError:
            val = 0
            print("out of range")
        finally:
            res.append(val)
            i += 1
    return(res)
