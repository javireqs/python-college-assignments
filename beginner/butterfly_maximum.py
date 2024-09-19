# This program allows users to input a series of integers that represent
# butterflies collected in a day.
# Inputs: Number of butterflies
# Outputs: Total butterflies and Max butterflies in a day
# Written by: Javier Hernandez Requena
# Date: Feb. 26, 2021
# Class: CS 110A

# Print heading
print('WELCOME TO THE BUTTERFLY COLLECTING PROGRAM\n\n')

# Get the number of butterflies collected per day
print('Enter the number of butterflies you have collected for each day you spent in the field.')
print('Please enter -1 when finished.\n\n')
butterflies = int(input('Enter the number of butterflies collected (or -1 to end):\n'))

total = 0
maximum = 0


# Sentinel
while butterflies != -1:
    # Running total
    total = total + butterflies
    # Nested if statement
    if maximum < butterflies:
            maximum = butterflies

    butterflies = int(input('Enter the number of butterflies collected (or -1 to end):\n'))

# Print footing
print('\n\nHERE ARE THE RESULTS OF YOUR BUTTERFLY COLLECTING')
# Print Total and Maximum bugs caught
print('Total bugs collected: ', total)
print('Maximum bugs collected: ', maximum)
