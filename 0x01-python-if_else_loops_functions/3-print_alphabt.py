#!/usr/bin/python3
for i in range(ord('a'), ord('z')):
	if not (i == ord('q') or i == ord('e')):
		print(chr(i), end='')
