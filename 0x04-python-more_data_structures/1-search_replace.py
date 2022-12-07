#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list == None or len(my_list) == 0:
        return
    new = [replace if item == search else item for item in my_list]
    return new
