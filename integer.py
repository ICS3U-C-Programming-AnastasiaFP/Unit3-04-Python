#!/usr/bin/env python3
# Created by: Anastasia Friedenstein Patino
# Created on: October. 20, 2023
# Program determines wether integer is positive or negative

# Get input from the user

integer = int(input("Enter an integer:"))

# Check if the integer is greater than 0
if integer > 0:
    print(f"{integer} is a positive number")
# Check if the integer is less than 0
elif integer < 0:
    print(f"{integer} is a negative number")
# If neither condition is met
else:
    print(f"{integer} is just zero!")
