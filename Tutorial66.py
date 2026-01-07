#walrus operator (:=)

a=True
print(a:=False)

print("\n")

numbers=[1,2,3,4,5]
while(n:=len(numbers)) >0:
    print(numbers.pop())

print("\n")

names=["aditya","Ankosh","doijad"]
if name:=input("Enter the name : ") in names:
    print(f"Hello , {name}!")
else:
    print("no name found")


foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)



#NOTE
'''
The walrus operator (:=) is a feature introduced in Python 3.8. It allows you to assign a value to a variable as part of an expression. 
The main benefit of the walrus operator is that it enables both assignment and evaluation within the same statement, making code more concise.

Key Benefits:
-Reduces the need to calculate or call functions multiple times.
-Allows compact, readable loops or conditions.
-Improves code clarity by keeping the logic in one place.
'''