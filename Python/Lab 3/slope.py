# Prolog
# Author: Chase Karlen
# Email: chase.karlen@uky.edu
# Section: 002
'''
Purpose: To find the slope and distance between points from four different numbers
Preconditions: The inputs are four floats respectively: x1, y1, x2, y2
Postconditions: The outputs will be the slope and distance of the four floats inputted
'''
# 1. Import sqrt from library math
from math import sqrt


# 2. Define main
def main():
    # 3. Introduce/greet the user
    print("Slope calculator")
    # 4. Print a blank line
    print()
    # 5. Ask user for x1 (float)
    x1 = float(input("Enter x1: "))
    # 6. Ask user for y1 (float)
    y1 = float(input("Enter y1: "))
    # 7. Ask user for x2 (float)
    x2 = float(input("Enter x2: "))
    # 8. Ask user for y2 (float)
    y2 = float(input("Enter y2: "))

    # 9. Calculate the slope
    slope = (y1 - y2) / (x1 - x2)
    # 10. Calculate the distance between points
    distance = sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

    # 11. Print a blank line
    print()
    # 12. Print the slope
    print("The slope is:", round(slope, 3))
    # 13. Print the distance
    print("The distance between the two points is:", round(distance, 3))


main()
# end of program file

# A. 7.43303, -2.8
# B. 9, 0
# C. 992.5, 9925
# D. 0, Undefined
