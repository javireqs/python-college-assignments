# This module contains two function defintions
# and returns the area and perimeter of a stadium.
# Written by: Javier Hernandez Requena
# Date: Mar 9, 2021
# Class: CS 110A


import math

def area(radius, length):
    return (math.pi * radius**2) + (2 * radius * length)

def perimeter(radius, length):
    return 2 * (math.pi * radius + length)
