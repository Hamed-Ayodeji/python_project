# Operator Functions
def division(a, b):
    return a / b

def multiplication(a, b):
    return a * b

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

# Prompt for input
while True:
    user_input = input("Enter the numbers to be calculated (e.g., 1 + 2) or 'exit' to quit:\n")
    # Exit Mechanism
    if user_input.lower() == 'exit':
        break

    try:
        values = user_input.strip().split()
        # Check is input parameter follow the required format
        if len(values) != 3:
            print("Invalid input, use format: number operator number (e.g., 1 + 2)")
            continue

        value_a = float(values[0])
        value_b = float(values[2])
        operation = values[1]

        if operation == "/":
            result = division(value_a, value_b)
        elif operation == "*":
            result = multiplication(value_a, value_b)
        elif operation == "+":
            result = addition(value_a, value_b)
        elif operation == "-":
            result = subtraction(value_a, value_b)
        else:
            print("Invalid operation. Use /, *, +, -, or type 'exit' to quit")
            continue

        print(f"{value_a} {operation} {value_b} = {round(result, 2)}")

    except ValueError:
        print("Ensure both values are numbers separated by spaces")
    except ZeroDivisionError:
        print("Can't divide by zero")