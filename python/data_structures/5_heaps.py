

# Python built in data structure for heap

# Python has built-in Heap data structure but it is only a MinHeap.
# In order to use it as MaxHeap, if you are using heap for a list of numbers, you need to negate the numbers and add to the heap.
# If you are inserting objects, then you need to create objects and proper comparators to insert it into the heap


import heapq

list = [3,6,2,8,1,-1]
print("before heapify: ", list)

# create a heap from an existing list. If you have an empty list, you can directly invoke heappush and heappop on the list without calling heapify on the empty list.
heapq.heapify(list)

# Now, list itself has been modified
print("after heapify: ", list)

# Get the minimum element
print("minimum element in the list: ", list[0])   #O(1)

# Insert element
heapq.heappush(list, 10)
print("after insert: ", list)

# Pop element (i.e. remove the minimum element)
x = heapq.heappop(list)
print("popped element: ", x)