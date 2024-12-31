#type of list
empty_list =[] 
list_fruits=["Apple", "banana", "orange"]
print (list_fruits)

list_fruits[0]="Mango"
print(list_fruits)

print(list_fruits[-1])

list_marks=[1,2,3,4]
print(list_marks)

#append
list_fruits.append("Kiwi")
print(list_fruits)

#insert
list_fruits.insert(1,"gauva")
print(list_fruits)

#remove
list_fruits.remove("Kiwi")
print(list_fruits)

#loop
for fruits in list_fruits:
   print(fruits)

for i in range( len(list_fruits)) :
   print(f'{i} : {list_fruits[i]}')

#sort
list_fruits.sort()
print(list_fruits)

#reverse
list_fruits.reverse()
print(list_fruits)

#index
list_fruits.index('Mango')
print(list_fruits)

