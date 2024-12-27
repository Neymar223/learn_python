import random


number=random.randint(1, 10)
attempt = 0
while attempt <=3:
           user_guess=int(input("Guess the number between 1 to 10"))
           attempt +=1
           if user_guess >10 or user_guess <0:
            print("Please enter tbhe valid number")
           else:
             if(number==user_guess):
              print("Congrats you win !!!!!")
              break
             elif(user_guess<number):
              print("Your guess is low, Please Guess Higher Number")
             else:
              print("Your guess is higher, please Guess Lower")