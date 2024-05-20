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

    @classmethod
    def save_to_file(cls, list_objs):
        """"""
        filename = cls.__name__ + '.json'

        with open(filename, 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]

            f.write(cls.to_json_string(list_dicts))
