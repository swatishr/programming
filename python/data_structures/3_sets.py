
# set is an unordered list of elements with no duplicates

# Usually used for membership tests and eliminating duplicates


# Initializing empty set

s = set()
s.add(2)
print(s)

# sets can be initialized by elements in curly braces

s = {"a", "b", "c", "a", "d", "e"}
print(s) # removes duplicates

# membership tests
print("a" in s) # returns True
print("f" in s) # returns False

# supports different set functions like union, intersectoin, difference, symmetric difference

s1={'a', 'b', 'c', 'd'}
s2={'v','a','d','e','f'}

print(s1)
print(s2)
print(s1-s2) #elements in s1 that doesn't exist in s2; prints {b, c}
print(s1 & s2) # elements in both s1 and s2 {a,d}
print(s1 | s2) # elements in s1 or s2 or both
print(s1 ^ s2) # elements in a or b but not in both {b, c, v, e, f}

# set comprehensions also supported

print("\nset comprehension...")
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

