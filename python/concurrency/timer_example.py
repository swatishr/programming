'''
Timer (threading.Timer) is a construct in Python that helps you kick off a thread after a specified duration.
It creates a timer thread that starts when you call start() and runs the function after the specified time.

Timer can be cancelled before it's scheduled by calling .cancel() on the timer.

Usage:
- Delaying the execution of a function.
- Scheduling tasks with a delay in simple scenarios.
- Implementing lightweight time-based actions (e.g., reminders, notifications).
'''

import time
import threading
import random

def scheduledFunc(name, duration):
    print(f"Hello, Timer {name} after duration {duration}s! the current time is {time.strftime('%H:%M:%S')}")

if __name__ == "__main__":
    
    timers = []
    for i in range(5):
        seconds = random.randint(1, 10)
        timers.append(threading.Timer(seconds, scheduledFunc, args=(i,seconds,)))
    
    print(f"Current time is {time.strftime('%H:%M:%S')} before timers start")
    for i in range(5):
        timers[i].start()

    for i in range(5):
        timers[i].join()

    print("All timers done with execution")