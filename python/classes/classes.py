

class Dog:
    """A simple Dog class"""       # this is a documentation string that can be printed using an attribute called __doc__ as shown below

    kind = "canine" # this is a class variable. It's shared among all the instance objects of the class. If it's a slice, dictionary, or dynamic objects then the value would change across objects

    # __init__ is like a constructor in Java. It's used when you need some kind of initial state. You can either have it without or with arguments, as per your customization needs.
    # __init__ is not mandatory if there is no instance variables. You can still create objects of class without __init__, no customization.
    def __init__(self, name=""):
        self.name = name        # this is an instance variable. It's distinct for each instance object
        self.eats = []

    def bark(self, sound):      
        print(self.name, "barks", sound)


print(Dog.__doc__)           # prints the class documentation string

# Below print prints a string and functions objects. These are valid attribute references. You can even assign Dog.kind to something else.
print(Dog.kind, Dog.bark)


# Below d1 and d2 are called instance objects.
# The only operations understood by instance objects are attribute references. There are two kinds of valid attribute names: data attributes and methods.

d1 = Dog("Fluffy")           # creates a new instance of class Dog and assigns it to d1. invokes __init__

# One interesting take with data attributes is that you can have some variables on that instance which doesn't belong to the class too. 
# Data attributes need not be declared; like local variables, they spring into existence when they are first assigned to. This is only applicable to data attributes and not method attributes. You can't sprung up a new method on the object which doesn't belong to the class.
# For eg:

d1.barkCount = 1
while d1.barkCount < 5:
    d1.barkCount *= 2
print(d1.name, "barks", d1.barkCount, "times")

# The below fails since d2 doesn't have that data attribute. It returns error: AttributeError: 'Dog' object has no attribute 'barkCount'
# print(d2.barkCount)


# instance variables are for data unique to each instance and class variables are for attributes and methods shared by all instances of the class
print(d1.kind, d1.name)


# Valid method names of an instance object depend on its class. By definition, all attributes of a class that are function objects define corresponding methods of its instances.
# See how the function called on an object and class are of different types
# A method is a function that “belongs to” an object.
print(Dog.bark, d1.bark)          # Dog.bark is a function object and d1.bark is a method object


# One interesting things you might have noted is the function eifinition has two args: self, sound but we pass only a string that's sound. WHy?
# Because the special thing about methods is that the instance object is passed as the first argument of the function. In the below example, the call d1.bark("woof") is equivalent to Dog.bark(d1, "woof")
# When the method object is called with an argument list, a new argument list is constructed from the instance object and the argument list, and the function object is called with this new argument list.
# ‘ self ‘ is not a keyword in Python. Self is just a parameter name used in instance methods to refer to the instance itself.

# Self is a convention and not a Python keyword. Self is a parameter in Instance Method and the user can use another parameter name in place of it. But it is advisable to use self because it increases the readability of code, and it is also a good programming practice.

d1.bark("woof")

d2 = Dog("Tommy")
print(d2.kind, d2.name) # it prints same kind as that of d1 since it's a class variable
d2.bark("hau")

# If the same attribute name occurs in both an instance and in a class, then attribute lookup prioritizes the instance
d2.kind = "hound"
print(d2.kind, d2.name)
print(d1.kind, d1.name)

print(d1.__class__)


