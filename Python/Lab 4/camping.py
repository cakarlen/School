# Author: Chase Karlen
# Email: chase.karlen@uky.edu
# Section: 002
'''
Purpose: To calculate a total bill based on user responses towards camping items
Preconditions: The inputs will be either a 'y' or a 'n'
Postconditions: The outputs will be the total bill, total bill plus tax, and a thank you message
'''
def main():
    # display title
    print("Camping Supply Store\n")
    # display instructions
    print("Enter y or n to answer the questions")

    # initialize total bill
    total_bill = 0
    # ask about walking stick
    walking_stick = input("Do you want a walking stick? ($15) ")
    # ask about canteen
    canteen = input("Do you want a canteen? ($10) ")
    # ask about water filter
    water_filter = input("Do you want a water filter? ($25) ")
    # ask about tent, if yes, ask about large tent
    tent = input("Do you want a tent? ($100-$150) ")

    # if walking stick is yes, add cost to bill
    if walking_stick == "y":
        total_bill += 15
    # if canteen is yes, add cost to bill
    if canteen == "y":
        total_bill += 10
    # if water filter is yes, add cost to bill
    if water_filter == "y":
        total_bill += 25
    # if tent is yes, ask for large tent
    if tent == "y":
        # if large tent is yes, add cost to bill
        large_tent = input("Do you want a large tent? ($150) ")
        if large_tent == "y":
            total_bill += 150
        else:
            total_bill += 100

    # calculate sales tax
    total_tax = round((total_bill * 0.06) + total_bill, 2)

    # print new line
    print()
    # display total bill with $ in front
    print("Your total bill is $", total_bill, ".", sep='')
    # display total bill plus tax with $ in front
    print("Your total bill plus tax is $", total_tax, ".", sep='')
    # thank them for their business
    print("Thank you for your business!")


main()










