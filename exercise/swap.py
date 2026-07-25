# Create two variables, a = "Python" and b = "Flask". Swap their values without reassigning manually.
message_1 = 'Python' 
message_2 = 'Flask' 

message_3 = message_1 
message_1 = message_2
message_2 = message_3

print(message_1)
print(message_2)
print(message_1 + ' ' + message_2)

"""Mini challenge  
Write a program that asks the user for their name and favorite color, then prints:
"Hello [name], your favorite color is [color]!"""

user_name = input("Enter Your name:")
fav_color = input("What's your favourite color:")

speech = f'Hello, my name is {user_name} and my favourite color is {fav_color}'

print(speech)