#!/usr/bin/python3
"""Module conversts object to python Data Structure"""
import json


def from_json_string(my_str):
    """Using loads to convert json to python data structure"""
    return json.loads(my_str)
