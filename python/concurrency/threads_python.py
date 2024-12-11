'''
In Python, threads execute only one at a time. Why? because of GIL (Global Interpreter Lock) that is acquired for an entire program.
So, even if the program is spawning off multiple threads, and even if executed on different processors,
it is running one after another.
So, better to use it for tasks that wait for an external call for a long time instead of using threads for CPU intensive applications
In other programming languages like C, the threads can run concurrently since they release the GIL lock.

For CPU-bound problems, better to use multiprocessing Python package. Threads won't speed those programs.
'''

# threading package
import threading
import time
import concurrent.futures

# create a thread using Thread class and start it by invoking start() function
def thread_func(name):
    print("Thread ", name, " started")
    time.sleep(2)
    print("Thread ", name, " finished")

if __name__ == "__main__":
    '''
    The below block of code demonstrates how main thread executed before and waits for all the threads to be done
    Why? Because internally, threading._shutdown which is called at the end of the program invokes join()
    on each of the threads spawned off.
    '''
    # print("before creating two threads")
    # thread1 = threading.Thread(target=thread_func, args=(1,))
    # thread1.start()
    # print("started thread 1")
    # thread2 = threading.Thread(target=thread_func, args=(2,))
    # thread2.start()
    # print("started thread 2")
    # print("main done")

    '''
    Below block shows daemon threads. Once the main program executes and is done, it doesn't wait for daemon threads
    since threading._shutdown() function doesn't call join for daemon threads.
    You won't see finished log lines for below code
    '''
    # print("before creating two threads")
    # thread1 = threading.Thread(target=thread_func, args=(1,), daemon=True)
    # thread1.start()
    # print("started thread 1")
    # thread2 = threading.Thread(target=thread_func, args=(2,),daemon=True)
    # thread2.start()
    # print("started thread 2")
    # print("main done")

    '''
    Using join() and multiple threads: 
    join() should be called from a thread if you want to wait for another thread to be finished
    It can be used on daemon or non-daemon threads and it will have the same effect.
    Now, you can see that the finished log lines are printed before the main finished log line.

    Multiple threads can finish at any time.
    '''
    print("Main: before creating multiple threads")

    # threads = list()
    # for i in range(3):
    #     print("Main: started thread", i)
    #     threads.append(threading.Thread(target=thread_func, args=(i,)))
    #     threads[i].start()

    # for i in range(2,-1,-1):
    #     print("Main: waiting for thread", i)
    #     threads[i].join()
    #     print("Main: thread done", i)

    # print("main done")


    '''
    Using the same example above, we can spawn off multiple threads with a ThreadPoolExecutor.
    It is present in concurrent.futures package
    You can use the ThreadPoolExecutor using the 'with' statement and it runs as a context manager.
    It's better this way, because you won't forget to write join() as using it as context manager, 
    invokes join at the end of the execution of the block.
    It accepts max_workers parameter which is set to the number of workers you want in the pool.
    And then use map function to step through a iterable of objects to pass through in the given thread function.

    Also, make sure that the thread function you are calling doesn't have exceptions. 
    If it does, the main program silently ends and very difficult to troubleshoot.
    '''
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        #executor.map(thread_func, range(3))
        # another way to invoke threads is using submit function as below
        for i in range(3):
            executor.submit(thread_func, i)
    print("main done")
