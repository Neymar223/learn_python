age=int(input("What is your age"))

if age>=18:
    print("You can vote")
else:
    print("Try again")
      
print("*" *100)

marks=int( input("Enter Your Exam marks?"))

if marks >=24:
    print("Pass")
else:
    print("fail")

print("*" *100)

grade = int(input("Enter Your Exam grade?"))

if grade >=90:
    print("A")
elif grade >=80:
    print("B+")
elif grade >=60:
    print("B")
else :
    print("You are fail")