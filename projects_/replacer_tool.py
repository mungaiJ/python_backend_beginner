"""String Replacer Tool
Input a sentence.
Replace one word with another using .replace()."""

my_sentence = input('Write down your sentence here:')
word_to_replace = input('Word to replace is:')
new_word = input('Enter the new word:')
new_sentence = my_sentence.replace(word_to_replace, new_word)

print(new_sentence)