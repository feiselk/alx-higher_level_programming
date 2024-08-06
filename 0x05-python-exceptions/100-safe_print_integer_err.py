#!/usr/bin/python3

def safe_print_integer_err(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        elif isinstance(value, dict):
            raise TypeError
            return False

        else:
            raise TypeError
    except TypeError:
        print("Exception: Unknown format code 'd' for object of type 'str'")
        return False
