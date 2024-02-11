#!/usr/bin/python3
"""Creates a script that adds all arguments to a Python list,
    and then save them to a file
"""

import sys
import os

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

file = "add_item.json"
list_of_args = list(sys.argv[1:])
if os.path.exists(file):
    currentlist = load_from_json_file(file)
else:
    currentlist = []
currentlist += list_of_args
save_to_json_file(currentlist, file)
