# supply program prolog  - fill this in!
# Authors: Chase Karlen, Michael Harp, Mark Davidson, Christian Ennis
# Email: chase.karlen@uky.edu
# Section: 002
# include purpose, pre-conditions and post-conditions
'''
Purpose: To calculate the number of chips in a wafer based on wafer area and chip area
Preconditions: The inputs are the diameter of the wafer and the area of each chip
Postconditions: The outputs are the total wafer area, the total number of chips cut, and the chip area
'''
# import math library to use sqrt and pi
from math import sqrt, pi


# main function
def main():
    # 1. Display introductory message
    print("            000 Slicing wafers 000")
    print()
    # 2. Ask user for diameter of wafer
    diameter = float(input("What is the diameter of the wafer? (in mm): "))
    # 3. Ask user for desired area of a chip
    chip_area = float(input("What is the area of a chip? (in mm^2): "))

    # 4. Calculate the area of the wafer using the formula for area of a circle
    wafer_area = pi * ((diameter / 2) ** 2)
    # 5. Calculate the number of chips that can be cut from the
    #    wafer using formula given
    total_chips = int(diameter * pi * ((diameter / (4 * chip_area)) -
                                       (sqrt(1 / (2 * chip_area)))))

    # 6. Output a blank line
    print()
    # 7. Output the area of the wafer
    print("From a circular wafer with area", round(wafer_area, 2), "square millimeters")
    # 8. Output the (integer) number of chips cut from the wafer
    print("you can cut", total_chips, "chips, each with area", chip_area, "square millimeters")


main()
# end of program file
