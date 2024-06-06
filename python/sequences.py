
########   List   #########

list1 = [1,2,3,4,5]

print("Appending a value to the list using + operator")
list1 = list1 + [8]
print(list1)

print("Appending a value to the list using append function") # append is more efficient than + operator
list1.append(10)
print(list1)


### For all sequences

# in operator: can be used with lists or dictionaries
print("\nin operator with list")
i=2
if i in [1,2,3]:
    print("i is in the list")
