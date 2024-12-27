#student info
name = input("Enter the student Name")
student_class = input("Enter the Class")

#get Marks

mark1 = int(input("Enter the marks for Subject1"))
mark2 = int(input("Enter the marks for Subject2"))
mark3 = int(input("Enter the marks for Subject3"))

#calculate Total & Average Marks
total_marks = mark1 + mark2 + mark3
average_marks = total_marks/3

#Result

print("=== Student Report ===")
print(f"Name={name}")
print(f"Class={student_class}")
print(f"Total Marks={total_marks}")
print(f"Average marks={average_marks}")