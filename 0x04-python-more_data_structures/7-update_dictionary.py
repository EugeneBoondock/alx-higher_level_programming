#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    if isinstance(key, str):
        a_dictionary.update({key: value})
    else:
        raise ValueError("Key must be a string")
