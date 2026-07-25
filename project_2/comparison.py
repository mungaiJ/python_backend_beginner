"""3. Number Comparison Tool Input two numbers.Print which one is larger, or if they’re equal."""
# Ask the user to enter the first number and convert it to an integer
user_number = int(input('Enter first number:'))

# Ask the user to enter the second number and convert it to an integer
user_number2 = int(input('Enter second number:'))

# Check if the first number is greater than the second
if user_number > user_number2:
    # If true, print that the first number is greater
    print(f'{user_number} is greater than {user_number2}')

# If the first condition is false, check if the second number is greater
elif user_number2 > user_number:
    # If true, print that the second number is greater
    print(f'{user_number2} is greater than {user_number}')

# If neither condition is true, the numbers must be equal
else:
    # Print that both numbers are equal
    print(f'{user_number} is equal to {user_number2}')