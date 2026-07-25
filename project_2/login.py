"""Login Simulation
Store a username and password in variables.
Ask the user to input them.
Use conditionals to check if they match.
"""

username = "Gueverstarstone"
password = 87654321

user_con= input("Enter your username:")
password_con = int(input('Enter your password:'))

if username == user_con and password == password_con:
    print("Username and password matches")
else:
   print("Nothing matches")