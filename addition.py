#!/usr/bin/env python3

# Created by: Zaida Hammel
# Created on: Oct 2022
# This program adds two numbers and finds the sum


def main():
    # this function adds two numbers
    # input
    print("This program adds two numbers and finds the sum.")

    num1 = int(input("Enter the the first number: "))
    num2 = int(input("Enter the the second number: "))
    # process
    total = num1 + num2
    # output
    print("")
    print("The sum of {0:,.0f} + {1:,.0f} = {2:,.0f}".format(num1, num2, total))
    print("\nDone.")


if __name__ == "__main__":
    main()
