"""2. Simple Grading System
Input a score (0–100).

Print grade: A, B, C, D, F using conditionals."""
user_score = int(input("What score did user get?"))

if user_score < 0 or user_score > 100:
    print('Inavalid score!!!')
elif user_score >= 80:
    print('A')
elif user_score >= 60:
    print('B')
elif user_score >= 40:
    print('C')
elif user_score >= 20:
    print('D')
else:
    print('F')

    """Special messages with boolean logic

Example: If average ≥ 90 and age < 18 → print “Young Genius!”.

Example: If average < 50 or total_score == 0 → print “Needs Serious Improvement”."""