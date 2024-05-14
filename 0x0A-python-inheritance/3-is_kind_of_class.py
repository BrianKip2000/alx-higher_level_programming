#!/usr/bin/python3
"""Module to check instance of a class"""


def is_kind_of_class(obj, a_class):
    """
    Function to check for instance of class
    Args:
    obj: anytype
    a_class: class containing values
    """
    return isinstance(obj, a_class)
