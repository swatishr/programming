
# A function which returns a generator iterator. 
# It looks like a normal function except that it contains yield expressions for producing a series of values usable in a for-loop or that can be retrieved one at a time with the next() function.

# generator iterator
# An object created by a generator function.
# Each yield temporarily suspends processing, remembering the location execution state (including local variables and pending try-statements). 
# When the generator iterator resumes, it picks up where it left off (in contrast to functions which start fresh on every invocation).

# Compute fibonacci series using generators

num = input("Enter the length of Fibonacci series to be generated:")   # input() function accepts a prompt and returns a string.

def fib(n):
   x, y = 0, 1
   for _ in range(n):
      yield(x)
      x, y = y, x+y 

print(fib(num))    # this prints the generator object

gen = fib(int(num))   # gen variable is of type iterator (generator iterator)

print("using next(iterator) function: ", next(gen))  # this should return 0

# using for loop
for i in gen:
   print(i)

# using list function
gen2 = fib(int(num))
print(list(gen2))



##### Generator expressions #####

# Some simple generators can be coded succinctly as expressions using a syntax similar to list comprehensions but with parentheses instead of square brackets. 
# These expressions are designed for situations where the generator is used right away by an enclosing function.
# Generator expressions are more compact but less versatile than full generator definitions and tend to be more memory friendly than equivalent list comprehensions.


# sum of squares

squares = sum(x*x for x in range(10))
print(squares)

# multiplying 2 lists
list1 = [2,3,4]
list2 = [5,6,7]

total = sum(x*y for x,y in zip(list1, list2))
print("using zip:", total)