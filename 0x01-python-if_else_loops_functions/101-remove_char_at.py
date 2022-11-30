#!/usr/bin/python3

def remove_char_at(str, n):
    i = 0
    while i < len(str):
        if i == n:
            i = i + 1
            continue
        else:
            print("{}".format(str[i]), end='')
            i = i + 1
    print()
