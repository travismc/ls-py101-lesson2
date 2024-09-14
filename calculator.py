# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.

import json


def prompt(message):
    print(f"==> {message}")


def invalid_number(num_str):
    try:
        float(num_str)
    except ValueError:
        return True
    return False


def messages(message, lang="en"):
    return MESSAGES[lang][message]


with open("calculator_messages.json", "r") as file:
    MESSAGES = json.load(file)


exit = False
answer = "n"


while exit is False:
    prompt(messages("welcome"))

    prompt(messages("number_prompt_1"))
    num1 = input()

    while invalid_number(num1):
        prompt(messages("invalid_number"))
        num1 = input()

    prompt(messages("number_prompt_2"))
    num2 = input()

    while invalid_number(num2):
        prompt(messages("invalid_number"))
        num2 = input()

    prompt(f"You entered {num1} and {num2}.")

    prompt(messages("operation_prompt"))
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(messages("invalid_operation"))
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
