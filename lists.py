friends = ["Kevin", "Kiran", "Sam"]
print(friends)
print(friends[0])
# to acces last element in list
print(friends[-1])

# to access list element using range operatoe

print(friends[0:3])
print(friends[1:])

# modify a list
friends[0] ="Sachin"
print(friends)

#List Functions

list_one = ["Sam", "Ram", "Nick"]
list_two = [1,2,3,4,5]

# adding one list to another (extend)
list_one.extend(list_two)
print(list_one)

# adding one item to end of the list (append)
list_one.append("Sachin")
print(list_one)

# adding item to the middle of list (insert)
list_one.insert(2,"Ray")
print(list_one)


# remove element from list
list_one.remove(1)
list_one.remove("Ray")
print(list_one)

# poping out last elemnt from the list
list_one.pop()
print(list_one)


# to get index of a specific element in a lsit

print(list_one.index("Sam"))

list_one.append("Sam")

print(list_one)

print(list_one.count("Sam"))
print(list_two)
list_two.sort()
list_two.reverse()
print(list_two)