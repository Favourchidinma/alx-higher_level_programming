#!/usr/bin/python3

def uppercase(str):
    for letter in str:
        if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
            print("{}".format(chr(ord(letter) - 32)), end='')
        else:
            print("{}".format(letter), end='')
