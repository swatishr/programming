

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


# while and if can contain any operators, not just comparisons

# in and not in : membership tests if a val is in the sequence or not

# is and is not : compare whether two objects are really the same object

# All comparison operators have same priority. Comparison operators < numerical operators priority

# comparisons can be chained. Eg: a > b == c is valid. First tests a> b and also check b == c

# Boolean operators: and, or, not. not has the highest priority amongst these. or has the lowest.
# Boolean operators have lower priority than comparison operators

# Similar to many other languages, and and or are short-circuit operators. 
# Args evaluated from left to right and execution is stopped once the outcome is determined.


