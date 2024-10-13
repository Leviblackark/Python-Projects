from art import logo


# TODO: Write out the other 4 functions - subtract, multiply and divide.
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    """Perform division and re-prompt for another number if n2 is zero."""
    while n2 == 0:
        print("Error: Division by zero is not allowed")
        n2 = int(input("Whats the next number?: "))

    return n1 / n2


# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
calculation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# TODO: Create function that returns and output when the operator is not Typed


def get_operator():
    """Function to prompt user for a valid operator"""
    print("+\n-\n*\n/")
    operator = input("Pick an operation: ")

    #  Keep rotating the question if keyword not present
    while operator not in calculation:
        print("Invalid operator! Please choose from:\n+\n-\n*\n/")
        operator = input("Pick an operation: ")
    return operator


# TODO: Ask user to type First number, Operator, Second number
continue_calculation = True
# cal_result = 0

while continue_calculation:
    # Reset additional_calculation for each new calculation session
    additional_calculation = True
    print(logo)

    # Ask for the first number, operator, second number
    first_number = int(input("Whats the first number?: "))
    operator_ = get_operator()
    second_number = int(input("Whats the next number?: "))

    # TODO: Calculate the result based on the chosen operator
    # print(calculation[operator](n1=first_number, n2=second_number)
    result = calculation[operator_](n1=first_number, n2=second_number)
    print(f"{first_number} {operator_} {second_number} = {result}")

    # TODO: Check if user wants to continue working with the previous result
    while additional_calculation:
        continue_cal = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new "
                             f"calculation: ").lower()

        if continue_cal == "y":
            operator_ = get_operator()
            next_number = int(input("Whats the next number?: "))

            new_result = calculation[operator_](n1=result, n2=next_number)
            print(f"{result} {operator_} {next_number} = {new_result}")
            # overwrites result with new_result so when the comes back round it always uses the new amount
            result = new_result

        if continue_cal == "n":
            additional_calculation = False
            print("\n" * 100)
