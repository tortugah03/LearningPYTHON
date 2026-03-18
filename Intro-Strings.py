import math  # importing the math module to use its functions

print("hello Danilito 👽")
print("*" * 10)

print("hello")
print(2 + 3)

x = 1
y = 2
unit_price = 3

Students_Count = 1000
print(x + y + unit_price + Students_Count, " = Student count")
# Variables
# An expression is a piece of code that produces a value
# A variable is a named location used to store data in the memory
# You can use variables to store values and later retrieve them using the variable name
price = 29  # Integer
rating = 4.99  # FLoating
is_published = False  # Boolean
course_name = "Python Programming"  # String

################################################
course = "python's course for beginners"
message = """
hi Danilo,

This is Your future and you are doing great!
"""
print(course)
print(message)
###############################################
# to get the lenght of a string
# len()  # function
print(len(course))

print(course[0])  # first character
print(course[-1])  # last character
print(course[0:3])  # slicing, returns the first 3 characters
print(course[0:])  # returns all characters from index 0 to the end
print(course[:3])  # returns the first 3 characters
print(course[:])  # returns the entire string
###############################################
# adding double quotes inside a string
# using escape character and scape sequences \"
# \'
# \\
# \n  # new line
# \t  # tab

quote = 'She said, "Hello!"'
print(quote)
quote2 = "It's \"a beautiful day!\""
print(quote2)
###############################################

first = "DANi"
last = "LITO"
# full = first + " " + last  # concatenation

full = f"{len(first)} {last}"
# formatted string also for the last name you can use any expression like {2+2}

print(full)

# 48:48 (git example)
# now we are you g to look at "." that brings up functions or methods
# course.upper()  method that converts the string to uppercase
# course.lower()  method that converts the string to lowercase

print(course.upper())
print(course.lower())
# method that converts the first letter of each word to uppercase
print(course.title())
# method that removes whitespace from the beginning and end of the string
print(course.strip())
# you can also use .lstrip() and.rstrip() to remove whitespace from the left or right side of the string respectively
# method that returns the index of the first occurrence of the specified value
print(course.find("y"))
# if there is no match, it returns -1
print(course.find("z"))

print("\n")

# method that replaces a specified value with another value
print(course.replace("beginners", "absolute beginners"))

# method that checks if a specified value is present in the string, returns True or False
# boolean expression that checks if "python" is in the course string, returns True or False
print("python" in course)
print("Python" in course)  # case sensitive

# method that checks if a specified value is not present in the string, returns True or False
print("swift" not in course)
