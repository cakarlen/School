# Author: Chase Karlen
# Email: chase@uky.edu
# Section: 002
"""
Purpose: To perform calculations on finding leap year
Preconditions: The input is its parameter, an integer year
Postconditions: The output will be a boolean value, True or False, depending on leap year
"""
def check_year(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                result = True
            else:
                result = False
        else:
            result = True
    else:
        result = False

    return result


"""
Purpose: To determine if an inputted year is a leap year
Preconditions: The input will be a year
Postconditions: The output will be a yes or no if the year is a leap year
"""
def main():
    user_input = int(input("Enter a year: "))

    while user_input != -1:
        answer = check_year(user_input)
        if answer:
            print("Yes, it is a leapyear")
        else:
            print("No, it is not a leapyear")
        user_input = int(input("Enter a year: "))


main()
