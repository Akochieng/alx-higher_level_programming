#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = j = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end='')
        except (ValueError, TypeError):
            pass
        else:
            j += 1
        finally:
            i += 1
    print("")
    return j
