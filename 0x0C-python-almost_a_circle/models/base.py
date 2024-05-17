#!/usr/bin/python3
"""Main class for almost circle"""


class Base:
    """Base class for entire project"""
    __nb_obj = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_obj += 1
            self.id = Base.__nb_obj
