#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]  # Exclude the script name from arguments
    num_args = len(args)

    # Print the number of arguments
    if num_args == 0:
        print("{} argument.")
    elif num_args == 1:
        print("{} argument:")
    else:
        print(f"{} arguments:")

    # Print each argument
    for i, arg in enumerate(args, start=1):
        print(f"{i}: {arg}")
