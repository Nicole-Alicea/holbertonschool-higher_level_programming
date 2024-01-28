#!/usr/bin/python3

for alphabet in range(97, 123):
    if chr(alphabet) not in {'q', 'e'}:
        print("{}".format(chr(letter)), end="")
