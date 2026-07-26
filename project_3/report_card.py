student_name = input('Enter the score for the name of the student: ').title()
student_age = int(input('Enter student\'s age: '))

english_score = int(input('Enter the score for English: '))
comm_skill_score = int(input('Enter the score for Communication Skills: '))
net_score = int(input('Enter the score for Networking: '))
math_score = int(input('Enter the score for Maths: '))

if not student_name:
    print('Name required....')

if (english_score < 0 or english_score > 100 or
    comm_skill_score < 0 or comm_skill_score > 100 or
    net_score < 0 or net_score > 100 or
    math_score < 0 or math_score > 100):
    print("Invalid score. Please put the correct scores.")
else:
    total_score = english_score + comm_skill_score + net_score + math_score
    average_score = total_score / 4

    print(f'\nReport Card for {student_name} (Age: {student_age}')
    print(f'English: {english_score}, Communication Skills: {comm_skill_score}, Networking: {net_score}, Maths: {math_score}')
    print(f'Total Score: {total_score}')
    print(f'Average Score: {round(average_score, 2)}')
    
    if average_score >= 90:
        print("A")
    elif average_score >= 80:
        print('B')
    elif average_score >= 70:
        print('C')
    elif average_score >= 60:
        print('D')
    elif average_score >= 50:
        print('E')
    else:
        print('F')

print(f'{student_name} scored an average score of {average_score}: ')