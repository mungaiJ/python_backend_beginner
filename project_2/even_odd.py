"""Even or Odd Checker
Ask the user for a number.
Use % modulus and if/else to check if it’s even or odd."""

user_number = int(input('Enter any number of your choice:'))

if user_number % 2 == 0:
    print("This is an Even number")
else:
    print("This is an Odd number")