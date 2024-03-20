#!/usr/bin/python3
import sys

def main():
    args = sys.argv[1:]  # Exclude the script name from arguments
    num_args = len(args)

    # Print the number of arguments
    if num_args == 0:
        print("0 argument.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print(f"{num_args} arguments:")

    # Print each argument
    for i, arg in enumerate(args, start=1):
        print(f"{i}: {arg}")

if __name__ == "__main__":
    main()
