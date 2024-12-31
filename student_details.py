students= []

student1={
    "name":"boom","age":15,  "major":"computer",
}
student2={
    "name":"joom","age":15,  "major":"maths",
}
student3={
    "name":"doom","age":15,  "major":"english",
}

students.append(student1)
students.append(student2)

for student in students:
  print(f"Name:{student["name"]} age:{student["age"]} major{student["major"]}")