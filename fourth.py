grade = int(input("Enter a grade value (0-100): "))
#print(type(grade))

#if(grade == type(string)):
#    grade_output = "You entered text, please enter a number"

if(grade > 100 or grade < 0):
    grade_output = "Please input a valid number"

if(grade <= 100 and grade >= 90):
    grade_output = "A"
elif(grade <= 89 and grade >= 80):
    grade_output = "B"
elif(grade <= 79 and grade >= 70):
    grade_output = "C"
elif(grade <= 69 and grade >= 60):
    grade_output = "D"
elif(grade <= 59 and grade >= 0):
    grade_output = "F"
#else:

print("Your grade is: " + grade_output)
