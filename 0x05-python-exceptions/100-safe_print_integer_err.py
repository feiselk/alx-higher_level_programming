#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        # Try to format the value as an integer and print it
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        # Catch ValueError and TypeError exceptions
        print(f"Exception: {e}", file=sys.stderr)
        return False
