print("-------------------- Welcome to the CALCULATOR APPLICATION --------------------")
print("")
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))


while True:
    print("")
    print("                                  Operations                                   ")
    print("                                  Enter 'Add' for Addition                                   ")
    print("                                  Enter 'Subtract' for Subtraction                                   ")
    print("                                  Enter 'Multiply' for Multiplication                                   ")
    print("                                  Enter 'Divide' for Division                                   ")
    print("                                  Enter 'Exit' to exit the program             ")
    print("")

    operator = input("Choose the operator you want to use:")

    if operator == 'Add':
        print("Result:",num1+num2)

    elif operator == 'Subtract':
        print("Result:",num1-num2)

    elif operator == 'Multiply':
        print("Result:",num1*num2)

    elif operator == 'Divide':
        print("Result:",num1/num2)

    elif operator == 'Exit':
        print("Thankyou for using the Calculator Application")
        break

    else:
        print("Invalid input")
