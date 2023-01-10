#!/usr/bin/python3
"""A module that contains a function that trys adds attributes to an object.
"""


def add_attribute(obj, attr, val):
    """A function that trys to add attributes to an object.
    """
    if getattr(obj, attr, "My default") != "My default":
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, val)


#    if not hasattr(an_obj, '__slots__') and not hasattr(an_obj, '__dict__'):
#        raise TypeError("can't add new attribute")
#    if hasattr(an_obj, '__slots__') and not hasattr(an_obj, an_attr):
#        raise TypeError("can't add new attribute")

#    setattr(an_obj, an_attr, a_value)
