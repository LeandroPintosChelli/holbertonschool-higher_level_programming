#!/usr/bin/python3
"""function that returns True if the object is exactly an instance
of the specified class otherwise False"""


def is_same_class(obj, a_class):
    """Function to determine if obj is an instance of a_class."""
    if type(obj) is a_class:
        return True
    else:
        return False
