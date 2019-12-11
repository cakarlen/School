# Prolog
# Author:  Chase Karlen
# Email:  chase.karlen@uky.edu
# Section: 002
"""
  Purpose: to find the average of two floating point numbers,
    given the two numbers.
  Preconditions: (input)
    User supplies the two numbers
  Postconditions: (outputs)
    User greeted and prompted for the two numbers
    The average of the two numbers is displayed.
"""


def main():
    # 1. Greet the user
    print("Average Finder\n")

    # 2. Get one number (float)
    value1 = float(input("First Number: "))  # Error 1: Ending parenthesis needed to complete the statement

    # 3. Get other number (float)
    value2 = float(input("Second Number: "))

    # 4. Calculate the average
    average = (value1 + value2) / 2  # Error 2: Parenthesis needed around value1 and value2 to correctly calculate the average

    # 5. Display a blank line.
    print()

    # 6. Display average
    print("The average is", round(average, 2))


main()
# end of program file
