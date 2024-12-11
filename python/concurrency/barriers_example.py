'''
Barriers (threading.Barrier) is a synchronization primitive that helps synchronize multiple threads.
It takes a count as an argument that indicates how many threads it has to wait on.

Each thread performs some work and then calls barrier.wait() to wait at the barrier.
The barrier is "released" when the required number of threads have called barrier.wait(). At this point, all threads proceed simultaneously.

Advanced features:
1. You can provide a timeout to barrier wait(). If the given number of threads don't call wait by the given timeout,
an exception (threading.BrokenBarrierError) is raised.
2. You can specify a function to execute when the barrier is released.
3. Threads can perform independent work before and after the barrier synchronization.

Usage:
- Can be used for initializing a pool of threads before the actual work is kicked off simultaneously.
- Synchronizing threads at specific points in a computation.
- Ensuring that all threads start or finish a task together.
- Coordinating phases of a multi-threaded algorithm.
'''

import threading
import concurrent.futures
import time

barrier = threading.Barrier(3)

def worker(name):
    print(f"Thread {name} is executing some pre-setup")
    time.sleep(1)
    print(f"Thread {name} is waiting for the barrier")
    barrier.wait()
    print(f"Thread {name} has passed the barrier")

if __name__ == "__main__":

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(worker, range(3))

    print("All threads executed")