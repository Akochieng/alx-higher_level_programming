#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    newdict = {i: v for i, a_dictionary.get(i) in [map(sorted(a_dictionary))]}
    print(newdict)
