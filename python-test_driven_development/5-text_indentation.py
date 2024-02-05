#!/usr/bin/python3
"""This function prints a text with 2 new lines"""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        # print(delim, text.split(delim))
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")
