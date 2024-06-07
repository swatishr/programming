

# Tuple is a type of sequence

# It is immutable

# But, it can consist of mutable objects

# During assignment, the values don't need to be in parantheses

# During output i.e. if you are printing the tuple, it will be displayed with parantheses.

t = 1234, -4857, "third"
print(t)

# tuples are mostly used for heterogeneous values whereas list is usually used to store sequences of homogeneous values.

# Initializing empty tuple

t = ()
print(t)

# If the tuple has only one element, the syntax to initialize it is a bit odd (needs a comma at the end to recongnize it's a tuple)

t = 123,
print(t)

# you can even unpack a tuple to multiple vars. This works for any sequence. 
# Only requirement is the number of variables on the LHS == number of elements in the sequence getting unpacked.

t = 1234, -4857, "third"
x, y, z = t
print(x, y, z)

l = [1,2,3]
x,y,z = l
print(x, y, z)