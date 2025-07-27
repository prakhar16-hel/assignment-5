#Name: Prakhar Chaurasia
#Chprakhar1@gmail.com

# Task 1: Create a Dictionary of Student Marks

student_marks = {      # dict
    'Rohan': 82,
    'Morgan': 95,
    'Ram': 79,
    'Chandan': 90
}

student_name = input("Enter the student's name: ")

if student_name in student_marks:
    marks = student_marks[student_name]   # allow to show the marks of requested student
    print(f"{student_name}'s marks: {marks}")   # show the marks of the student   which is requested
else:
    print("Student not found.")     # when we enter a name of student which is not in data