import concurrent.futures
import requests
import os

def downloadfile(url, name):
    print(f"Started downloading {name}")
    response = requests.get(url)
    print(f"Finished downloading {name}")
    
    # Create a directory if it doesn't exist
    os.makedirs(r"D:\Aditya\Python\Python Tutorials\files2", exist_ok=True)
    
    # Save the file
    with open(f"D:\\Aditya\\Python\\Python Tutorials\\files2\\{name}.jpg", "wb") as f:
        f.write(response.content)

if __name__ == '__main__':
    url = "https://picsum.photos/500/500"

    # Use ThreadPoolExecutor for I/O bound tasks
    with concurrent.futures.ProcessPoolExecutor() as executor:
        l1 = [url for _ in range(50)]
        l2 = [i for i in range(50)]
        
        # Avoid naming conflict with 'requests'
        results = executor.map(downloadfile, l1, l2)
        
        for _ in results:
            pass  # No need to print anything; just iterate to ensure completion




#NOTE
'''
Python’s multiprocessing module allows the execution of multiple processes simultaneously, leveraging multiple CPU cores to achieve parallelism. 
It helps overcome the limitations of the Global Interpreter Lock (GIL), which restricts the execution of multiple threads in CPython.


Why Use multiprocessing?
GIL Limitation: Threads in Python are limited by the GIL, making true parallel execution impossible for CPU-bound tasks. multiprocessing bypasses this by using separate processes.
Parallel Execution: Great for CPU-bound tasks like numerical computations or video processing.
Process Isolation: Each process has its memory space, which prevents data corruption.


'''