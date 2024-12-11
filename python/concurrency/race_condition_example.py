'''
Race conditions occur when multiple thread are accessing a shared object/resource
and if you are not handling it properly.

In the below code, we see one such example.
The output is expected to be 13 but it is always 11 (purposefully, it is made deterministic to always fail)

'''
import concurrent.futures
import time

class FakeDatabase:
    def __init__(self, val):
        self.value = val
    
    # update simulates reading the value, doing some computation on local copy and setting it to the original copy
    def update(self, name):
        print("Starting update by thread", name)
        temp = self.value
        temp += 1
        time.sleep(0.1)
        self.value = temp
        print("Finished update by thread", name)

if __name__ == "__main__":

    database = FakeDatabase(10)
    print("Starting value is:", database.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(database.update, range(3))
    print("Final value is:", database.value)
    print("Main DONE")