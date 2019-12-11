# Author: Chase Karlen
# Email: chase@uky.edu
# Section: 002
"""
Purpose: To guess a coordinate based on textual clues
Pre-conditions: The inputs will be if users want to test, difficulty level,
                and x, y guesses
Post-conditions: The outputs will be how close the user guesses to the coordinates
                 randomly generated and the distance (if user is in test mode)
"""
from random import randrange
from math import sqrt
from graphics import *

"""
Purpose: To find the distance between 4 points
Pre-conditions: The inputs are the function's parameters: x1, y1, x2, y2
Post-conditions: The output is the distance based on the parameters
"""

def distance(point1, point2):
    # all four parameters are integers
    # they represent the coordinates of two points
    # the distance between the two points is returned
    return int(sqrt((point2.getX() - point1.getX()) ** 2
                    + (point2.getY() - point1.getY()) ** 2))

def main():
    win = GraphWin("Find the animal", 500, 500)

    # Initialize random values
    rand_x = randrange(1, 501)
    rand_y = randrange(1, 501)
    rand_point = Point(rand_x, rand_y)
    # Initialize counter variable
    counter = 0
    # Initialize testing flag to False
    is_testing = False

    animal_message = Text(Point(250, 10), "Find the invisible animal!")

    test_box = Entry(Point(250, 150), 10)
    test_text = Text(Point(250, 130), "Testing mode?")

    difficulty_box = Entry(Point(250, 150), 10)
    difficulty_text = Text(Point(250, 130), "Difficulty?")

    guess_text = Text(Point(250, 480), "Animal")
    guess_text.setSize(35)

    counter_text = Text(Point(475, 10), "%d clicks" % counter)
    pic = Image(rand_point, "animal.gif")

    animal_message.draw(win)
    test_box.draw(win)
    test_text.draw(win)

    win.getMouse()
    test_input = test_box.getText()

    # Check if user inputs either "Y/y" or "N/n" or enter, if not, ask again
    while test_input != "y" and test_input != "Y" and \
            test_input != "n" and test_input != "N" and test_input != '':
        # Prompt user again
        win.getMouse()
        test_input = test_box.getText()

    test_box.undraw()
    test_text.undraw()
    difficulty_box.draw(win)
    difficulty_text.draw(win)

    # If user inputs y/Y
    if test_input == "y" or test_input == "Y":
        # Set testing flag to True
        is_testing = True
        win.getMouse()
        difficulty = difficulty_box.getText()
        # If user hits enter on difficulty
        if difficulty == '':
            # Set difficulty to 5
            difficulty_int = 5
        # If user enters a number 1-25
        else:
            # Typecast difficulty to int for later usage
            difficulty_int = int(difficulty)
    # If user inputs enter or n/N
    else:
        # Prompt user for difficulty
        win.getMouse()
        difficulty = difficulty_box.getText()
        # If user hits enter on difficulty
        if difficulty == '':
            # Set difficulty to 5
            difficulty_int = 5
        # If user enters a number 1-25
        else:
            # Typecast difficulty to int for later usage
            difficulty_int = int(difficulty)

    # Check if difficulty is between 1 to 25 and nothing else
    while difficulty_int < 1 or difficulty_int > 250:
        # Tell user to enter valid number
        # print("Invalid difficulty, 1-25 allowed")
        # Prompt user again
        # difficulty_int = int(input("Difficulty? (smaller is harder) "))
        win.getMouse()
        difficulty = difficulty_box.getText()
        difficulty_int = int(difficulty)

    difficulty_box.undraw()
    difficulty_text.undraw()

    user_guess = win.getMouse()

    if is_testing:
        pic.draw(win)

    distance_text = Text(Point(35, 10), "Distance %d" % distance(user_guess, rand_point))

    guess_text.draw(win)
    counter_text.draw(win)

    # While distance between points is greater than difficulty
    while distance(user_guess, rand_point) > difficulty_int:
        # Print to user to guess
        # print("\nGive me a guess (x and y between 1 and 50)")
        # Input for x
        # guess_x = int(input("x? "))
        # Input for y
        # guess_y = int(input("y? "))
        user_guess = win.getMouse()
        new_guess = user_guess.clone()
        new_guess.draw(win)

        # Add one to counter to show user at the end
        counter += 1
        counter_text.undraw()
        counter_text = Text(Point(475, 10), "%d clicks" % counter)
        counter_text.draw(win)

        distance_text.undraw()
        distance_text = Text(Point(35, 10), "Distance %d" % distance(user_guess, rand_point))

        # If distance between points is less or equal to difficulty
        if distance(new_guess, rand_point) <= difficulty_int:
            #print("\nYou found him!\nYay!!")
            #print("It took you", counter, "tries")
            if not is_testing:
                pic.draw(win)
            elif is_testing:
                distance_text.draw(win)
            guess_text.setFill("red")
            win_text = Text(Point(250, 250), "You found the animal!\n"
                                             "It took you %d clicks" % counter)
            win_text.setSize(36)
            win_text.draw(win)

            close_text = Text(Point(250, 350), "Click to close")
            close_text.setSize(36)
            close_text.draw(win)
        # If distance between points is less than or equal to 10
        elif difficulty_int > distance(new_guess, rand_point) <= 100:
            if is_testing:
                #print("Distance is:", distance(new_guess, rand_point))
                distance_text.draw(win)
            #print("You're close!")
            guess_text.setFill("firebrick")
        # If distance between points is more or equal to 10 and less than
        # or equal to 20
        elif 100 >= distance(new_guess, rand_point) <= 200:
            if is_testing:
                #print("Distance is:", distance(new_guess, rand_point))
                distance_text.draw(win)
            #print("Not bad!")
            guess_text.setFill("peru")
        # If distance between points is more or equal to 20 and less than
        # or equal to 30
        elif 200 >= distance(new_guess, rand_point) <= 300:
            if is_testing:
                #print("Distance is:", distance(user_guess, rand_point))
                distance_text.draw(win)
            #print("So-so!")
            guess_text.setFill("gold")
        # If distance between points is more or equal to 30 and less than
        # or equal to 40
        elif 300 >= distance(new_guess, rand_point) <= 400:
            if is_testing:
                #print("Distance is:", distance(new_guess, rand_point))
                distance_text.draw(win)
            #print("Really far away!")
            guess_text.setFill("deep sky blue")
        # If distance between points is more or equal to 40 and less than
        # or equal to 50
        else:
            if is_testing:
                #print("Distance is:", distance(new_guess, rand_point))
                distance_text.draw(win)
            #print("You're way off!")
            guess_text.setFill("navy")

    win.getMouse()
    win.close()


main()
# end of program file

""" 
DESIGN

while test input is not y, Y, n, N, or '':
    prompt user again
        
while difficulty int is less than 1 or greater than 25:
    print invalid message
    prompt user again

while distance from rand, guess points is greater than difficulty:
    if distance from rand, guess points is less than difficulty:
        print success
    elif distance from rand, guess points is less than 10:
        print message
    elif distance from rand, guess points is greater than 10 and less than 20:
        print message
    elif distance from rand, guess points is greater than 20 and less than 30:
        print message
    elif distance from rand, guess points is greater than 30 and less than 40:
        print message
    else:
        print far away message
"""

"""
TEST CASES

1. User makes minimum number of guesses possible:
    Give me a guess (x and y between 1 and 50)
    x? 37
    y? 35

    You found him!
    Yay!!
    It took you 1 tries
    
2. User guesses and misses animal one time (testing loop executing one time):
    Give me a guess (x and y between 1 and 50)
    x? 50
    y? 50
    Distance is: 20
    So-so!

    Give me a guess (x and y between 1 and 50)
    x? 33
    y? 38

    You found him!
    Yay!!
    It took you 2 tries
    
3. User guesses and misses animal more than one time (testing loop executing more than one time):
    Give me a guess (x and y between 1 and 50)
    x? 50
    y? 50
    Distance is: 47
    You're way off!
    
    Give me a guess (x and y between 1 and 50)
    x? 40
    y? 40
    Distance is: 35
    You're way off!
    
    Give me a guess (x and y between 1 and 50)
    x? 6
    y? 31
    
    You found him!
    Yay!!
    It took you 3 tries
    
4. Test for distance = 0:
    Find the Invisible Cat!
    Testing mode? (y/n) y
    
    27 4
    Difficulty? (smaller is harder) 1
    
    Give me a guess (x and y between 1 and 50)
    x? 27
    y? 4
    
    You found him!
    Yay!!
    It took you 1 tries
    
5. Normal test for distance:
    Find the Invisible Cat!
    Testing mode? (y/n) y
    
    26 50
    Difficulty? (smaller is harder) 1
    
    Give me a guess (x and y between 1 and 50)
    x? 26
    y? 45
    Distance is: 5
    Not bad!
    
6. Take the default value for difficulty:
    Difficulty? (smaller is harder) 
    
    Give me a guess (x and y between 1 and 50)
    x? 8
    y? 43
    Distance is: 6
    Not bad!
    
    Give me a guess (x and y between 1 and 50)
    x? 8
    y? 42
    
    You found him!
    Yay!!
    It took you 2 tries
    
7. Wants a different value for difficulty (7):
    Difficulty? (smaller is harder) 7
    
    Give me a guess (x and y between 1 and 50)
    x? 2
    y? 27
    Distance is: 8
    Not bad!
    
    Give me a guess (x and y between 1 and 50)
    x? 2
    y? 26
    
    You found him!
    Yay!!
    It took you 2 tries
    
8. Low boundary input for difficulty (1):
    Difficulty? (smaller is harder) 1
    
    Give me a guess (x and y between 1 and 50)
    x? 6
    y? 43
    Distance is: 2
    Not bad!
    
    Give me a guess (x and y between 1 and 50)
    x? 6
    y? 42
    
    You found him!
    Yay!!
    It took you 2 tries
    
9. High boundary input for difficulty (25):
    Difficulty? (smaller is harder) 25
    
    Give me a guess (x and y between 1 and 50)
    x? 45
    y? 45
    
    You found him!
    Yay!!
    It took you 1 tries
    
10. Invalid input, too low for difficulty (0):
    Find the Invisible Cat!
    Testing mode? (y/n) y
    
    4 27
    Difficulty? (smaller is harder) 0
    Invalid difficulty, 1-25 allowed
    Difficulty? (smaller is harder) 5
    
    Give me a guess (x and y between 1 and 50)
    x? 
    
11. Invalid input, too high	for difficulty (1200):
    Find the Invisible Cat!
    Testing mode? (y/n) y
    
    23 7
    Difficulty? (smaller is harder) 1200
    Invalid difficulty, 1-25 allowed
    Difficulty? (smaller is harder) 5
    
    Give me a guess (x and y between 1 and 50)
    x? 
    
12. Take the default for test mode:
    Find the Invisible Cat!
    Testing mode? (y/n) 
    
    Difficulty? (smaller is harder) 
    
13. Wants normal mode for test mode (N):
    Find the Invisible Cat!
    Testing mode? (y/n) N
    
    Difficulty? (smaller is harder) 
    
14. Wants normal mode for test mode (n):
    Find the Invisible Cat!
    Testing mode? (y/n) n
    
    Difficulty? (smaller is harder)
    
15. Wants test mode	(y):
    Find the Invisible Cat!
    Testing mode? (y/n) y
    
    19 40
    Difficulty? (smaller is harder) 
    
16. Wants test mode	(Y):
    Find the Invisible Cat!
    Testing mode? (y/n) Y
    
    26 37
    Difficulty? (smaller is harder) 
    
17. Invalid input for test mode:
    Find the Invisible Cat!
    Testing mode? (y/n) 4
    Testing mode? (y/n) 5
    Testing mode? (y/n) y
    
    27 3
    Difficulty? (smaller is harder) 
"""
