# Create an empty dictionary to store student names and their marks
student_marks = {}

# Input names and marks for 5 students
for i in range(5):
    student_name = input(f"Enter name of student {i+1}: ")
    marks = float(input(f"Enter marks for {student_name}: "))
    student_marks[student_name] = marks

# Find the topper (student with the highest marks)
topper = max(student_marks, key=student_marks.get)

# Display the topper's name
print(f"\nTopper: {topper} with {student_marks[topper]} marks")
