# Author: Chase Karlen
# Email: chase@uky.edu
# Section: 002
"""
Purpose: To calculate the square root of a number using Newton's method
Preconditions: The input will be a number
Postconditions: The outputs will be the total number of iterations
                used to accurately calculate the square root
"""
# Import math library
from math import *


# Define main
def main():
    # Get input for number
    number = float(input("What number do you want to take the square root of? "))
    # Calculate initial guess
    initial_guess = number / 2
    # Calculate new guess with initial guess and number
    new_guess = 0.5 * (initial_guess + number / initial_guess)

    # Initialize counter for loop
    counter = 1
    # Initialize while loop
    while abs(initial_guess - new_guess) >= 1e-10:
        # Print out number of iterations
        print("Iteration", counter, initial_guess)
        # Put new guess in initial guess
        new_guess = initial_guess
        # Recalculate initial guess
        initial_guess = 0.5 * (initial_guess + number / initial_guess)
        # Add 1 to counter
        counter += 1

    # Calculate actual square root using math library
    actual_sqrt = sqrt(number)
    # Print actual square root
    print("The square root from the math library is", actual_sqrt)
    # Get difference between 2 square roots
    difference_sqrt = initial_guess - actual_sqrt
    # Print different between 2 square roots
    print("The difference between Newton's method and the math library function is", difference_sqrt)


# Call main
main()
# end of program file

"""
TEST CASES

1. 4.0, Iteration 6
2. 4.24, Iteration 6
3. 100.0, Iteration 11
4. 4.68, Iteration 4
5. ZeroDivisionError, Iteration 1
"""
