# Author: Chase Karlen
# Email: chase.karlen@uky.edu
# Section: 002


def main():
    print("Practice Lab Test\n")

    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter a number: "))
    number3 = int(input("Enter a number: "))

    numbers_even = 0

    if number1 % 2 == 0:
        numbers_even += 1
    if number2 % 2 == 0:
        numbers_even += 1
    if number3 % 2 == 0:
        numbers_even += 1

    if numbers_even == 1:
        print("At least one is even")
    elif numbers_even == 2:
        print("At least one is even")
    elif numbers_even == 3:
        print("All are even")
    else:
        print("None are even")

    num_average = (number1 + number2 + number3) / 3

    print("The average is", round(num_average, 2))

    num_sum = number1 + number2 + number3

    print("The sum is", num_sum)


main()
