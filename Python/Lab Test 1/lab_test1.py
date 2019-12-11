# Author: Chase Karlen
# Email: chase@uky.edu
# Section: 002


def main():
    home_value = int(input("What is the value of your home ($ thousands)? "))
    district = int(input("What district do you live in? (1,2,3) "))
    age = int(input("How old are you? "))

    tax_rate = 0
    is_exempt = False

    if age >= 65:
        print("\nYou get the homestead exemption")
        is_exempt = True

    else:
        print("\nYou don't get the homestead exemption")
        is_exempt = False

    if is_exempt:
        home_value -= 35

    if district == 1:
        tax_rate = 1.2174 * home_value
    elif district == 2:
        tax_rate = 1.0441 * home_value
    else:
        tax_rate = 1.1867 * home_value

    if home_value < 35:
        tax_rate = 0

    print("Your property tax is $", end="")
    print(round(tax_rate, 2))


main()
