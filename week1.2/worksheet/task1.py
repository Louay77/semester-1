# Worksheet 1.2: Task 1 Solution
import sys
grade = input("enter your grade:")
if grade.isdecimal() == True:
    grade= int(grade)
    if grade > 100 or grade < 0:
        sys.exit("Error: Grade must be an integer between 0 and 100")
    elif grade >= 70 :
        print(f"{grade} is a Distinction")
    elif grade < 70 and grade > 39 :
        print(f"{grade} is a Pass")
    elif grade <= 39:
        print(f"{grade} is a Fail")
else:
    sys.exit("Error: Grade must be an integer between 0 and 100")
