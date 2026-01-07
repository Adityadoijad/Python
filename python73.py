# Multithreading
import threading
import time
from concurrent.futures import ThreadPoolExecutor

def print_num():
    for i in range(5):
        print(i+1)
        time.sleep(1)

def print_letter():
    for letter in 'ABCDE':
        print(letter)
        time.sleep(1)

t1=threading.Thread(target=print_num)
t2=threading.Thread(target=print_letter)

t1.start()
t2.start()

t1.join()
t2.join()

print("finished")


def func(seconds):
    print(f"waiting {seconds} seconds")
    time.sleep(seconds)
    print(f"waited for {seconds} seconds")
    return seconds

def pooldemo():
    with ThreadPoolExecutor() as executor:
        l=[5,4,2,6,1]
        result =executor.map(func,l)
        for results in result:
            print(results)

pooldemo()

#NOTE
'''
Multithreading is a programming concept that allows multiple threads (smaller units of a process) to run concurrently within a single process. 
Threads share the same memory space and can help perform tasks simultaneously, making programs faster and more responsive.


>>>Key Concepts<<<
Thread: A lightweight process that can run concurrently with other threads in the same application.
Concurrency: Multiple threads working on separate tasks but within the same program.
Parallelism: Tasks executed simultaneously on multiple CPU cores.


>>>Advantages of Multithreading<<<
Improved Performance: Tasks can execute concurrently, utilizing multiple CPU cores effectively.
Responsiveness: Long-running tasks (e.g., I/O operations) don't block the entire application.
Resource Sharing: Threads share the same memory and resources, reducing overhead.
Efficient Utilization: Makes better use of CPU resources during idle times.


>>>Disadvantages<<<
Complexity: Writing, debugging, and maintaining multithreaded code is more challenging.
Synchronization Issues: Threads sharing resources may lead to data inconsistencies or race conditions.
Overhead: Context switching between threads can add overhead.
'''