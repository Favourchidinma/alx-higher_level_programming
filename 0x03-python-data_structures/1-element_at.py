#!/usr/bin/python3

def element_at(my_list, idx):
    if not idx < 0 or not idx >= len(my_list):
        return(my_list[idx])

print(element_at([1,2,3,4,5,6,7,8,9,9,0,4], 4))
