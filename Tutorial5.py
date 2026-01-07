# Taking input from user
a=input("enter your name : ")
print("your name is ",a)

x=input("enter first no. ")
y=input("enter second no. ")
print(x+y)

print(int(x)+int(y))





























#NOTES
'''
Taking User Input in python
In python, we can take user input directly by using input() function.This input function gives a return value as string/character hence we have to pass that into a variable

Syntax:
variable=input()


But input function returns the value as string. Hence we have to typecast them whenever required to another datatype.

Example:
variable=int(input())
variable=float(input())


We can also display a text using input function. This will make input() function take user input and display a message as well

Example:
a=input("Enter the name: ")
print(a)


Output:
Enter the name: Harry
Harry
'''