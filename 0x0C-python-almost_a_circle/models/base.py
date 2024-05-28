#!/usr/bin/python3
"""Main class for almost circle"""
import json
import csv


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

    @staticmethod
    def from_json_string(json_string):
        """returns list of JSON string representation"""
        if json_string is None or json_string == "":
            return []
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Returns a instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            cls()
        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = f"{cls.__name__}.json"

        try:
            with open(filename, 'r') as file:
                json_file = file.read()
        except Exception:
            return []

        json_list = cls.from_json_string(json_file)
        instances = [cls.create(**item) for item in json_list]
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves file from csv"""
        filename = f"{cls.__name__}.csv"

        if filename == 'Rectangle.csv':
            fields = ['id', 'width', 'height', 'x', 'y']
        elif filename == 'Square.csv':
            fields = ['id', 'size', 'x', 'y']

        with open(filename, 'w', newline='') as file:
            if list_objs is None:
                writer = csv.writer(file)
                writer.writerow([[]])
            else:
                writer = csv.DictWriter(file, fieldnames=fields)
                writer.writeheader()
                for w in list_objs:
                    writer.writerow(w.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes a csv file and returns a list of instances"""
        try:
            filename = f"{cls.__name__}.csv"

            with open(filename, newline='') as fn:
                reading = csv.DictReader(fn)
                lis = []
                for x in reading:
                    for i, n in x.items():
                        x[i] = int(n)
                    lis.append(x)
                return (cls.create(**objects) for objects in lis)
        except FileNotFoundError:
            return []
