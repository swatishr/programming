

# To compare objects based on their values, Python’s equality operators (==) are employed
# Python identity operators (is, is not) are used to compare objects based on their identity. 
# When the variables on either side of an operator point at the exact same object, the “is” operator’s evaluation is true. 
# Otherwise, it would provide us with a false assessment.
# is operator can't be used for literal comparison

i = 2
if i is 2: # works but raises a SyntaxWarning
    print("i is 2")

if i==2:
    print("i is 2 and doesn't raise syntaxwarning")

j = 2

print(i==j)
print(id(i))
print(id(j))
print(i is j) # This returns True because since the RHS is a literal, both i and j point to the same memory location.

list1 = []
list2 = []

print(list1 == list2) # returns True
print(list1 is list2) # returns False since Lists refer to two different objects
