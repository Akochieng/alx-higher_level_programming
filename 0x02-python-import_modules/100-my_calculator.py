#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    lent = len(argv) - 1
    if lent != 3:
        print(f"Usage: {argv[0]} <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    res = 0
    if op == "+":
        res = add(a, b)
    elif op == "-":
        res = sub(a, b)
    elif op == "*":
        res = mul(a, b)
    elif op == "/":
        if b == 0:
            print("Denominator should be a non zero number")
            exit(1)
            res = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and //")
        exit(1)
    print(f"{a:d} {op} {b:d} = {res:d}")
