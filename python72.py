#AsyncIO in Python

import asyncio

async def Task1():
    print("Task 1 Started")
    await asyncio.sleep(4)
    print("Task 1 Completed")

async def Task2():
    print("Task 2 Started")
    await asyncio.sleep(1)
    print("Task 2 Completed")

async def Task3():
    print("Task 3 Started")
    await asyncio.sleep(3)
    print("Task 3 Completed")

async def main():
    await asyncio.gather(Task1(),Task2(),Task3())

asyncio.run(main())

print("\n")



async def countdown(n):
    while n>0:
        print(f"Counting Down: {n}")
        await asyncio.sleep(1)
        n=n-1

async def main():
    task=asyncio.create_task(countdown(5))

    print("Task started")
    await task
    print("Task finished")
asyncio.run(main())


#NOTE
'''
asyncio is a Python library used for writing concurrent code using the async and await keywords. 
It is used to handle asynchronous I/O operations such as network requests, file I/O, or tasks that require waiting. 
Instead of creating new threads or processes, asyncio uses an event loop that schedules and executes tasks in an efficient manner.

Why Use asyncio?
Improves Performance: Helps handle I/O-bound tasks concurrently.
Non-blocking: Allows running multiple tasks without waiting for each to complete.
Efficient: Uses a single-threaded approach, reducing the overhead of thread management.



Core Concepts of asyncio
Coroutines: These are functions defined with async def. They are the building blocks of asynchronous programs.
Event Loop: This is the core of asyncio. It runs the coroutines and handles the asynchronous execution.
Tasks: Tasks are used to schedule the execution of coroutines in the event loop.
Await: The await keyword is used to pause the coroutine until the awaited task is completed.

Key Points to Remember
Define Coroutines: Use async def to define an asynchronous function.
Use await: Use the await keyword to pause and resume coroutines without blocking the program.
Event Loop: asyncio.run() manages the event loop automatically.
Concurrency with gather(): Run multiple coroutines concurrently using asyncio.gather().

'''