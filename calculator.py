# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.


def prompt(message):
    print(f"==> {message}")


def invalid_number(num_str):
    try:
        float(num_str)
    except ValueError:
        return True
    return False


exit = False
answer = "n"

while exit is False:
    prompt("Welcome to Calculator!")

    prompt("What's the first number?")
    num1 = input()

    while invalid_number(num1):
        prompt("Hmm... that doesn't look like a valid number.")
        num1 = input()

    prompt("What's the second number?")
    num2 = input()

    while invalid_number(num2):
        prompt("Hmm... that doesn't look like a valid number.")
        num2 = input()

    prompt(f"You entered {num1} and {num2}.")

    prompt(
        """What operation do you want to perform?
    1) Add 2 Subtract 3) Multiply 4) Divide: """
    )
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt("You must choose 1, 2, 3, or 4")
        operation = input()

    # output = None

    match operation:
        case "1":
            output = float(num1) + float(num2)
        case "2":
            output = float(num1) - float(num2)
        case "3":
            output = float(num1) * float(num2)
        case "4":
            output = float(num1) / float(num2)

    if output is not None:
        prompt(f"The result is: {output}")
    else:
        prompt("Invalid operation selected.")

    prompt("Would you like to perform another calculation? (y/n) ")
    answer = input()

    if answer == "n":
        break
    else:
        continue
