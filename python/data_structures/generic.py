

### For all sequences

# in operator: can be used with lists or dictionaries
print("\nin operator with list")
i=2
if i in [1,2,3]:
    print("i is in the list")




#### Looping Techniques

# For dictionaries, you can use items() method to loop through key-value pairs 
print("\nDictionary key-value pair listing...")
dict1 = {'x': 1, 'y': 2}

for k, v in dict1.items():
    print(k, v)


# For lists or other sequences, enumerate() function can be used to get the index and the value at that index
print("\nList enumeration...")
for idx, v in enumerate(['a','b','c']):
    print(idx, v)

# for sets
print("\nSet enumeration...")
set1 = {1,2,3}
for idx, val in enumerate(set1):
    print(idx, val)


# To loop on more than one sequence, zip() function can be used to pair up the entries on the same index:
print("\nLooping through more than one se   quence using zip(list1, list2) function...")
l1=['a','b','c']
l2=[1,2,3]

for x,y in zip(l1, l2):
    print(x,y)


# To loop the list in reverse, use reversed function
print("\nLoop in reverse...")
for i in reversed(range(1, 10, 2)):
    print(i)


# Use sorted() function to return a sorted list without altering the original list.
print("\nsorted function on list....")
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for fruit in sorted(basket):
    print(fruit)

# Using set and sorted combination
print("\nTo get unique elements in a list in a sorted order")
for fruit in sorted(set(basket)):
    print(fruit)

# Sequences can be compared with each other. The comparison uses lexicographical ordering
# i.e. it compares the first element in the lists, if equal,, goes to next elements, etc.
# if the list is nested, it does lexicographic comparisons recursively.

# Usually, sequences having same types are compared.