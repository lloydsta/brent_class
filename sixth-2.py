def calculate_grade(grade):
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
    return(grade_letter)

def getting_user_input():
    user_input_list = []
    for x in range(4):
        user_input_list.append(int(input("Enter a grade value (0-100): ")))
    return(user_input_list)


############################################################################################

four_grades_list = getting_user_input()



grade_list = []

for x in range(len(four_grades_list)):
    single_numerical_grade = four_grades_list[x]

    output_grade = calculate_grade(single_numerical_grade)

    grade_list.append(output_grade)

print(grade_list)
