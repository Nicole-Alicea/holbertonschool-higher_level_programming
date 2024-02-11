#!/usr/bin/python3
"""Creates a function that creates an Object from a 'Json file'"""

import json


def load_from_json_file(filename):
    """Creates an Object from a 'JSON file'"""
    with open(filename) as f_obj:
        return json.load(f_obj)
