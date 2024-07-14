# This file includes the functions/syntax that was new for me while solving leetcode problems

### initialize dict, set:
numdict = {} #or dict()
numset = set()

### you can assign multiple variables with the same value in the same line

a = b = 3
print(a, b)

### you don't need to compare it with None in conditions

Instead of doing `while p != None and q != None`, you can just write `while p and q`. In case of if: `if p`, not needed `if p == None`

### You can have inline if else during assignment

Eg: `p = head1 if head1 else head2`: This means assign p to head1 if head1 is not None else assign it to head2
```
if list1 or list2:
    p.next = list1 if list1 else list2
```


### Remove all non alphanumeric characters from a string
```
import re
re.sub(r'\W+', '', your_string) #\W keeps underscore (_) as well. But it keeps all the non-ASCII characters
```

So, if you only want ASCII characters and no underscore then:

```
''.join(ch for ch in s if ch.isalnum() or '')
```

This is faster:
```
words_str = [ch for ch in s.lower() if ch.isalnum()]
```


### Boolean

Remember boolean values in Python starts with captial letter: `True` and `False`.

### Dictionary

Regular dictionary is initialized as `count = {}`. But, this returns KeyError if you try to get a key that does not exist

If you want a dictionary with default values assigned, then use the defaultdict from collections package

Syntax: defaultdict(default_factory)
Parameters:  
    default_factory: A function returning the default value for the dictionary defined. If this argument is absent then the dictionary raises a KeyError.

You can have custom default_factory functions too.

```
from collections import defaultdict

d = defaultdict(int) => defaults the values to 0
d = defaultdict(list) => defaults the values to empty list
```


### Sorting

Python default sorting function:

```
s = "Hello World"
sorted_s = sorted(s)
```

Remember that sorted function returns a list. If you want a string out of it then use `''.join(sorted(s))`


### Boolean operators

```
and
or
```

### Loops

You can't use `while` to iterate over the string or a collection with this syntax: `w in words`. You must use `for`: `for w in words`


### enumerate in Loops

You can use enumerate on a list to get an <index, val> pair

```
for i, num in enumerate(nums):
```

### How to have a counter map for string

I was handling counter similar to how we do it in Java/Go:

```
counter = defaultdict(int)

for ch in s:
    counter[ch] += 1
```

However, in Python, you can have the counter as below:

```
Counter(s).values()
```


# Slicing a list

Slicing Python lists always creates copies. So, if you want to apply reverse on a slice of a list in-place, you can't use the reverse function, reversed, or slicing operation for reverse.


# Integer max and min

```
import sys

INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize-1
```

# Get random value from a list with equal probability:

```
random.choice(list)
```

# Different methods to get digits out of an integer number in Python

```
while num != 0: #from RHS o LHS
    digit = num % 10
    print(digit)
    num = num // 10
```

```
for i in str(current_number): #from LHS to RHS
    digit = int(i)
    print(digit)
```

# Verify if a string is an integer (It should be able to pick up negative numbers too)

One way is to use isDigit function but for negative numbers, need an additional check

```
if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
```

Another way is to use try...except block while converting string into int using int() function

```
try:
    intVal = int(str)
except ValueError: # not a valid integer
    # logic for non integer strings.
```

# How to use a variable from parent function in the nested functions

I faced this issue in leetcode problems where I needed to use a global variable defined in the enclosing function.
However, I used to get this error.
```
UnboundLocalError: cannot access local variable 'curr_max' where it is not associated with a value
```

This is because Python redefines the variable with that name for the inner function.

In order to use the one defined in the parent, we need to use the below statement in the child/enclosed function:

```
def maxPathSum(self, root):
    curr_max = float('-inf')

    def helper(root):
        nonlocal curr_max
        ...
```

### Check out


package re (for regex and pattern matching)
string functions
self in class