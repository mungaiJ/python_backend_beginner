"""Simple Calculator
Ask the user for two numbers.
Perform addition, subtraction, multiplication, division.
Show results neatly formatted."""

number_1 = int(input("Enter first number:"))
number_2 = int(input("Enter second number:"))

maths_calc = number_1 /  number_2
addition = number_1 + number_2
multiplication = number_1 * number_2
subtration = number_1 - number_2

print('Answer after division is:' ,maths_calc)
print('Answer after addition is:' ,addition)
print('Answer after multiplying is:' ,multiplication)
print('Answer after subtracting is:' ,subtration)