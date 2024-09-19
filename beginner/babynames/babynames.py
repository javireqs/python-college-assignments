# This program takes the inputs of a boy's name, a girl's name, or neither (N), and
# outputs a message indicating whether the names were among the most popular.
# This program demonstrates the ability to to read data from a text-file
# into a Python list for some simple data analysis.
# Inputs: boyNames, girlNames, or 'N'
# Outputs: most popular name message
# Written by: Javier Hernandez Requena
# Date: March 20, 2021
# Class: CS 110A


# main function
def main():

    # try statement
    try:

        # open file, read file to list, close file
        boyNames = open('BoyNames.txt', 'r')
        boys = boyNames.readlines()
        boyNames.close()
        # strip \n
        index = 0
        while index < len(boys):
            boys[index] = boys[index].rstrip('\n')
            index += 1

        # open file, read file to list, close file
        girlNames = open('GirlNames.txt', 'r')
        girls = girlNames.readlines()
        girlNames.close()
        # strip \n
        index = 0
        while index < len(girls):
            girls[index] = girls[index].rstrip('\n')
            index += 1
        
        # get input
        boysInput = input('Enter a boy\'s name, or N if you do not wish to enter a boy\'s name: ')
        girlsInput = input('Enter a girl\'s name, or N if you do not wish to enter a girl\'s name: ')

        # analyze boysInput in list & display result
        if boysInput in boys:
            print(boysInput + ' is one of the most popular boy\'s names.')
        elif boysInput == 'N':
            print('You chose not to enter a boy\'s name.')
        else:
            print(boysInput + ' is not one of the most popular boy\'s names.')

        # analyze girlsInput in list & display result          
        if girlsInput in girls:
            print(girlsInput + ' is one of the most popular girl\'s names.')
        elif girlsInput == 'N':
            print('You chose not to enter a girl\'s name.')
        else:
            print(girlsInput + ' is not one of the most popular girl\'s names.')
        
    # exception
    except IOError:
        print('An error occured trying to read the file.')

# call main function
main()
