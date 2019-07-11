# Write a program where you can do the following to pre-set tuples:
#   1. Sort by name
#   2. Sort by age
#   3. Sort by score

# Name, Age, Score
tom = ('Tom', 19, 80)
john = ('John', 20, 90)
jony1 = ('Jony', 17, 93)
jony2 = ('Jony', 17, 91)
json = ('Json', 21, 85)

tuple_list = [tom, john, jony1, jony2, json]

def run():
    sort_input = input('How do you want to sort each tuple?\n'
    '1. Sort by name\n'
    '2. Sort by age\n'
    '3. Sort by score\n'
    '\nChoose a number: ')

    if sort_input == '1':
        sort_by_name()
    if sort_input == '2':
        sort_by_age()
    if sort_input == '3':
        sort_by_score()

def sort_by_name():
    name_list = [tom[0], john[0], jony1[0], jony2[0], json[0]]
    name_sorted = name_list.sort()
    print(name_list)

def sort_by_age():
    age_list = [tom[1], john[1], jony1[1], jony2[1], json[1]]
    age_sorted = age_list.sort()
    print(age_list)

def sort_by_score():
    score_list = [tom[2], john[2], jony1[2], jony2[2], json[2]]
    score_sorted = score_list.sort()
    print(score_list)


run()

