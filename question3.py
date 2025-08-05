# Create an empty dictionary to store student names and their marks
student_marks = {}

# Input marks for 5 students
for i in range(5):
    student_name = input(f"Enter name of student {i+1}: ")
    marks = float(input(f"Enter marks for {student_name}: "))
    student_marks[student_name] = marks

# Display the marks of all 5 students
print("\nStudent Marks:")
for student, marks in student_marks.items():
    print(f"{student}: {marks}")
