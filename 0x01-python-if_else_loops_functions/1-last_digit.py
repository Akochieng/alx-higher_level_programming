#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
numdiv = abs(number) % 10
numdiv = numdiv * -1 if number < 0 else numdiv
str = f"Last digit of {number:d} is {numdiv:d} and is "
if (numdiv == 0):
    str += f"0"
elif (numdiv > 5):
    str += f"greater than 5"
else:
    str += f"less than 6 and not 0"
print(str)
