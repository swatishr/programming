# Everything Strings


# Important string functions

## Related to string case:

s = "hello WoRld. I am here."
print("\nOriginal string:", s)

c = s.capitalize() #Capitalizes first letter only and lowers all the other letters
print("\ns.capitalize(): ", c)

u = s.upper() #all letters uppercased
print("\ns.upper():", u)

l = s.lower() #all letters lowercased
print("\ns.lower():", l)

#swapcase. swaps the cases lower->upper and upper->lower
# s.swapcase().swapcase() == s is False for some unicode characters(not ascii)
s = "Hello World"
print("\ns.swapcase():", s.swapcase())

# title returns a string where all the words first letter is made uppercase. 
# This also includes any word separated by punctations like apostrophes
print("\ns.title(): ", "Hello it's me".title()) #s is also capitalized.

l = u.casefold() # lowers all the characters aggressively. 
# It means that it also lowers some unicode characters that are not converted with .lower().
# lower() is used when you want to lowercased version of a string and casefold is used for case-insensitive string comparison 
## What is case folding: https://www.w3.org/TR/charmod-norm/#definitionCaseFolding
print("\ns.casefold():", l)


## Justifications

# center() function centers the string, given the length of the resultant string and filled characters to left and right
# by default, fills up space.
s = "Hello World"
c = s.center(16, "_")
print("\ns.center():", c) 

#ljust, rjust: left/right justification and accepts width that is the resultant string length
print("\ns.ljust(width, [fillchar]) s.rjust(width, [fillchar]):", "Hello".ljust(9, "_"), "Hello".rjust(9, "_"))


# Strip strings: lstrip, rstrip, strip (By default, strips whitespaces)

# These functions accept an optional string that you want to strip. It's not a prefix rather it strips strings that match all ocmbinations of those characters.
print("\ns.lstrip([string]):", "___Hello___".lstrip("_")) 
print("s.rstrip([string]):", "___Hello___".rstrip("_")) 
print("s.strip([string]):", "Hello".rstrip("_")) 

# Split strings: split() and rsplit(). Accepts a separtor and maxsplit, which is a counter until when to split
# rsplit() behaves like split if maxsplit is not provided
# Remember splitting with consecutive delimiters include empty strings in the result.

print("\ns.split(sep):", "Hello World. How are you?".split(" ")) 
print("s.split(sep) with consecutive delimiters:", "Hello World.  How  are you?".split(" "))
print("s.rsplit(sep):", "Hello World. How are you?".rsplit(" ")) 
print("s.rsplit(sep) with maxsplit:", "Hello World. How are you?".rsplit(" ", 2)) 

#splitlines: splits on line breaks. There are different line boundaries that can be provided as arg, but default is \n
# Another arg keepends if True, also includes the line boundary character in the splitted strings

print("\ns.splitlines():", "Hi\nI\nam\ngetting\ngood\nat\nPython\n".splitlines())
print("\ns.splitlines() with keepends true:", "Hi\nI\nam\ngetting\ngood\nat\nPython".splitlines(keepends=True))

## Counters

# count() counts the number of characters in a string. You can also provide start and end index.
s = "Hello World"
c = s.count("l")
print("\ns.count(char):", c) 

# Index

# find: returns the loewst index of the substring if the substring exists. returns -1 if not
# use `in` operator to check if the string exists. Only use find if you need the index.
print("\ns.find(substr): ", "Hello World World".find("World"))

# there is an rfind function, similar to find, but returns the highest index
print("\ns.rfind(substr): ", "Hello World World".rfind("World"))

# index function is similar to find but if the substring is not found, it returns a ValueError instead of -1
print("\ns.index(substr):", s.index("World"))

## Substrings

# endswith: returns true if a string ends with the given string. You can also pass optional start and end pos.
s = "Hello world"
print("\ns.endswith(some_str): ", s.endswith("rld"))
print("s.endswith(some_str): ", s.endswith("Hello"))

# startswith: returns true if a string ends with the given string.
print("\ns.startswith(some_str): ", s.startswith("Hello"))
print("s.startswith(some_str): ", s.startswith("rld"))


## Check the string is something

# all of the below functions return False (except isprintable) if string is empty.

# isalnum checks that the string only has alphanumeric characters. Even no decimal point.
s = "Hi1234"
print("\ns.isalnum()", s.isalnum())

# isalpha checks if the characters are only alphabets.
print("\ns.isalpha():", s.isalpha())
print("\ns.isalpha():", "Hello".isalpha())

# isascii checks that the characters are ascii (0-127)
print("\ns.isascii():", s.isascii())
print("\ns.isascii():", "Åpple".isascii()) # doesn't include extended ascii

# isdecimal: returns true if the characters are decimal numbers i.e. base10.
print("\ns.isdecimal():", "23.45".isdecimal())
print("\ns.isdecimal():", "2345".isdecimal())

# isdigit
print("\ns.isdigit():", "23𐩃5".isdigit()) #Fun fact: isdigit includes idecimals and Kharosthi numbers. so this returns true
print("\ns.isdigit():", "2345".isdigit())

# isidentifier returns True if the string is a valid indeitifer in Python. ascii characters. alphabets, _, digits but not the first character
from keyword import iskeyword
print("\ns.identifier():", "_abc".isidentifier(), "1abc".isidentifier())
print("iskeyword(s) from keyword package:", iskeyword("def"), iskeyword("abc"))

# islower and isupper
print("\ns.islower()", "abcd".islower(), "AbcD".islower())
print("s.isupper()", "ABCD".isupper(), "AbcD".isupper())

# isnumeric
print("\ns.isnumeric()", "123".isnumeric(), "12.34".isnumeric(), "⅕".isnumeric()) 
# the last one is unicode U+2155 called vulgar fraction one fifth, there are other vulgar fractions represented in unicode
# and that's the difference of isnumeric with isdigit and isdecimal. It includes isdigit and isdecimal and includes these extra things.

# isspace returns true if string consists of all whitespaced characters: space, \t, \n
print("\ns.isspace()", " \t\n".isspace(), "abcd nn".isspace()) 


## Concatenation / Divide

# join accepts an iterable object and concatenates all the string in that object with the separator on which the function was called.
print("\ns.join(iterable):", "_".join(["abc", "def", "ghi"]))

# partition function divides a string, given a separator is found first. It returns 3 strings: first part, separator itself, and then the last part
# if no separator found, returns the string itself, and two empty strings

print("\ns.partition(separtor):", "Hello_World_Hi".partition("_"))
print("s.partition(separtor):", "Hello_World".partition(" "))

# similarly, there is rpartition too, which partitions the string at the last occurrence of the separator
print("\ns.rpartition(separtor):", "Hello_World_Hi".rpartition("_"))

# removeprefix and removesuffix removes given string if it's a prefix or suffix and returns the resultant string
# else returns the whole string itself

print("\ns.removeprefix(substr):", "Hello_World".removeprefix("Hello"))
print("s.removesuffix(substr):", "Hello_World".removesuffix("World"))

# replace function replaces all occurrences of an old str with new. 
# There is optional count arg too, if provided, only replaces first "count" occurrences of the old string

print("\ns.replace(old, new, [count]):", "too late, too bored".replace("too", "not"))

## Other functions

#Return the string encoded to bytes.
s = "Mr S†åle"
e = s.encode("ascii", "ignore") # this will remove the non-ascii characters from string because they are not in th ascii range
# so ascii codec can't recognize those words. But, since we have selected "ignore" as error handling, it just removes it.
# if you have encoding as "utf-8", it doesn't error out.
print("\ns.encode(encoding, error_handling)", e)




