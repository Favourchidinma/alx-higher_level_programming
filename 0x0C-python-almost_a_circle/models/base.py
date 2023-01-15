#!/usr/bin/python3
""" A module `base` that contains a class `Base` to be used as the base class
for future implementation of other classes.
"""


class Base:
    """A class that is used as a base class for yet implemented classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Imitializes the class `Base` with `id`.

        Args:
            id(int): the id.
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
