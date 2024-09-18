
# Single Inheritance

# When the class object is constructed, the base class is remembered. 
# This is used for resolving attribute references: if a requested attribute is not found in the class, the search proceeds to look in the base class. 
# This rule is applied recursively if the base class itself is derived from some other class.

class BaseClass:

    def __init__(self, name):
        self.name = name

    # all methods in Python are effectively virtual
    def update_name(self, new_name):
        self.name = new_name

    def clear_name(self):
        self.name = ""

class DerivedClass(BaseClass):

    # Method references are resolved as follows: the corresponding class attribute is searched, descending down the chain of base classes if necessary, and the method reference is valid if this yields a function object.
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade


    def update_name(self, new_name):
        super().update_name(new_name)


b = BaseClass("foo")
print("name: ", b.name)

b.update_name("new_foo")
print("name: ", b.name)

b.clear_name()
print("name: ", b.name)

d = DerivedClass("bar", 90)
print("name: ", d.name, "grade:", d.grade)

d.update_name("new_bar")
print("name: ", d.name)

d.clear_name()
print("name: ", d.name)

# Use isinstance() to check an instance’s type: isinstance(obj, int) will be True only if obj.__class__ is int or some class derived from int.
print("is d an instance of BaseClass:", isinstance(d, BaseClass))
print("is b an instance of BaseClass:", isinstance(b, BaseClass))
print("is b an instance of DerivedClass:", isinstance(b, DerivedClass))

# Use issubclass() to check class inheritance: issubclass(bool, int) is True since bool is a subclass of int. However, issubclass(float, int) is False since float is not a subclass of int.
print("is DerivedClass a subclass of BaseClass:", issubclass(DerivedClass, BaseClass))



## Multiple Inheritance

# Python supports a form of multiple inheritance as well.

class Mammal():

    def __init__(self, name):
        print(name, "Is a mammal")

class canFly(Mammal):

    def __init__(self, canFly_name):
        print(canFly_name, "cannot fly")

        # Calling Parent class
        # Constructor
        super().__init__(canFly_name)

class canSwim(Mammal):

    def __init__(self, canSwim_name):

        print(canSwim_name, "cannot swim")

        super().__init__(canSwim_name)

class Animal(canFly, canSwim):       # syntax is: `class DerivedClassName(Base1, Base2, Base3)`

    def __init__(self, name):
        super().__init__(name)

# Driver Code
Carol = Animal("Dog")
    