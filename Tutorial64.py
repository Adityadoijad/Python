# Hiearchial Inheritance
'''
         Parent
        /     \
      /        \
   Child1      Child2
'''

class Vehicle:
    def engine(self):
        print("This vehicle has engine")

class Bike(Vehicle):
    def type(self):
        print("It is a Bike")

class Car(Vehicle):
    def type(self):
        print("It is a Car")

b=Bike()
b.engine()
b.type()

print("\n")

c=Car()
c.engine()
c.type()



#NOTE
'''
Hierarchical inheritance in Python refers to a type of inheritance where multiple child classes inherit from a single parent class. 
Each child class can have its own methods, but they all share the attributes and methods of the parent class.
'''
