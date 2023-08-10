#!/usr/bin/python3
from sys import argv
num = len(argv) - 1
if num == 0:
    print(f"{num:d} arguments.")
elif num == 1:
    print(f"{num:d} argument:")
else:
    print(f"{num:d} arguments:")
for i in range(1, num + 1):
    print(f"{i:d}: {argv[i]}")
