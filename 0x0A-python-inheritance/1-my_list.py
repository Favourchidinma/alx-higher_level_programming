#!/usr/bin/python3
""" 1-my_list.py

A module that contains a class MyList which inherits from list
"""


class MyList(list):
    """A class that inherits from list"""

    def print_sorted(self):
        """A function that prints a list in ascending order"""
        self.sort()
        print(self)
