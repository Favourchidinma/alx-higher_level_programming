#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary

    new = {}
    for k, v in a_dictionary.items():
        if v == value:
            continue
        new[k] = v
    a_dictionary = new
    return a_dictionary
