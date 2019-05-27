# Introduction / Crash Course to Python

# This is a comment

# This is how you print a string. The print function automatically adds a newline
print("Hello World!")

# Initializing and assigning variables
x = 1

# This is how you print a variable
print(x)

# If statement
if x == 1:
    print("X is 1")

# Python is completely object oriented, and not "statically typed".
# You do not need to declare variables before using them, or declare their type.
# Every variable in Python is an object.

string1 = "yes"
string2 = "no"
i_am_a_number = False # Take note that boolean values such as True and False need to be capitalized
potato = 6

# You can even initialize and assign variables simultaneously
a, b = 1, 2

# Adding integer-valued variables
c = a + b + potato*2
print(c)

# Adding string-valued variables
print(string1 + " " + string2)

# In Python, they use Lists instead of arrays, but the two of them are REALLY SIMILAR in terms of their functionalites
my_list = [1,2,3]
my_list.append(4) # appends at the tail of the list
print(my_list) # prints entire list

# Python lists are 0-indexed
# Separate different-valued variables by a string in order to be printed together on the same line
print("I am the 1st element:", my_list[1]) # prints the 1st element (2nd techincally) which is 2

# A for-loop that prints each element of the list in a newline. For-loops are 0-indexed
for y in my_list:
    print(y)

# In Python, in order to use the power function, use two multiplication symbols
power = 3**2
print(power)

# Python also supports multiplying strings (for some reason?) LOL
print(string1*3)

# I mean you could just do a for loop still no? This one runs a loop of 3 iterations but prints in all in a newline
for i in range(3):
    print(string1, end=" ") # this cancels the newline much amaze

print()
my_list2 = ["chicken", "nuggets"]
new_list = my_list + my_list2 # you can append lists together in a new variable like this
print()
print(new_list)
my_list2.append(my_list[2])
print(my_list2 * 3) # you can also multiply list to repeat a certain amount og times now it's a list with 9 elements (8 indexes)

# EXERCISE SOLUTION IN LIST COUNTING
yee = object() # can initialize as objects
haba = object()

# TODO: change this code
x_list = [2, yee] * 11
y_list = [haba] * 10
big_list = x_list + y_list

# Another way of printing strings and variables together (similar to C) - PROPER WAY OK
print("\nx_list contains %d objects" % len(x_list)) # this counts how elements there are in list
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# Testing code
if x_list.count(2) >= 10 and y_list.count(haba) == 10: # counts how many occurences of the yee object there is in the list
    print("Almost there...")
if big_list.count(yee) >= 10 and big_list.count(haba) == 10:
    print("Great!")
print()

name = "Wesley"
age = 20
print("%s is %d years old" % (name, age)) # use a tuple if you hgve two or more argument specifiers

print(len(name)) # this prints length of a string
print(name.index('e')) # this prints the index location the first occurence of that letter
print(name.count('e')) # this prints how many occurences of that letter appears within the string

astring = "Hello world!"
print(astring[3:8]) # this prints characters from 3rd index to 7th index
print(astring[::-1]) # this prints the string in reverse
print(astring.upper()) # this prints the string in uppercase
print(astring.lower()) # this prints the string in lowercase
print(astring.startswith("Hello")) # this prints true if the string does starts with this string or character
print(astring.endswith("asdfasdfasdf")) # this prints true if the string does end with this string or character

x = 2
print()
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True

print()
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Wesley":
    print("Your name is either John or Wesley.")

# In Python they have the in operation which checks if something is IN a list
if name in my_list:
    print("Yes that name is in the list")
else:
    print("nah man that isnt here\n")

# SIDE NOTE: Take account that the == and is operator are two different things
    # x = [1,2,3]
    # y = [1,2,3]
        # x == y --> True
        # x is y --> False

for i in range(5):
    print(i) # prints 0 to 4 because for loops are 0-indexed in Python

print("----")

for i in range(3, 8, 2):
    print(i) # prints out 3, 5, 7 because it takes every second element

print("----")

count = 0
while count < 5: # stops when count is 5
    print(count) # prints 0 to 4 (technically 5 elements)
    count = count + 1  # This is the same as count = count + 1

# This is how to define a function in Python
def my_function():
    print("I am a function :)")

# This is how to define a function with arguments in Python
def function_with_arguments(a, b):
    print("a is %d and b is %d" % (a,b))

# This is how to define a function with arguments and a return statement in Python
def function_with_return(a,b):
    return a + b

print()
my_function() # how to call a function
function_with_arguments(a, b)
sum = function_with_return(a,b)
print(sum)

# This is how to create a class in Python
class MyClass:
    name = "Boba"

    def function(self):
        print("Hi! this is a message inside the class :)")

# Initializing these Classes to variables
myObject = MyClass()
myObject2 = MyClass()
myObject2.name = "Drake" # changes the name for myObject2's myClass name variable

print("\n%s" % myObject.name)
print(myObject2.name)

myObject.function()

# A dictionary is a data type similar to arrays, but works with keys and values instead
dictionary = {}
dictionary["John"] = 123456
dictionary["Mary"] = 224466
dictionary["Klay"] = 999999
print()
print(dictionary)

# can also be initialized as :
    # dictionary {
        # "John" : 123456
        # "Mary" : 224466
        # "Klay" : 999999
    # }

# Iterating over entire dictionary
for name, number in dictionary.items():
    print("Phone number of %s is %d" % (name, number))

# To delete a specified index in the dictionary
del dictionary["Mary"] # or dictionary.pop("Mary")
print(dictionary)

# You define your own main function
