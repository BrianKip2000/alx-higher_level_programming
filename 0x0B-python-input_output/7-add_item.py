#!/usr/bin/python3
"""Adds all arguments to a Python list"""
import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    existing_data = load_from_json_file("add_item.json")
except Exception:
    existing_data = []

for arg in sys.argv[1:]:
    existing_data.append(arg)

save_to_json_file(existing_data, "add_item.json")
