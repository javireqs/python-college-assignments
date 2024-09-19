# This program allows the user to choose various
# geometry calculations from a menu. This program
# imports the circle and rectangle modules.
import circle
import rectangle
import stadium

# Constants for the menu choices
AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
AREA_STADIUM_CHOICE = 5
PERIMETER_STADIUM_CHOICE = 6
QUIT_CHOICE = 7

# The main function.
def main():
    # The choice variable controls the loop
    # and holds the user's menu choice.
    choice = 0

    while choice != QUIT_CHOICE:
        # display the menu.
        display_menu()

        # Get the user's choice.
        choice = int(input('Enter your choice: '))

        # Perform the selected action.
        if choice == AREA_CIRCLE_CHOICE:
            radius = float(input("Enter the circle's radius: "))
            print('The area is', circle.area(radius))
        elif choice == CIRCUMFERENCE_CHOICE:
            radius = float(input("Enter the circle's radius: "))
            print('The circumference is', \
                  circle.circumference(radius))
        elif choice == AREA_RECTANGLE_CHOICE:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print('The area is', rectangle.area(width, length))
        elif choice == PERIMETER_RECTANGLE_CHOICE:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print('The perimeter is', \
                  rectangle.perimeter(width, length))
        elif choice == AREA_STADIUM_CHOICE:
            radius = float(input("Enter the stadium's radius: "))
            length = float(input("Enter the stadium's side length: "))
            print('The area is', format(stadium.area(radius, length), '.2f'))
        elif choice == PERIMETER_STADIUM_CHOICE:
            radius = float(input("Enter the stadium's radius: "))
            length = float(input("Enter the stadium's side length: "))
            print('The perimeter is', \
                  format(stadium.perimeter(radius, length), '.2f'))
        elif choice == QUIT_CHOICE:
            print('Exiting the program...')
        else:
            print('Error: invalid selection.')
    
# The display_menu function displays a menu.
def display_menu():
    print('        MENU')
    print('1) Area of a circle')
    print('2) Circumference of a circle')
    print('3) Area of a rectangle')
    print('4) Perimeter of a rectangle')
    print('5) Area of a stadium')
    print('6) Perimeter of a stadium')
    print('7) Quit')

# Call the main function.
main()
