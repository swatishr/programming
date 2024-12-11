'''
A Semaphore is a synchronization primitive that helps with limiting the number of threads to a critical section.
It's a counter.

The counting is atomic. 
i.e There is a guarantee that the operating system will not swap out the thread in the middle of incrementing or decrementing the counter.
Only one thread can increment/decrement it at a given time.

The internal counter is incremented when you call .release() and decremented when you call .acquire().

The next special property is that if a thread calls .acquire() when the counter is zero, 
that thread will block until a different thread calls .release() and increments the counter to one.

Usage: Used to protect a resource that has a limited capacity. 
An example would be if you have a pool of connections and want to limit the size of that pool to a specific number.

Rate-Limiting Access: To control how many threads can access a shared resource simultaneously.
Connection Pooling: Managing a pool of limited resources like database connections.
Simulating Bounded Resources: When you want to model limited availability of resources (e.g., parking spaces).

'''

import threading
import concurrent.futures
import time

semaphore = threading.Semaphore(2)

def worker(name):
    print("Thread ", name, "waiting for semaphore")
    with semaphore:
        print("Thread ", name, "acquired semaphore")
        time.sleep(2) # some critical section that needs restricted access of only 2 threads simultaneously
    print("Thread ", name, "released semaphore")

if __name__ == "__main__":

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(worker, range(5))






