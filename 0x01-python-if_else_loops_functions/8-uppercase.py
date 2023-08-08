#!/usr/bin/python3
def uppercase(str):
	other = ""
	for i in str:
		if (ord(i) >= ord('a') and ord(i) <= ord('z')):
			other += f"{chr(ord('A') + (ord(i) - ord('a')))}"
		else:
			other += f"{i}"
	print("{:s}".format(other))
