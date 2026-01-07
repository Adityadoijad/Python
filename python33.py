# Enumrate Function

marks=[1,2,3,4,5,6,7,8,9]

index=0
for mark in marks:
    print(mark)
    if(index == 3):
        print("it is boundry to pass")
    index+=1
print("\n")

for index,mark in enumerate(marks):
    print(mark)
    if(index == 3):
        print("it is boundry to pass")
print("\n")

fruits=["apple","mango","banana","pineapple","kiwi","cherry","strawberry"]
for index,fruit in enumerate(fruits,start=1):
    print(fruit)
    if(index==2):
        print("~~it's banana next~~")












#NOTE
'''
Enumerate function in python
The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time. Here's a basic example of how it works:

# Loop over a list and print the index and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(index, fruit)
The output of this code will be:

0 apple
1 banana
2 mango
As you can see, the enumerate function returns a tuple containing the index and value of each element in the sequence. You can use the for loop to unpack these tuples and assign them to variables, as shown in the example above.

Changing the start index
By default, the enumerate function starts the index at 0, but you can specify a different starting index by passing it as an argument to the enumerate function:

# Loop over a list and print the index (starting at 1) and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
This will output:

1 apple
2 banana
3 mango
The enumerate function is often used when you need to loop over a sequence and perform some action with both the index and value of each element. For example, you might use it to loop over a list of strings and print the index and value of each string in a formatted way:

fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(f'{index+1}: {fruit}')
This will output:

1: apple
2: banana
3: mango
In addition to lists, you can use the enumerate function with any other sequence type in Python, such as tuples and strings. Here's an example with a tuple:

# Loop over a tuple and print the index and value of each element
colors = ('red', 'green', 'blue')
for index, color in enumerate(colors):
    print(index, color)
And here's an example with a string:

# Loop over a string and print the index and value of each character
s = 'hello'
for index, c in enumerate(s):
    print(index, c)
'''
    
