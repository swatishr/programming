'''
Using the example in race_conditions_example.py, we are handling how to avoid the race condition
using Lock.
Lock provides mutual exclusion such that only one thread has access to the shared resource at a given time.

Only one thread can have the Lock. Any other thread has to wait until the owner of the Lock gives it up.

You can use lock's acquire() and release() functions to acquire and release the lock.
Or since Lock can act as a context manager, you can use it in a "with" statement too 
and the lock gets released once the block ends.
'''

import threading
import concurrent.futures
import time

class FakeDatabase:
    def __init__(self, val):
        self.value = val
        self._lock = threading.Lock()
    
    # update simulates reading the value, doing some computation on local copy and setting it to the original copy
    def update(self, name):
        print("Starting update by thread", name)
        with self._lock:
            print("Thread", name, "grabbed the lock")
            temp = self.value
            temp += 1
            time.sleep(0.1)
            self.value = temp
            print("Thread", name, "released the lock")
        print("Finished update by thread", name)

if __name__ == "__main__":

    database = FakeDatabase(10)
    print("Starting value is:", database.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(database.update, range(3))
    print("Final value is:", database.value)
    print("Main DONE")