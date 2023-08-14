#!/usr/bin/python3
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

my = [0, 1, 2, 3, 4, 5, 6]
res = divisible_by_2(my)

i = 0
while i < len(res):
    print("{:d} {:s} divisible by 2".format(my[i], "is" if res[i] else "is not"))
    i += 1
