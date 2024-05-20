#!/usr/bin/python3
"""Main class for almost circle"""
import json


class Base:
    """Base class for entire project"""
    __nb_obj = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_obj += 1
            self.id = Base.__nb_obj

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts dictionary to JSON string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return (json.dumps(list_dictionaries))
