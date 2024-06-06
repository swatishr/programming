
# Functions


# defined using `def` keyword. Accepts arguments
# Python functions use "Call by Object Reference" or "Call By Assignment". Depending upon the type of argument, immutable or mutable, it uses call by value or reference respectively.
# For eg. in case of strings, numbers, tuples (they are immutable objects), it's like call-by-value.
# For lists, dictionaries, it will be call by reference since the object itself is mutable.


# When a function doesn't return anything, by default it returns "None". return without an expression argument returns None. Falling off the end of a function also returns None.
# Writing the value None is normally suppressed by the interpreter if it would be the only value written.



def fib(n):
    """Print a Fibonacci series from 0 to n.""" #documentation string of the function
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

print("**Function example with nothing to return**")  
fib(20)

print("All the functions return value. The ones that don't have explicit return statements, return None")
print(fib(0))

# With return type

def fib(n):
    result=[]
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

print("**Function example with return value**")  
series = fib(20)
print(series)

### Default Arguments

# You can have default values for function arguments such that the function call can have only the non-default args set or even override the default ones
print("\nfunctions with default args...")
def funcWithDefaultArgs(arg1, arg2=3, arg3='third argument'):
    print(arg1)
    print(arg2)
    print(arg3)

funcWithDefaultArgs("call with only only non-default")
funcWithDefaultArgs("call with overriding one default arg", "4")
funcWithDefaultArgs("call with overriding both default args", "4", "override 3rd arg")


# The default values are evaluated at the point of function definition in the defining scope, so that the below function prints 5 since i is set to 5 before the function definition.

i = 5

def f(arg=i):
    print(arg)

i = 6
f()

# The default value is evaluated only once. 
# This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes. 
# For example, the following function accumulates the arguments passed to it on subsequent calls:

def func(a, L=[]):
    L.append(a)
    return L

print(func(1))
print(func(2))
print(func(3))

# if we want a fresh default on the mutable object each time, it can be resolved using the following code:

def funcWithoutAccumulation(a, L=[]): #Or L=None
    if len(L) == 0: #Or if L is None
        L=[]
    L.append(a)
    return L

print(funcWithoutAccumulation(1))
print(funcWithoutAccumulation(2))
print(funcWithoutAccumulation(3))


### Keyword Arguments

# You can have keyword arguments following positional arguments. This means while calling the function, you can provide the name of the argument as the key.
# the keyword arguments don't need to be in order but they need to follow the positional (non-keyword) arguments.

def keyword_func(arg1, arg2="def1", arg3="def2"):
    print("\nTrying different versions of keyword argument placements")
    print("I am non default arg", arg1)
    print("I am a keyword arg: ", arg2)
    print("I am the next keyword arg: ", arg3)

# we can call this function in different ways:
# Note: duplicate value for same argument is not allowed. for eg: keyword_func(100, arg1=2000)
# unknown keyword is errored out
# non-keyword arg after keyword arg also errors out

keyword_func(1000)
keyword_func(1000, arg2="override1")
keyword_func(1000, arg3="override2", arg2="override2") #positions of keyword args can change, given that we have keyword identifiers
keyword_func(1000, arg3="only-override-3")

# you also have interesting formal parameters of the form **arg or *arg.
# **arg will result into a map with keys == keywords used and values set to the values passed in the function call
# *args result in a list and will accept all the positional args
# **args should follow *args
# We won't go into much details but something to keep in mind (or explore later) if you see such args in Python code


#### Special Parameters / and *

# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):

#As guidance:

#Use positional-only if you want the name of the parameters to not be available to the user. 
#This is useful when parameter names have no real meaning, if you want to enforce the order of the arguments when the function is called 
#or if you need to take some positional parameters and arbitrary keywords.

#Use keyword-only when names have meaning and the function definition is more understandable by being explicit with names 
#or you want to prevent users relying on the position of the argument being passed.

#For an API, use positional-only to prevent breaking API changes if the parameter’s name is modified in the future.


#### Arbitrary Arguments List OR Variadic Arguments

# These variables must follow all the positional args. Only keyword-only args can be after variadic ones.
# This is because variadic args scoop up all the remaining input args passed

print("\n Arbitrary or Variadic arguments list")

def concat(*args, sep="/"):
    return sep.join(args)

print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep="."))


### Lambda expressions

# Can be used to write small anonymous functions. 
# They can be used wherever function objects are required
# You can also use lambda to pass function as an argument
# See both the examples below:

print("\nlambda expressions as return functions")

def incrementor(n):
    return lambda x: x+n

f = incrementor(2)
print(f(12))
print(f(0))

print("\nlambda expressions as arguments to function")

pairs = [(2, "two"), (4, "four"), (8, "eight")]
pairs.sort(key=lambda pair: pair[1])

print(pairs)