# Author: Chase Karlen
# Email: chase.karlen@uky.edu
# Section: 002
"""
Purpose: To calculate the resistance and current from series and parallel circuits
Pre-conditions: The inputs will be the 3 resistors in ohms
Post-conditions: The outputs will be the resistance and current from the pre-conditions
"""
# Import sqrt from math
from math import sqrt


# Define main()
def main():
    # Display title and author
    print("\tResistor Calculations\n\tby Chase Karlen\n")
    # Input the 3 resistances and the power for the circuits
    resistor1 = float(input("Enter the resistance of the first resistor (ohms): "))
    resistor2 = float(input("Enter the resistance of the second resistor (ohms): "))
    resistor3 = float(input("Enter the resistance of the third resistor (ohms): "))
    power = float(input("How much power (in watts)? "))
    # Print new line
    print()

    # Calculate the resistance of the two circuits, serial and parallel
    resist_series = resistor1 + resistor2 + resistor3

    # Prevent division by zero by checking the 3 inputs for zero value
    if resistor1 == 0 or resistor2 == 0 or resistor3 == 0:
        # at least one resistance was zero, make parallel result very large (1e300)
        print("One of the resistors is zero. Parallel resistance set to 1e300.")
        resist_parallel = 1e300
    # If none are zero, resistances are ok
    else:
        # Calculate the regular parallel resistance
        resist_parallel = (1 / ((1 / resistor1) + (1 / resistor2) + (1 / resistor3)))

    # Calculate the current of the series and parallel
    current_series = sqrt(power / resist_series)
    current_parallel = sqrt(power / resist_parallel)

    # Print the resistance of the series and parallel with rounding to 3 decimals
    print("The resistance of these three resistors in series is:", round(resist_series, 3), "ohms")
    print("The resistance of these three resistors in parallel is:", round(resist_parallel, 3), "ohms\n")
    # Print the current of the series and parallel with rounding to 3 decimals
    print("The current in the circuit with the resistors in series is", round(current_series, 3),
          "amps when the power is", power, "watts.")
    print("The current in the circuit with the resistors in parallel is", round(current_parallel, 3),
          "amps when the power is", power, "watts.")


main()
# end of program file

"""
DESIGN

Prolog with 3 P's
Import sqrt from math
Define main()
Display title and author
Input the 3 resistances and the power for the circuits in floats
Print new line
Calculate the resistance of the two circuits, serial and parallel
Prevent division by zero by checking the 3 inputs for zero value
    at least one resistance was zero, make parallel result very large (1e300)
    If none are zero, resistances are ok
        Calculate the regular parallel resistance
Calculate the current of the series and parallel using sqrt function
Print the resistance of the series and parallel with rounding to 3 decimals
Print the current of the series and parallel with rounding to 3 decimals
Call main()
end of program file
"""
