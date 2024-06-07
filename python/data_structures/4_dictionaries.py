
# Dictionaries are "associative memories" or "associative arrays" or "maps" in other languages.

# key:value pairs

# it's not a sequence (in sequences, elements are indexed by a range of numbers)
# But, in dictionary, they are indexed by keys

# keys need to be immutable types (like numbers, strings) but not lists. Tuples can be keys too.

telcode = {'jack': 716, "john": 456}
print(telcode)

telcode['anna'] = 389    # adding a key:value pair
print(telcode)

del telcode['john']      # removing a pair
print(telcode)

print(telcode['anna'])   # getting the value for a key

print('anna' in telcode) # membership
print('john' in telcode)

print(list(telcode))     # listing all the keys in the dict

print(sorted(telcode))   # sorted list of keys

print(list(telcode.values()))  # list all the values

# dictionary comprehension supported

squares = {x: x**2 for x in range(10)}
print(squares)

