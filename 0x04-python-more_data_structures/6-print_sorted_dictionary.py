#!/usr/bin/python3


def print_dict_by_keys(a_dictionary):
    for key, value in sorted(a_dictionary.items(), key=lambda item: item[0]):
        print(key, ":", value)
