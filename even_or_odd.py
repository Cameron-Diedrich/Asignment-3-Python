#!/usr/bin/env python3

# Created by: Cameron Diedrich
# Created on: October 2022
# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

from ast import Num
import math


def main():

    # input
    num = int(input("Enter any integer: "))

    # process and output
if (Num % 2) == 0:
    print("{0} is Even".format(Num))
else:
    print("{0} is Odd".format(Num))

    print("\n\nDone.")

if __name__ == "__main__":
    main()
