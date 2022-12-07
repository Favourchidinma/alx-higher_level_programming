#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return a_dictionary

    val_list = list(a_dictionary.values())
    val_list.sort(reverse=True)
    max_score = val_list[0]

    for key in a_dictionary:
        if a_dictionary[key] == max_score:
            return key
