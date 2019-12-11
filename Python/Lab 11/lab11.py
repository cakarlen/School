# Author: Chase Karlen
# Email: chase@uky.edu
# Section: 002
"""
Purpose: To calculate payroll based on employee, hourly rate, and hours worked
Preconditions: The inputs are employee name, hourly rate, and hours worked
Postconditions: The outputs are total payroll, employee name, and pay based on rate*hours worked
"""
# Define main
def main():
    # Print title
    print("Payroll for ACME\n")

    # Initialize variables
    employees = []
    total_pay = 0

    # Get initial user input
    user_input = input("Press Enter to stop\nEnter name, comma, hours worked, comma, hourly rate: ")

    # While user input doesn't equal space
    while user_input != "":
        # Split user input based on ","
        user_split = user_input.split(",")

        # Find individual pay based on index of 1 and 2 in user_split
        indiv_pay = float(user_split[1]) * float(user_split[2])
        # Add individual pay to total_pay accumulator
        total_pay += indiv_pay
        # Append name and individual pay to employees list
        employees.append([user_split[0], indiv_pay])

        # Prompt for user input again
        user_input = input("Enter name, comma, hours worked, comma, hourly rate: ")

    # Print total payroll
    print("Total payroll ", "$", total_pay, sep="")

    # For loop checking length of employees list
    for i in range(len(employees)):
        # Alphabetize employees
        employees.sort()
        # Print employee name
        print(employees[i][0], "\t", end="")
        # Print perspective employee's pay
        print("$", employees[i][1], sep="")


main()
# end of program file
