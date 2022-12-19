#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as val_err:
        sys.stderr.write("Exception: {}".format(val_err))
    except TypeError as typ_err:
        sys.stderr.write("Exception: {}".format(typ_err))
