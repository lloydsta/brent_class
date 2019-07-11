# Given a string, create a dictionary that tells me, how many times
# a letter is used in that string


string = 'beer'
dictionary = {}

for x in string:
    if x in dictionary:
        dictionary[x] += 1
    else:
        dictionary[x] = 1

print(dictionary)