#!/usr/bin/python3
for i in range(9):
    for j in range(i, 10):
        if ((i * 10 + j) < 89):
	    print(f"{}{}".format(i, j), end=", ")
	else:
	    print(f"{}{}".format(i, j))
