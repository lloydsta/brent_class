
count = 0
limit = 4
user_input = []

for x in range(limit):
    user_input.append(int(input("Enter a grade value (0-100): ")))


grade_list = []

for x in range(len(user_input)):
    grade = user_input[x]
    if(grade <= 100 and grade >= 90):
        grade_letter = "A"
    elif(grade <= 89 and grade >= 80):
        grade_letter = "B"
    elif(grade <= 79 and grade >= 70):
        grade_letter = "C"
    elif(grade <= 69 and grade >= 60):
        grade_letter = "D"
    elif(grade <= 59 and grade >= 0):
        grade_letter = "F"
    grade_list.append(grade_letter)


print(grade_list)
