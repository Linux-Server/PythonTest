# Python variable have to be snake case
character_name ="Samray"
character_age = 30
is_male = True
print("There was s person name", character_name, "who got age of", character_age)

character_name ="Sachin"
print("Th name of the person is " + character_name)
# backslack to escape new char

print("Giraffe\"academy")

phrase = "Giraffe Academy"

print(phrase.lower())
print(phrase.upper())

print(phrase.isupper())
print(phrase.islower())

print(phrase.upper().isupper())
print(phrase.lower().islower())

# length of string
print(len(phrase))

# get the data out of index
print(phrase[0])

# to get the index number
print(phrase.index("ff"))

# replace
print(phrase.replace("Academy", "Class"))