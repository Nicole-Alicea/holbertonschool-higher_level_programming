#!/usr/bin/python3
"""Creates a function that returns the JSON representation of an object"""


import json


def to_json_string(my_obj):
    """Will return the JSON representation of an object(string)"""
    return json.dumps(my_obj)
