#!/usr/bin/python3

def lookup(obj):
    return obj.__dict__


print(lookup(int))
