#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Initialize an empty list to store the results
    result_list = []

    # Iterate through the input list
    for num in my_list:
        # Check if the current number is divisible by 2
        if num % 2 == 0:
            # If divisible by 2, append True to the result list
            result_list.append(True)
        else:
            # If not divisible by 2, append False to the result list
            result_list.append(False)

    return result_list
