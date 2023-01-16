#!/usr/bin/python3


def print_dict_by_keys(a_dictionary):
    for key in sorted(a_dictionary.keys()):
        print(key, ":", a_dictionary[key])
