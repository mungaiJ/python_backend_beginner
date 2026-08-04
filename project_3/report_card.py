def student_details():
    student_name = str(input('Enter the name of the student: ').strip().title())
    student_age = int(input('Enter student\'s age: '))
    return(student_name,student_age)
print(student_details())

# english_score = int(input('Enter the score for English: '))
# comm_skill_score = int(input('Enter the score for Communication Skills: '))
# net_score = int(input('Enter the score for Networking: '))
# math_score = int(input('Enter the score for Maths: '))

# if not student_name:
#     print('Name required....')
# elif not student_name.isalpha():
#     print("Please enter a vaid name.")
# elif (english_score < 0 or english_score > 100 or
#     comm_skill_score < 0 or comm_skill_score > 100 or
#     net_score < 0 or net_score > 100 or
#     math_score < 0 or math_score > 100):
#     print("Invalid score. Please put the correct scores.")
# else:
#     total_score = english_score + comm_skill_score + net_score + math_score
#     average_score = total_score / 4

#     print(f'\nReport Card for {student_name} (Age: {student_age})')
#     print(f'English: {english_score}, Communication Skills: {comm_skill_score}, Networking: {net_score}, Maths: {math_score}')
#     print(f'Total Score: {total_score}')
#     print(f'Average Score: {round(average_score, 2)}')

#     if average_score >= 90 and student_age < 18:
#         grade = ("A")
#         message = 'Young and Genius'
#     elif average_score >= 80:
#         grade = ("B")
#         message = 'Excelent work, keep it up'
#     elif average_score >= 70 and average_score < 90:
#         grade = ("C")
#         message = 'Good job, keep pushing for excelence'
#     elif average_score >= 60:
#         grade = ("D")
#         message = "Fair effort. There's room for improvement."
#     elif average_score >= 50:
#         grade = ("E")
#         message = "You passed, but keep practising."
#     else:
#         grade = ("F")
#         message = "Don't give up. Keep studying and you'll improve."

#     print(f'{student_name} scored a grade of {grade}. {message}')