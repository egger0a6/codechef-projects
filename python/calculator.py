def calculatorDisplay():
    display = "Welcome to Calculator\n\nChoose one operation:\n1. Add\n2. Subtract\n3. Exit\n"

    return(display)


def calculatorFunction(user_choice):
    if user_choice == 1:
        print("Let's perform addition")
        a, b = user_input()
        output = addition(a, b)
        return f"The sum is: {output}\n"
    elif user_choice == 2:
        print("Let's perform subtraction")
        a, b = user_input()
        output = subtraction(a, b)
        return f"The difference is: {output}\n"
    else:
        return("Exiting the calculator.")


def user_input():
    print("Give two numbers on two lines")
    a = int(input("Number 1 is: "))
    b = int(input("Number 2 is: "))

    return a, b


def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b


if __name__ == '__main__':
    while True:
        print(calculatorDisplay())
        user_choice = int(input("Select the operation: "))
        value = calculatorFunction(user_choice)
        print(value)
        if value == "Exiting the calculator.":
            break