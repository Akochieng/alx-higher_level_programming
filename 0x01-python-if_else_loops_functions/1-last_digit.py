#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
usednum = abs(number)
str = f"Last digit of {number:d} is {usednum % 10} and is "
if ((usednum % 10) == 0):
    str += f"0"
elif ((usednum % 10) > 5):
    str += f"greater than 5"
else:
    str += f"less than 6 and not 0"
print(str)
