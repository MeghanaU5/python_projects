def addition(num1, num2):
    result = num1 + num2
    print("{0} + {1} = {2}".format(num1, num2, result))

def subtraction(num1, num2):
    result = num1 - num2
    print("{0} - {1} = {2}".format(num1, num2, result))

def multiplication(num1, num2):
    result = num1 * num2
    print("{0} * {1} = {2}".format(num1, num2, result))

def division(num1, num2):
    if num2 == 0.0:
        print("Can't divide by zero")
    else:
        result = num1 / num2
        print("{0} / {1} = {2}".format(num1, num2, result))

while True:
    print("Choose any option:")
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Division")
    print("Press Q key to exit")

    choice = input("Enter your choice: ")

    if choice == 'q' or choice == 'Q':
        break

    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))

    if choice == '1':
        addition(num1, num2)
    elif choice == '2':
        subtraction(num1, num2)
    elif choice == '3':
        multiplication(num1, num2)
    elif choice == '4':
        division(num1, num2)
    else:
        print("Invalid choice")
