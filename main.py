# variable = container for a value. Behaves as that value that it contains
# Strings(Series of characters)

# Defining and concatenating strings
first_name = "Jeffrey"
last_name = "DevOps"
full_name = first_name + last_name
print("Hello " + full_name)

# int = integer
# Performing arithmetic operations on integers
age = 21
age -= 1
print("Your age is: " + str(age))

# float = floating point number(a decimal number)
# Converting string to float, printing type
height = "260.6"
print("Your height is: " + str(height) + "cm")
print(type(height))

# boolean = true or false
# Creating and printing a boolean variable
human = True
print("Are you human? " + str(human))
print(type(human))

# multiple assignment
# Demonstrating multiple assignment
name, age, attractive = "Jeffrey", 21, True
Jeffrey = Jessica = Janel = 30
print(Jeffrey)

# string methods
# Using various string methods
name = "Jeffrey DevOps"
print(len(name))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.find("J"))
print(name.isalpha())
print(name.isdigit())
print(name*8)

# type casting
# Converting variables between different types
x = 1  # int
y = 2.0  # float
z = "3"  # str
x = float(x)
y = int(y)
z = int(z)
print(x)
print(y)
print(z*3)

# How to accept user input
# Taking user input and printing the results
name = input("What is your name?: ")
age = input(str("How old are you?: "))
height = input(str("How tall are you?: "))
print("Hello " + name)
print("You are " + str(age) + " year old")
print("You are " + str(height) + " cm tall")

# slicing = create a substring by extracting elements from another string
# indexing [] or slicing ()
# [start:stop:step]
# Demonstrating string slicing
name = "Jeffrey Devops"
first_name = name[0:7]
last_name = name[8:14]
funky_name = name[::3]
print(first_name)
print(last_name)
print(funky_name)

# slicing
# Using slice objects for string slicing
website1 = "https://google.com"
website2 = "https://wikipedia.com"
website3 = "https://wwe.com"
slice = slice(8,-4)
print(website1[slice])
print(website2[slice])

# if statements , else , elif
# Checking age and printing messages accordingly
age = int(input("Enter your age: "))
if age == 100:
    print("You are an adult!")
elif age >= 18:
    print("Welcome to adulthood")
elif age == 0:
    print("You aren't born yet  ")
else:
    print("You're a kid")

height = float(input("How tall are you?: "))
if height == 7.5:
    print("You are way too tall!")
elif height >= 6.1:
    print("You are tall")
elif height < 6.0:
    print("You are short")
else :
    print("You are a dwarf")

# logical operators
# Checking weather conditions and giving recommendations
weather = int(input("Enter the weather condition: "))
if 0 <= weather <= 30:
    print("the weather is good")
    print("go outside")
else:
    print("the weather is bad don't go outside")

# while loops
# Using a while loop to get a non-empty name from the user
name = ""
while len(name) == 0:
    name = input("Enter your name: ")
print("Hello " + name)

password = ""

while len(password) < 5:
    password = (input("Enter a new password: "))
    if len(password) < 5:
        print("Enter a new password")

print("Successful! ")

# for loop
# Using for loops to iterate over ranges and strings
for i in range(10):
    print(i)
for i in range(50, 100 + 1, 2):
    print(i)
for i in "bro code":
    print(i)

import time
for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print("Happy new year ")

# nested loops
# Generating a grid of symbols based on user input
rows = int(input("How many rows?: "))
column = int(input("How many column?: "))
symbols = input("How many symbols?: ")
for i in range(rows):
    for j in range(column):
        print(symbols, end="")
    print()

# loop control statement
# Using a loop with a break statement to get a non-empty name
while True:
   name = input("Enter your name: ")
   if name != "":
       break

# Iterating over a string and skipping hyphens
phone_number = "123-456-789-0"
for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

# Using pass statement to do nothing when i equals 13
for i in range(1, 21):
   if i == 13:
        pass
   else:
        print(i)

# list = used to store multiple items in a single variable
# Modifying, adding, removing, and sorting elements in a list
food = ["EBA", "EGUSI", "FUFU", "RICE", "BREAD"]
food[0] = "BEANS"
food.append("BREAD")
food.remove("FUFU")
food.pop(2)
food.sort()
food.insert(3,"ICE CREAM")
for x in food:
   print(x)

# 2D LIST
# Creating a 2D list and accessing an element
solid_food = ["EBA", "FUFU", "AMALA"]
normal_food = ["RICE", "BEANS", "PASTA"]
snacks = ["ZOBO", "CHAPMAN",]
food = [solid_food, normal_food, snacks]
print(food[2][1])

# tuple
# Creating and manipulating a tuple
student = ("bro", 16, "female")
(student.count("bro"))
print(student.index("female"))
for x in student:
    print(x)
if "female" in student:
    print("Hey what's up")