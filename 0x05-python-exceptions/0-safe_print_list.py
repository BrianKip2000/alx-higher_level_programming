#!usr/bin/python3
# a python file that prints the items in a list
def safe_print_list(my_list=[], x=0):
    i = 0
    printed = 0

    for i in range(0, x):
        # find the items x in my list
        try:
            print(":d".format(my_list[i]), end=" ")
            elements += 1  # type: ignore
        except IndexError:
            continue
        print()
        return(printed)
