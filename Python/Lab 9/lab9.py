# Author: Chase Karlen
# Email: chase@uky.edu
# Section: 002
"""
Purpose: To generate random lists to be low/high filtered
Preconditions: The input will be a number
Postconditions: The outputs will be a list non-filtered, a list high filtered,
                a list low filtered, and a sum of all lists
"""
# Import randrange from random
from random import randrange
from graphics import *

# Define main
def main():
    # Initialize variables for filtering
    low_filter = 50
    high_filter = 200
    # Initialize first list
    init_list = []

    # Ask user for how many samples
    user_input = int(input("How many samples? "))
    # Print generating list
    print("generating random list")

    # For i in range of 0 to user input
    for i in range(0, user_input):
        # Generate random number between 1 and 350 and store in variable
        rand_num = randrange(1, 351)
        # Add random number variable to first list
        init_list.append(rand_num)
    # Print out the first list
    print("The list is", init_list, "\n")
    # Copy first list to high list to be high filtered
    high_list = init_list.copy()

    # Print filtering list for highs
    print("Filtering for highs with upperlimit =", high_filter)

    # For i in range of high list
    for i in range(len(high_list)):
        # If i in high list is greater than or equal to the high filter
        if high_list[i] >= high_filter:
            # Set i in high list to 200
            high_list[i] = 200
    # Print high list
    print("The list is", high_list, "\n")
    # Copy high list to low list to be low filtered
    low_list = high_list.copy()

    # Print filtering list for lows
    print("Filtering for lows with lowerlimit =", low_filter)

    # For i in range of low list
    for i in range(len(low_list)):
        # If i in low list is less than or equal to the low filter
        if low_list[i] <= low_filter:
            # Set i in low list to 50
            low_list[i] = 50
    # Print low list
    print("The list is", low_list, "\n")

    # Get sum of first list
    init_sum = sum(init_list)
    # Get sum of high list
    high_sum = sum(high_list)
    # Get sum of low list
    low_sum = sum(low_list)
    # Get total of all 3 lists
    total = init_sum + high_sum + low_sum

    # If total is equal to 0
    if total == 0:
        # Cannot divide by 0
        print("Size is zero, average value is zero")
    # If total is not equal to 0
    else:
        # Get average
        average = total / 3
        # Print average
        print("The average value is", round(average, 3))


main()
# end of program file

"""
TEST CASES

1. Zero samples:
    How many samples? 0
    generating random list
    The list is [] 
    
    Filtering for highs with upperlimit = 200
    The list is [] 
    
    Filtering for lows with lowerlimit = 50
    The list is [] 
    
    Size is zero, average value is zero
    
2. 1 sample:
    How many samples? 1
    generating random list
    The list is [164] 
    
    Filtering for highs with upperlimit = 200
    The list is [164] 
    
    Filtering for lows with lowerlimit = 50
    The list is [164] 
    
    The average value is 164.0
    
3. More than 1 sample:
    How many samples? 3
    generating random list
    The list is [283, 23, 93] 
    
    Filtering for highs with upperlimit = 200
    The list is [200, 23, 93] 
    
    Filtering for lows with lowerlimit = 50
    The list is [200, 50, 93] 
    
    The average value is 352.667

4. Negative sample size:
    How many samples? -10
    generating random list
    The list is [] 
    
    Filtering for highs with upperlimit = 200
    The list is [] 
    
    Filtering for lows with lowerlimit = 50
    The list is [] 
    
    Size is zero, average value is zero
    
5. Limits same value (100):
    How many samples? 10
    generating random list
    The list is [124, 263, 277, 3, 96, 37, 302, 231, 107, 172] 
    
    Filtering for highs with upperlimit = 100
    The list is [200, 200, 200, 3, 96, 37, 200, 200, 200, 200] 
    
    Filtering for lows with lowerlimit = 100
    The list is [200, 200, 200, 50, 50, 50, 200, 200, 200, 200] 
    
    The average value is 1566.0

6. Upper limit (50) lower than the lower limit (100):
    How many samples? 10
    generating random list
    The list is [264, 158, 178, 38, 136, 342, 153, 159, 274, 16] 
    
    Filtering for highs with upperlimit = 50
    The list is [200, 200, 200, 38, 200, 200, 200, 200, 200, 16] 
    
    Filtering for lows with lowerlimit = 100
    The list is [200, 200, 200, 50, 200, 200, 200, 200, 200, 50] 
    
    The average value is 1690.667
    
7. Lower limit (150) lower than lowest number generated:
    How many samples? 10
    generating random list
    The list is [142, 93, 311, 190, 173, 80, 267, 104, 154, 287] 
    
    Filtering for highs with upperlimit = 200
    The list is [142, 93, 200, 190, 173, 80, 200, 104, 154, 200] 
    
    Filtering for lows with lowerlimit = 150
    The list is [50, 50, 200, 190, 173, 50, 200, 50, 154, 200] 
    
    The average value is 1551.333
    
8. Upper limit (350) higher than the highest number generated:
    How many samples? 15
    generating random list
    The list is [89, 86, 337, 53, 105, 95, 247, 2, 153, 244, 1, 335, 137, 168, 294] 
    
    Filtering for highs with upperlimit = 350
    The list is [89, 86, 337, 53, 105, 95, 247, 2, 153, 244, 1, 335, 137, 168, 294] 
    
    Filtering for lows with lowerlimit = 50
    The list is [89, 86, 337, 53, 105, 95, 247, 50, 153, 244, 50, 335, 137, 168, 294] 
    
    The average value is 2378.333
"""
