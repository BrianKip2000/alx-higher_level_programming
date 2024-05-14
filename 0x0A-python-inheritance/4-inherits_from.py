#!/usr/bin/python3
"""Module to check instance of a class"""


def inherits_from(obj, a_class):
    """
    Function to check for instance of class
    Args:
    obj: anytype
    a_class: class containing values
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
