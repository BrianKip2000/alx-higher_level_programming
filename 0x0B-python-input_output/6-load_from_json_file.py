#!/usr/bin/python3
"""load from json file Module"""
import json


def load_from_json_file(filename):
    """Module to load from json file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
