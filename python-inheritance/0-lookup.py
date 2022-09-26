#!/usr/bin/python3
"""Finding a list of available attributes and methods of an object."""


def lookup(obj):
    """Returns the list of available attributes and methods of an object
    obj: object to look into
    """

    return dir(obj)