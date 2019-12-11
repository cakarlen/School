from math import sqrt


def main():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    root1 = ((-b + (sqrt(b ** 2 - 4 * a * c))) / (2 * a))
    root2 = ((-b - (sqrt(b ** 2 - 4 * a * c))) / (2 * a))

    print("Root 1 is:", root1, "and root 2 is:", root2)


main()
