#!/usr/bin/python3
"""Module for class Student"""


class Student:
    """Class for student initiation"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dict representation of json"""
        return self.__dict__
