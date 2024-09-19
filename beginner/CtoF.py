# This program displays a table of Celsius
# temperatures and their Fahrenheit equivalents
# using a for loop and the range function.
# Inputs: none
# Outputs: Celsius & Fahrenheit Temperature Table
# Written by: Javier Hernandez Requena
# Date: Feb. 23, 2021
# Class: CS 110A


# print table headings.
print('Celsius\tFahrenheit')
print('------------------')

# print celsius temperatures
# and their fahrenheit equivalents.
for c in range(-20, 20, 2):
    fahrenheit = 9/5*c + 32
    print(c, '\t', format(fahrenheit, '.1f'))

# end table
print('------------------')
