# Author: Chase Karlen
# Email: chase@uky.edu
# Section: 002
"""
Purpose: To draw graphics using Zelle graphics
Pre-conditions: The input will be a string
Post-conditions: The outputs will be several Zelle graphics
"""
from graphics import *


def main():

    # Create graphic window
    window = GraphWin("Happy birthday!", 500, 600)

    # Show prompt text to enter name
    prompt = Text(Point(250, 50), "Please enter your name:")
    # Draw prompt
    prompt.draw(window)

    # Create input box
    input_box = Entry(Point(250, 100), 20)
    # Set text to blank
    input_box.setText("")
    # Draw input box
    input_box.draw(window)
    # Get mouse to advance
    window.getMouse()
    # Get input box name
    name = str(input_box.getText())

    # Un-draw prompt and input box
    prompt.undraw()
    input_box.undraw()

    # Show happy birthday text
    birthday = Text(Point(250, 60), "Happy birthday!")
    # Show name as inputted in input box
    print_name = Text(Point(250, 80), name)
    # Draw happy birthday text
    birthday.draw(window)
    # Draw name text
    print_name.draw(window)

    # Print click to close window text
    close_text = Text(Point(55, 10), "Click to close window")
    # Draw click to close text
    close_text.draw(window)

    # Define line1 for balloon1
    line1 = Line(Point(300, 300), Point(300, 500))
    # Draw line1
    line1.draw(window)

    # Define balloon1 circle
    balloon1 = Circle(Point(300, 250), 50)
    # Set circle to yellow
    balloon1.setFill("yellow")
    # Draw circle
    balloon1.draw(window)

    # Define line2 for balloon2
    line2 = Line(Point(100, 300), Point(100, 500))
    # Draw line2
    line2.draw(window)

    # Define balloon2 oval
    balloon2 = Oval(Point(150, 300), Point(50, 150))
    # Set oval to red
    balloon2.setFill("red")
    # Draw oval
    balloon2.draw(window)

    # Define rectangle
    rectangle = Rectangle(Point(150, 400), Point(250, 300))
    # Set rectangle to purple
    rectangle.setFill("purple")
    # Draw rectangle
    rectangle.draw(window)

    # Get mouse to interrupt program from exiting
    window.getMouse()
    # Close window
    window.close()


main()
# end of program file
