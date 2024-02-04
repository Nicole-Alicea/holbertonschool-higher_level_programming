#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        undefined_variable
    except NameError as e:
        raise NameError(f"{message}: {e}")
