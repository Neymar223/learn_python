try:
    file = open("hello.txt","r")
    print(file.read())
except FileNotFoundError :
    print("file not found")
except :
    print("something went wrong")
finally:
    file.close()

