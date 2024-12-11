'''
Follow-up of producer_consumer.py.
No need of a MessageQueue class. Can directly use queue
'''

import random
import threading
import concurrent.futures
import queue
import time


def producer(dataQueue, event):
    while not event.is_set():
        message = random.randint(1, 101)
        print("Producer received message: ", message)
        dataQueue.put(message)

    print("Producer received an event. Exiting")

def consumer(dataQueue, event):
    while not event.is_set() or not dataQueue.empty():
        message = dataQueue.get()
        print("Consumer read message: ", message, ". Queue size: ", dataQueue.qsize())

    print("Consumer consumed all messages. Exiting")


if __name__ == "__main__":
    dataQueue = queue.Queue(maxsize=10)
    event = threading.Event()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, dataQueue, event)
        executor.submit(consumer, dataQueue, event)

        time.sleep(0.01)
        print("Main: about to set an event")
        event.set()