def calculatorDisplay():
    display = "Welcome to Calculator\n\nChoose one operation:\n1. Add\n2. Subtract\n3. Multiplication\n4. Division\n5. Exit\n"

    return(display)


def calculatorFunction(user_choice):
    if user_choice == 1:
        print("Let's perform addition")
        a, b = user_input()
        output = addition(a, b)
        return f"The sum is: {output:.2f}\n"
    elif user_choice == 2:
        print("Let's perform subtraction")
        a, b = user_input()
        output = subtraction(a, b)
        return f"The difference is: {output:.2f}\n"
    elif user_choice == 3:
        print("Let's perform multiplication")
        a, b = user_input()
        output = multiplication(a, b)
        return f"The product is: {output:.2f}\n"
    elif user_choice == 4:
        print("Let's perform division")
        a, b = user_input()
        output = division(a, b)
        if output:
          return f"The quotient is: {output:.2f}\n"
        return None
    elif user_choice == 5:
        return("Exiting the calculator.")
    else:
        return("Operation does not exist - please provide the correct input.")


def user_input():
    print("Give two numbers on two lines")

    while True:
        try:
            a = float(input("Number 1 is: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for Number 1.")
    
    while True:
        try:
            b = float(input("Number 2 is: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for Number 2.")

    return a, b


def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None


if __name__ == '__main__':
    while True:
        print(calculatorDisplay())
        user_choice = int(input("Select the operation: "))
        value = calculatorFunction(user_choice)
        print(value)
        if value == "Exiting the calculator.":
            break