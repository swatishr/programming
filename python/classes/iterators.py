
# You can create a custom iterator for a class

# Behind the scenes, the for statement calls iter() on the container object. 
# The function returns an iterator object that defines the method __next__() which accesses elements in the container one at a time. 
# When there are no more elements, __next__() raises a StopIteration exception which tells the for loop to terminate. You can call the __next__() method using the next() built-in function

class IterBackwards:

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):         # __iter__ is the function that's called by for..range for an iterable object
        return self

    def __next__(self):         #__next__ is called after each iteration
        if self.index == 0:
            raise StopIteration # StopIteration is a built-in exception that's raised by default iterators. It's an exception and thus "raise" keyword
        self.index -= 1
        return self.data[self.index]
    

string = IterBackwards("hello")
print(string.index)

print("using direct next function: ", next(string))

for ch in string:
    print(ch)
