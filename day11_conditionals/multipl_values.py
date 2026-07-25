is_citizen = True
age = 16

if is_citizen:
    if age >= 18:
        print('You are eligible to vote') # You are eligible to vote
    else:
        print(bool(('You are still children')))
else:
    print('You are not eligible to vote')
