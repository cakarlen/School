# Author: Chase Karlen
# Email: chase@uky.edu
# Section: 002
from graphics import *
from math import sqrt


def distance(point1, point2):
    # all four parameters are integers
    # they represent the coordinates of two points
    # the distance between the two points is returned
    return float(sqrt((point2.getX() - point1.getX()) ** 2
                      + (point2.getY() - point1.getY()) ** 2))


def main():
    win = GraphWin("Lab Test 2", 450, 550)

    counter = 0

    click_text = Text(Point(225, 10), "Click 6 times")

    close_text = Text(Point(220, 535), "Click to close")
    click_text.draw(win)

    for i in range(3):
        first_click = win.getMouse()
        second_click = win.getMouse()
        actual_distance = distance(first_click, second_click)

        click_rectangle = Rectangle(Point(first_click.getX(), first_click.getY()),
                                    Point(second_click.getX(), second_click.getY()))
        click_rectangle.draw(win)

        dist_line = Line(Point(first_click.getX(), first_click.getY()),
                         Point(second_click.getX(), second_click.getY()))
        dist_line.draw(win)

        if actual_distance > 250:
            click_rectangle.setFill("blue")
        else:
            click_rectangle.setFill("green")

        counter = actual_distance + counter

    distance_point = "Total distance", round(counter, 1)
    distance_text = Text(Point(220, 520), distance_point)

    click_text.undraw()
    distance_text.draw(win)
    close_text.draw(win)

    win.getMouse()
    win.close()


main()
