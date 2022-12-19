#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0
    for item in my_list:
        if i < x:
            try:
                i += 1
                print("{}".format(item), end='')
            except:
                print()
                return i
    print()
    return i
