#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
if number > 0:
    print("The number is positive")
elif number == 0:
    print("{:d} is zero".format(number))
else:
    print("{:d} is negative".format(number))