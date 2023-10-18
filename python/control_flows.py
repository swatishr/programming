# Control Flow Tools

#### ----- if..elif..eif..else -----

x = 10   
if x < 0:
    print("x is negative")
elif x > 0:
    print("x is positive")
else:
    print("x is 0")
 
   
#### ----- for statement ------

# it doesn't follow C, Java-style format

words = ["I", "am", "learning", "python"]
print("Using for..in syntax")
for w in words:
    print(w)

# if you are going to update the collection while you are iterating on it, you could see unexpected results
# so, in such cases, better to iterate over a copy and update the items

dict = {"A": "active", "B": "inactive", "C": "active"}

print("collection before deletion: ", dict)
for user, status in dict.copy().items():
    if status == "inactive":
        del dict[user]
        
# if you don't iterate on copy(), then you will get this error: RuntimeError: dictionary changed size during iteration. 
# Try it out yourself by removing copy() call above
        
print("collection after deletion: ", dict)


# for using range function
print("\n***using for...range***")

for i in range(5):
    print(i) # it prints from 0 to 4, so excludes the end value that you provide here
    
# it is also possible to start the range on some other number rather than 0 (default), 
# increment (called as step) it instead of 1 (default), examples:

print("\n starts from 5 to 10 (excluded) with default step of 1")
for i in range(5, 10):
    print(i)
    
print("\nstarts from 5 to 10 (excluded) with step of 2")
for i in range(5, 10, 2):
    print(i)
    
print("\nstarts from -5 to 10 (excluded) with default step of 5")
for i in range(-5, 10, 5):
    print(i)
    
    
# To iterate over the indices of a sequence

print("\nIterate over the indices of a sequence:")
words = ["Python", "is", "so", "succint"]
for idx in range(len(words)):
    print(idx, words[idx])


# range is a function that takes start value, stop value, and step as arguments. It doesn't return a list, but an iterable.
# Iterable is an object which returns the successive items of the desired sequence when you iterate over it, 
# but it doesn’t really create a list of sequenced numbers, thus saving space.

# so, you can also pass range function as arguments to the functions that accept iterable objects, one such example is sum() function.

print("\nSum of range over 6: ", sum(range(6))) # 0+1+2+3+4+5 = 15


#### ----- break, continue, for...else

# Yes, you already what break and continue does in the for loops, if you come from C, Java, Go
# But, in Python, you can also have an else attached to a for loop.
# the else part of for loop runs after the loop reaches its final iteration. It doesn't run when a break is executed inside for. 

# Find all the prime numbers till a given number n

n = 10
for i in range(2, n):
    for factor in range(2,i//2+1):
        if i%factor == 0:
            print(i, "is not prime")
            break
    else:
        print(i, "is a prime number")
        
        
#### --- pass statement---

# They do nothing, used when the code is needed but we need no action. It's mainly used when you are creating minimal classes 
# or as a placeholder for the abstraction that you have created while writing code, so that you can revisit and fill it out
        
# while True:
#     pass # Busy waiting for keyboard contorl (Ctrl+C)

class MyEmptyClass:
    pass

def initLogs():
    pass # Remember to implement this!

#### --- match statement ---
# match statement was introduced in 3.10. Fairly recent, as I write it.
# it's similar to switch..case in other languages. It can be matched to literals, so exactly same behavior as like switch..case.
# _ acts as a default case as shown in the below example. You can combine several literals in a single pattern by using | ("or" operator)
# Interestingly, it also provides different additional features, including unpacking assignments and binding to variables, and you can use if with case statements as guard rules.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
            
where_is(Point(0,1))
