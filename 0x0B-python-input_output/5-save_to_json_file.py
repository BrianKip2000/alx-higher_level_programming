#!/usr/bin/python3
"""Save to json"""
import json


def save_to_json_file(my_obj, filename):
    """Function dump() to save to json file"""
    with open(filename, 'w', encoding='utf-8') as new_save:
        return json.dump(my_obj, new_save)
