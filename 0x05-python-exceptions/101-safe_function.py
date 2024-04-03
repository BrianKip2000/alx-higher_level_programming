#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        # Call the function with the provided arguments
        result = fct(*args)
        return result
    except Exception as e:
        # If any exception occurs, print the error message to stderr
        import sys
        print("Exception: {}".format(e), file=sys.stderr)
        return None
