# Author: Chase Karlen
# Email: chase.karlen@uky.edu
# Section: 002
"""
Purpose: To compare numbers
Pre-conditions: The inputs will be integer numbers
Post-conditions: The output will be either 'True' or 'False'
"""

# Define main
def main():
    # Initialize variable to True
    compare = True

    # Ask for first user input
    first_number = int(input("Enter number: "))

    # Loop 4 times
    for num in range(4):
        # Ask for second user input
        second_number = int(input("Enter number: "))

        # Compare first_number with second_number
        if first_number <= second_number:
            # If first_number is less than or equal to
            # second_number
            compare = False

        # Put second_number into first_number
        second_number = first_number

    # Test boolean for True or False
    if compare:
        # If first_number is greater than second_number
        print("yes")
    else:
        # If first_number is greater than second_number
        print("no")


main()
# end of program file
