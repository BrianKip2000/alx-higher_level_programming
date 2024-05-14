#!/usr/bin/python3
"""Modue for checking whether theyare in the same class"""


def is_same_class(obj, a_class):
    """function for checking whether obj and a_class are in same class"""
    return type(obj) is a_class
