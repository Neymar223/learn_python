file= open("hello.txt","r")

print (file.readline()) #readline #readlines



file.close()

#write

file= open("hello.txt","w")

print (file.write("Hello hello"))

file.close


#append
file= open("hello.txt","a")

print (file.write("Hello hello"))

file.close




