# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.


print("Welcome to Calculator")

num1 = int(input("What's the first number? "))
num2 = int(input("What's the second number? "))

print(f"You entered {num1} and {num2}.")

operation = input(
    "What operation do you want to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide: "
)

if operation == "1":
    answer = num1 + num2
elif operation == "2":
    answer = num1 - num2
elif operation == "3":
    answer = num1 * num2
elif operation == "4":
    if num2 == 0:
        answer = "You cannot divide by zero."
    else:
        answer = num1 / num2
else:
    answer = "Input error"

print(f"The result is: {answer}")
