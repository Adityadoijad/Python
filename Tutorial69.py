#generators in python
import time

'''creating loop using generator'''
def gen():
 for i in range(100):
    yield i

gen = gen()

def using_generator():
 for j in gen:
   print(j)

init=time.time()
using_generator()
t3=time.time()-init
print(f"This is time taken for for loop : {t3} sec")

'''fibonachi by using generator'''
print("\n")

def fibonacci():
  a,b=0,1
  while True:
    yield a
    a=b
    b=a+b

fib=fibonacci()

for _ in range(10):
  print(next(fib))

print("\n")

gen=(x**2 for x in range (5))

for i in gen:
  print(i)





#NOTE
'''
In Python, generators are a simple way to create iterators. However, unlike normal functions that return a value and then exit, generators yield values one at a time, pausing after each yield and resuming where they left off when called again. This allows you to iterate over potentially large datasets without needing to store the entire dataset in memory, making them more memory-efficient.

Key Concepts of Generators:
yield keyword: Instead of using return to return a result, a generator function uses yield to produce a value and pause its execution. The next time the generator is called, it resumes execution right after the yield statement.
Stateful Iteration: When a generator yields a value, it maintains its state. The next iteration resumes exactly where the generator left off.
Lazy Evaluation: Generators generate values on the fly, which is useful for large datasets or infinite sequences.


Advantages of Generators:
Memory efficiency: Generators don’t need to store the entire sequence in memory, they generate items one at a time.
Performance: For large datasets, generators can be much faster than list-based solutions.
Infinite sequences: You can model infinite sequences with generators, something not possible with lists.
'''







