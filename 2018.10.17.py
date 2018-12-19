# Write a program that takes a sentence and outputs the number of letters
# and numbers
# EX: 'hello world! 123'
# letters: 10
# numbers: 3

s = input('Enter a sentence:\n')

letters = 0
numbers = 0

for x in s:
    if x.isdigit():
        numbers += 1
    elif x.isalpha():
        letters += 1
    else:
        continue

print('\nLetters: ')
print(letters)
print('\nNumbers: ')
print(numbers)





## ORIGINAL ANSWER: KINDA WORKS

# sentence = 'hello world! 123'
#
# length = len(sentence)
# spaces = sentence.count(' ')
#
# digits = sum(x.isdigit() for x in sentence)
# print('\nThe number of digits is: ')
# print(digits)
#
# letters = length - digits - spaces
# print('The number of letters is: ')
# print(letters)
