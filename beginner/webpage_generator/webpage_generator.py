# This program asks a user for their name, then asks the user
# to enter a line describing something about themselves.
# Once the user has entered the requested input, this program
# creates a simple web page (external HTML file) using the users' information.
# Inputs: name, descr
# Outputs: Simple web page with Name and Description
# Written By: Javier Hernandez Requena
# Date: March 15, 2021
# Class: CS 110A


# just in case
import os

# main function
def main():

    # define input variables
    name = input('Enter your name: ')
    descr = input('Describe yourself: ')

    # open file using fileObject
    my_page = open('my_page.html', 'w')

    # write contents to file
    my_page.write('<html>' + '\n')
    my_page.write('\t' + '<head>' + '\n')
    my_page.write('\t' + '<title>' + name + '\'s Web Page' '</title>' + '\n')
    my_page.write('\t' + '</head>' + '\n')
    my_page.write('\t' + '<body>' + '\n')
    my_page.write('\t' + '<center>' + '\n')
    my_page.write('\t\t' + '<h1>' + name + '</h1>' + '\n')
    my_page.write('\t' + '</center>' + '\n')
    my_page.write('\t' + '<hr />' + '\n')
    my_page.write('\t' + descr + '\n')
    my_page.write('\t' + '<hr />' + '\n')
    my_page.write('\t' + '</body>' + '\n')
    my_page.write('</html>' + '\n')

    # close file
    my_page.close()
    print('File Created.')

# call main function
main()
