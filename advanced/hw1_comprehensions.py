#!/usr/bin/env python3

# Javier Hernandez Requena
# CS 231
# September 10, 2023
# Homework 1 - Palindromes
# This program prints the number of palindromes in /users/abrick/resources/english



# read file with words and put into list
try:
    with open('/users/abrick/resources/english') as file:
        words = file.read().splitlines()
except FileNotFoundError:
    print("File not found. Please check the file path and try again.")
    exit(1)

# list comprehension to find all palindromes
palindromes = [i for i in words if i and i == i[::-1]]

# print number of palindromes
print("There are " + str(len(palindromes)) + " palindromes in the file.")
