#!/usr/bin/python3

def uppercase(str):
    n = len(str) - 1
    for let in str:
        asc = ord(let)
        if asc >= ord('a') and asc <= ord('z'):
            print("{}{}".format(chr(asc - 32), '' if n > 0 else '\n'), end='')
        else:
            print("{}{}".format(let, '' if n > 0 else '\n'), end='')
        n = n - 1
