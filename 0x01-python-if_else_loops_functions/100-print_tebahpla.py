#!/usr/bin/python3
for i in range(ord('z'), ord('`'), -1):
    i = i - ord('a') + ord('A') if i % 2 != 0 else i
    print("{:c}".format(i), end="")
