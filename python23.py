# Recursion
print("Factorial of a number")
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)


n=int(input("Number: "))
print("Factorial:",fact(n))
print("\n")



print("Fibonacci Series")
def fibo(m):
    if(m==0):
        return 0
    elif(m==1):
        return 1
    else:
        return fibo(m-1)+fibo(m-2)
    
m=int(input("Number: "))
print("Fibonacci series:",fibo(m))











#NOTE
'''Recursion in python
Recursion is the process of defining something in terms of itself.

Python Recursive Function
In Python, we know that a function can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursive functions.

Example:
def factorial(num): 
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1)) 
  
# Driver Code 
num = 7; 
print("Number: ",num)
print("Factorial: ",factorial(num))


Output:
number:  7
Factorial:  5040
'''