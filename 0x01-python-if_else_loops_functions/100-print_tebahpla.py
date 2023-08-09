#!/usr/bin/python3
for i in range(ord('z'), ord('`'), -1):
    if i % 2 == 0:
        print(chr(i), end="")
    else:
        print(chr((i - ord('a')) + ord('A')), end="")
