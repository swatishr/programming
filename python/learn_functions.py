
# Functions


# defined using `def` keyword. Accepts arguments
# Python functions use "Call by Object Reference" or "Call By Assignment". Depending upon the type of argument, immutable or mutable, it uses call by value or reference respectively.
# For eg. in case of strings, numbers, tuples (they are immutable objects), it's like call-by-value.
# For lists, dictionaries, it will be call by reference since the object itself is mutable.


# When a function doesn't return anything, by default it returns "None". return without an expression argument returns None. Falling off the end of a function also returns None.
# Writing the value None is normally suppressed by the interpreter if it would be the only value written.



def fib(n):
    "Print a Fibonacci series from 0 to n."
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

print("**Function example with nothing to return**")  
fib(20)

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


