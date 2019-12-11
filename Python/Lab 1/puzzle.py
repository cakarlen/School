def main():
    input1 = int(input("First number: "))
    input2 = int(input("Second number: "))

    def division():
        return input1 / input2

    def addition():
        return input1 + input2

    def subtraction():
        return input1 - input2

    def multiplication():
        return input1 * input2

    def statements():
        if input2 == 0:
            print("Cannot divide by zero!\nRe-enter your numbers")
            return main()
        else:
            print("Sum:", addition())
            print("Difference:", subtraction())
            print("Ratio:", division())
            print("Multiplication:", multiplication())

    statements()


main()
