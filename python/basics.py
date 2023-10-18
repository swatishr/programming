

# Python is an interpreted language. no compiling and linking, so saves a lot of time during development
# short and concise programs because of high-level data types.
# 
# The interpreter operates somewhat like the Unix shell: 
# when called with standard input connected to a tty device, it reads and executes commands interactively;

# Argument Passing in Python: you can pass args while running a script, the arguments gets assigned to argv var from sys module.

# Source code encoding: By default, Python source files are treated as encoded in UTF-8. In that encoding, 
# characters of most languages in the world can be used simultaneously in string literals, 
# identifiers and comments — although the standard library only uses ASCII characters for identifiers



#---- Comments - start with # ----

#---- Numbers (integers, floats, complex) ----
# operators: +, -, *, / (always returns a floats), // (integer division), ** (power), () parantheses

print(5+5, 10-5, 10*5, 10/3, 10//3, 10%3, 10**3)


# In interactive mode, the last printed expression is assigned to the variable _. 
# So, you can use it while using python interpreter as a calculator

# Complex Numbers' imaginary part is indicated by j (not i like go): 3 + 2j



#---- Text ----
# Can be quoted with '' single or "" double quotes
# To escape quotes in the string itself, use escape character or wrap with another set of quotes


# While in interepreter, if you output a string wit special chars like \n, it will output with all those chars as is
#print() func interprets those chars and returns a prettified readable output.

print("This\nis\ninteresting")

print("C:\abcd\name") # If you noticed the output here, we wanted the string to be displayed as is, but it interprets them as \a and \n

#To avoid the above, use r i.e. raw in front of the string; 
# one subtle point with raw is that it needs even number of \ characters in the string else it will error out (https://docs.python.org/3/faq/programming.html#faq-programming-raw-string-backslash)
print(r"C:\abcd\name")
# or double \\. allows odd number of \
print("C:\\abcd\\name\\")


# To print a multi-line string, use triple quotes (single or double is fine)
print(""" \
Hello
      This is a multi-line
      string""") # the first \ prevents adding a newline character. Try removing it and see what happens.

# String concatenation can be done by simple + operator

print("a" + "b")
str1="New"
str2="York"
print(str1 + str2)

print(2 * "pa" + " and " + 2 * "ma") # you can repeat a string n number of times by multiplying the string with n

print('Put several strings within parentheses '
        'to have them joined together.') #concat works without + too, but only works with literals, not variables. Useful when you want to split a long string

# String indexing
# there are no character data types in Python, character is a string of size 1

str="NewYork"
print(str[0], str[3], str[6]) # returns N Y k -> indexing
print(str[-1], str[-3], str[-7]) # indexing from the end of the string, starting with -1. returns k o N

# this is called slicing. start index is included, end index is excluded
print(str[3:5], str[:5], str[3:], str[:3] + str[3:]) # returns Yo NewYo York NewYork (not last one to get the whole string)

# an index greater than length of the string - 1 would result in out of range error
# but, in slicing you can have larger indices such as:
print("With large indices:", str[3:42], str[546:]) #second one doesn't return anything

# Python strings are immutable; cannot assign value like str[5] = "P" to change values.
# You will have to create new strings like:

str2=str[:3] + "Delhi"
print(str2)

# to calculate length of the string
print(len(str), len(str2))


# ---- Lists ----

# They are of sequence data type i.e. indexed by integer. It can be sliced too similar to strings. 
# One interesting thing in Python is that the list can hold different data type values, but usually it is used to hold same data type values.

list = [1, 4, 9, 17]
print(list)

# you can copy the list as below. This creates a shallow copy i.e. 
# if the elements of the list are objects that have other objects, then it will just point to those objects, won't recursively copy.
list2 = list[:] 
print("Shallow copy:", list2)

# lists are mutable
list[3] = 16
print(list)

# to add new elements to list, use append method:
list.append(25)
list.append(6**2)
print(list)

# to find length of the list
print("Length of the list:", len(list))

# You can assign values to slices of list
list[2:4] = [49, 64]
print(list)

# remove an element from the list
list[3:4] = []
print("Removed 4th element:", list)

# remove multiple elements from list
list[2:4] = []
print("Removed 3rd and 4th element: ", list)

# clear all elements
list[:] = []
print("Cleared all elements. Length is", len(list))

# nested list are supported (multi-dimentional list similar to multiD arrays)
nestedList = [[1,2,3], ["Hi", "Nested", "List"]]
print(nestedList)


# Some more basics:

# You can assign multiple values in the same line. For eg:

a, b = 0, 1
a, b = b, a+b # expressions in RHS are all evaluated before assigning. RHS is evaluated from left to right.

# block scope is defined by indentations. No curly braces

# conditions in control statements: any non-zero integer is true, zero is false. 
# Conditions are also satisfied for other data types such as any sequence (string, list, etc.): non-empty is true and empty seq is false.

# print function: formats everything nicely. you can use end="" argument to specify the delimited instead of newline

print(a, end="---")
print(b)
