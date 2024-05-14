#!/usr/bin/pyhton3


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
    obj: Any Python object.

    Returns:
    A list of strings containing the names of attributes and methods of the object.
    """
    return dir(obj)
