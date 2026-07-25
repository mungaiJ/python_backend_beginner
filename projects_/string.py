"""String Analyzer
Input a sentence.
Print it in uppercase, lowercase, and title case.
Count how many characters and words it has."""

my_sentence = input('Write your sentence:')


print('This is my sentence in uppercase:', my_sentence.upper())
print('This is my sentence in lowercase:', my_sentence.lower())
print('This is my sentence in title case:', my_sentence.title())
print(len(my_sentence))
print(len(my_sentence.split()))