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

# A for-loop that prints each element of the list in a newline
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

name = "Wesley"
age = 20
print("%s is %d years old" % (name, age)) # use a tuple if you hgve two or more argument specifiers
