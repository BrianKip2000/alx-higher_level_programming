#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        # Try to convert the value to an integer and print it
        print("{:d}".format(value))
        return True
    except Exception as e:
        # If any exception occurs, print the error message to stderr
        import sys
        print("Exception: {}".format(e), file=sys.stderr)
        return False
