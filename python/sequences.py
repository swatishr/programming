
########   List   #########

list1 = [1,2,3,4,5]

## Append an item to the list: list.append(x)

print("\nAppending a value to the list using + operator")
list1 = list1 + [8]
print(list1)

print("\nAppending a value to the list using append function") # append is more efficient than + operator
list1.append(10)
print(list1)

print("\nAppending a list by assigning a list to the end of the list: a[len(a):] = [x]")
list1[len(list1):] = [20]
print(list1)

## Insert into a list: list.insert(i, x)

print("\n insert 30 on 3rd index using insert method")
list1.insert(3, 30)
print(list1)

print("\nyou can also append using insert method by inserting the element at index len(a)")
list1.insert(len(list1), 40)
print(list1)


## Extend a list: list.extend(iterable)

# This mean appending all the items from the iterable
# Equivalent to a[len(a):] = iterable

print("\n Extend a list")
list2 = [4,5,6]
list2.extend(list1)
print(list2)


## Remove an element from the list. list.remove(x) where x is the value. 
# raises a ValueError if no such element exists

print("\n Remove a value from a list")
list1.remove(30)
print(list1)

## Pop an element from the list: list.pop([i])

# optional argument. You provide the index of the element that you want to pop. It returns the value. 
# If no index specified, pop() removes and returns the last item in the list.
# IndexError if index is invalid.

print("\n Pop a value from a list")
x = list1.pop(3)
print(list1)
print("Value popped: ", x)


## Find index of an item in the list: list1.index(x[, start[, end]])
# returns zero-based index of the first occurrence of that item
# you can provide start and end index to limit the search i.e. find the index of the element in that range and not the whole list
# ValueError if no such value exists

print("\n Get index of a value from a list")
x = list1.index(10)
print("Index of 10: ", x)


## Count the occurrence of a value in the list: list1.count(x)

print("\n Get the count of 20 in the list")
print(list1.count(20))

## Sort the list: list.sort(*, key=None, reverse=False)

# Sort the items in ascending order by default.
# key specifies a function of one argument that is used to extract a comparison key from each element in iterable
# reverse, if True, sorts the list in descending order

print("\nregular sort")
list3 = ["Hello", "world", "Ladies", "and", "Gentlemen"]
list3.sort()
print(list3)

print("\n sort with a custom function as a key")
list3 = ["Hello", "world", "Ladies", "and", "Gentlemen"]
list3.sort(key=str.lower)
print(list3)

## Reverse a list: list.reverse()

print("\nreverse a list")
list1.reverse()
print(list1)

## Copy the list. Shallow copy: list.copy()
# equivalent to list[:]

print("\ncopy list1 and then update the new list")
list2 = list1.copy()
list2[5] = 300
print(list2)

## Clear a list list.clear()
# Equivalent to `del a[:]`

print("\nClear list1")
list1.clear()
print(list1)

print("\n clear list2 using del a[:]")
del list2[:]
print(list2)

# You might have noticed that methods like insert, remove or sort that only modify the list 
# have no return value printed – they return the default None.
# This is a design principle for all mutable data structures in Python.


### List as Stack

# list3.append("top")
# list3.pop()

### List as queue

# Since we need to pop from the first item, lists are inefficient.
# So, use collections.deque

print("\nUsing collections.deque for queues")
from collections import deque
queue=deque(["Hi", "I", "Am"])
queue.append("A")
queue.append("Queue")
print("queue: ", queue)
print(queue.popleft())
print(queue.popleft())
print("queue: ", queue)


### List comprehensions

# provides a concise way to create lists from another seuqnece.

print("\nRegular way to create a list with squares of numbers till 10, using for loop")
squares = []
for i in range(10):
    squares.append(i**2)
print(squares)

# In the above method, variable x still resides in memory after the loop exits

print("\ncalculating squares from a list of numbers using lambda")

squares = list(map(lambda x:x**2, range(10)))
print(squares)

print("\nList comprehension way to create a list of squares using for...in")

squares = [x**2 for x in range(10)]
print(squares)

# A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. 
# The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.

print("\nCombine the elements of two lists if they are not equal using list comprehension")

pairs = [(x,y) for x in [1,2,3] for y in [2,3,5] if x != y]
print(pairs)

print("\nflatten a 2D list using list comprehension")
vec = [[1,2,3],[4,5,6],[7,8,9]]
print("input", vec)
flat=[elem for row in vec for elem in row]
print("flattened list: ", flat)


### Nested List Comprehensions

# You can nest these list comprehensions. 

print("\nTranspose a matrix using nested list comprehension")
matrix= [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

transposed_matrix=[[row[i] for row in matrix] for i in range(4)]
print(transposed_matrix)


### del statement

# Using del statement, you can remove an element or a slice of elemnets from the list by index and not using values like list.remove().
print("\n delete elements using del statement")
a = [-1, 1, 66.25, 333, 333, 1234.5]
print("input: ", a)
del a[1]
print("After removing item at index 1: ", a)

del a[2:4]
print("After removing item from index 2 to 4 (excluding 4): ", a)

del a[:]
print("Cleared the whole list: ", a)

del a
print("deleting entire variable: ", a) # returns error that says name a is not defined




### For all sequences

# in operator: can be used with lists or dictionaries
print("\nin operator with list")
i=2
if i in [1,2,3]:
    print("i is in the list")