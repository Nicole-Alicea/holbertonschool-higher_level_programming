#!/usr/bin/python3
"""Creates a function that reads a text file"""


def read_file(filename=""):
    """Reads a text file(UTF8) and prints it to stdout"""
    with open(filename, 'r', encoding="utf-8") as f_obj:
        content = f_obj.read()
    print(content, end="")
