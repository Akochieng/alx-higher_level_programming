#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = a_dictionary.keys()
    new_dict = {key: a_dictionary.get(key) for key in sorted_keys}
    for key, value in new_dict.items():
        print(f"{key}: {value}")
