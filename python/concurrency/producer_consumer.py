'''
Producer: reads data from network and writes to disk. It accepts messages that many come in regular interval or in burst.
Consumer: once the data is there, it reads it and save it in database. Database access is slow but it keeps up speed
with regular flow of data, but it's not fast enough to keep pace if the data comes in burst.

You will learn here usage of:
threading.Lock
concurrent.futures.ThreadPoolExecutor
queue.Queue (thread-safe)
threading.Event: it allows one thread to signal an event while many other threads are waiting for that event to happen.

Reference: https://realpython.com/intro-to-python-threading/

First, we tried to set/read from a single message value and then we are using the thread-safe Queue class in Python
to store multiple values instead of a single one.
'''

import random
import threading
import concurrent.futures
import queue
import time

class MessageQueue(queue.Queue):
    def __init__(self):
        super().__init__(maxsize=10)

        # self.message = ""
        # self.producer_lock = threading.Lock()
        # self.consumer_lock = threading.Lock()

        # consumer lock is acquired during initialization as consumer can't read unless produces writes
        #self.consumer_lock.acquire()
        
    
    def set_message(self, message):
        print("About to add in queue. Message: ", message)
        self.put(message)
        print("Added in queue. Message: ", message)
        # self.producer_lock.acquire()
        # print("Producer acquired the producer lock")
        # self.message = message
        # self.consumer_lock.release()
        # print("Producer released the consumer lock. Message written: ", message)
    
    def read_message(self):
        print("About to read from queue")
        message = self.get()
        print("Read from queue. Message: ", message)

        # print("Consumer acquired the consumer lock")
        # self.consumer_lock.acquire()
        # message = self.message
        # self.producer_lock.release()
        # print("Consumer released the producer lock. Message read: ", message)
        return message


def producer(dataQueue, event):
    while not event.is_set():
        message = random.randint(1, 101)
        print("Producer received message: ", message)
        dataQueue.set_message(message)

    print("Producer received an event. Exiting")

def consumer(dataQueue, event):
    message = 0
    while not event.is_set() or not dataQueue.empty():
        message = dataQueue.read_message()
        print("Consumer read message: ", message, ". Queue size: ", dataQueue.qsize())

    print("Consumer consumed all messages. Exiting")


if __name__ == "__main__":
    dataQueue = MessageQueue()
    event = threading.Event()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, dataQueue, event)
        executor.submit(consumer, dataQueue, event)

        time.sleep(0.1)
        print("Main: about to set an event")
        event.set()