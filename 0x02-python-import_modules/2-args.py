#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_argv = len(sys.argv) - 1

    # Print the number of arguments
    if num_argv == 0:
        print("{} argument.".format(num_argv))
    elif num_argv == 1:
        print("{} argument:".format(num_argv))
    else:
        print("{} arguments:".format(num_argv))

    # Print each argument
    if num_argv >= 1:
        num_argv = 0

        for arg in sys.argv:
            if num_argv != 0:
                print("{} :{}".format(num_argv, arg))
