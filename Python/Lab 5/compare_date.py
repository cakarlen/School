# Author: Chase Karlen
# Email: chase.karlen@uky.edu
# Section: 002
"""
Purpose: To compare user-inputted dates
Pre-conditions: The inputs are the first month, day, and year and the second month, day, and year
Post-conditions: The output will be Date1 is the same/earlier/later to Date2
"""


# Define main
def main():
    # Ask user for first month, day, and year
    first_month = int(input("Enter first month: "))
    first_day = int(input("Enter first day: "))
    first_year = int(input("Enter first year: "))

    # Ask user for second month, day, and year
    second_month = int(input("\nEnter second month: "))
    second_day = int(input("Enter second day: "))
    second_year = int(input("Enter second year: "))

    # Initialize result variable to None (null)
    result = None

    # If first_year does not equal second_year
    if first_year != second_year:
        # If first_year is greater than second_year
        if first_year > second_year:
            # Set result to 2 (First date is later than second date)
            result = 2
        # If first_year is less than second_year
        else:
            # Set result to 1 (First date is earlier than second date)
            result = 1
    # If first_year is equal to second_year
    elif first_year == second_year:
        # If first_month does not equal second_month
        if first_month != second_month:
            # If first_month is greater than second_month
            if first_month > second_month:
                # Set result to 2 (First date is later than second date)
                result = 2
            # If first_month is less than second_month
            else:
                # Set result to 1 (First date is earlier than second date)
                result = 1
        # If first_month is equal to second_month
        else:
            # If first_day does not equal second_day
            if first_day != second_day:
                # If first_day is greater than second_day
                if first_day > second_day:
                    # Set result to 2 (First date is later than second date)
                    result = 2
                # If first_day is less than second_day
                else:
                    # Set result to 1 (First date is earlier than second date)
                    result = 1
            # If first_day is equal to second_day
            else:
                # Set result to 0 (First date is the same as second date)
                result = 0

    # Print date1 with first_* variables
    print("\nDate1:", end=" ")
    print(first_month, first_day, first_year,
          sep="/", end=" ")

    # Print comparative messages using result
    if result == 0:
        print("is the same as Date2:", end=" ")
    elif result == 1:
        print("is earlier than Date2:", end=" ")
    elif result == 2:
        print("is later than Date2:", end=" ")

    # Print date2 with second_* variables
    print(second_month, second_day, second_year, sep="/")


# Call main
main()
# end of program file

"""
D1, D2, D3, D4, D5, D6, D7

D1: result = 1
D2: result = 2
D3: result = 1
D4: result = 2
D5: result = 1
D6: result = 2
D7: result = 0
"""

"""
TEST CASES

2.  A. 1, 9, 99
    B. 12, 9, 99
    C. Date1: 1/9/99 is earlier than Date2: 12/9/99
3.  A. 12, 1, 99
    B. 12, 31, 99
    C. Date1: 12/1/99 is earlier than Date2: 12/31/99
4.  A. 12, 31, 19
    B. 12, 31, 12
    C. Date1: 12/31/19 is later than Date2: 12/31/12
5.  A. 12, 9, 99
    B. 11, 9, 99
    C. Date1: 12/9/99 is later than Date2: 11/9/99
6.  A. 12, 31, 99
    B. 12, 30, 99
    C. Date1: 12/31/99 is later than Date2: 12/30/99
7.  A. 1, 2, 19
    B. 1, 2, 19
    C. Date1: 1/2/19 is the same as Date2: 1/2/19
"""
