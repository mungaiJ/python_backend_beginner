"""Write a program that:
Asks the user for a sentence.
Prints it in uppercase, lowercase, and title case.
Splits the sentence into words and prints the list.
Replaces one chosen word with another."""

user_sentence = input('Enter your sentence:')
print(user_sentence.upper())
print(user_sentence.title())
print(user_sentence.split())
sentence = input('Enter the word you want to replce:')
sentence2 = input('Enter new word:')

print('New sentence:', user_sentence.replace(sentence, sentence2))