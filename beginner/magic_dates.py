# This program uses a decision structure to calculate a magic date.
# Written by: Javier Hernandez Requena
# Date: Feb 18, 2021
# Class: CS 110A


print("Magic Date?\n")

# inputs/get data
month = int(input("Enter the number for a month: "))
day = int(input("Enter the number for a day: "))
year = int(input("Enter a two-digit year: "))

# if, else statement
if month * day == year:
    print("That date is magic!")
else:
    print("Sorry, that's just a regular date... not magic.")
