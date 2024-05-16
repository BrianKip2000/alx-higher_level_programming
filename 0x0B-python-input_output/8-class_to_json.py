#!/usr/bin/python3
"""Module of class to json"""


def class_to_json(obj):
    """
    Serialize an object into a JSON-serializable dictionary.

    Args:
    - obj: An instance of a Class

    Returns:
    - A dictionary containing the serialized attributes of the object.
    """
    json_class = {}

    for attribute_name in dir(obj):
        if not attribute_name.startswith('__'):
            attribute_value = getattr(obj, attribute_name)

            if isinstance(attribute_name, (list, dict, str, int, bool)):
                json_class[attribute_name] = attribute_value
            elif not callable(attribute_value):
                json_class[attribute_name] = class_to_json(attribute_value)

    return json_class
