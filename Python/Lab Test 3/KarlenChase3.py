# Author: Chase Karlen
# Email: chase@uky.edu
# Section: 002
def main():
    user_input = input("Press Enter to stop data entry\nEnter name, 3 test scores with commas: ")

    scores = []
    average = 0

    while user_input != "":
        user_split = user_input.split(",")
        grades = round((int(user_split[1]) + int(user_split[2]) + int(user_split[3])) / 3, 2)
        average += grades
        scores.append([user_split[0], grades])
        user_input = input("Enter name, 3 test scores with commas: ")

    print("\nAverage grade:", round(average / 3, 2), "\n")
    print("Student\t\tGrade\t\tPassing?\n")

    scores.sort()
    for i in range(len(scores)):
        if scores[i][1] >= 60:
            print(scores[i][0], "\t\t", scores[i][1], "\t\t", "yes")
        else:
            print(scores[i][0], "\t\t", scores[i][1], "\t\t", "no")


main()
