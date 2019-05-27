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
