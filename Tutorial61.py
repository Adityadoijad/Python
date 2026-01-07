# Multiple Inheritance

class Company:
    def __init__(self,name):
        self.name=name

    def show(self):
        print(f"The company name is {self.name}")#1

class Processor:
    def __init__(self,processor_name):
        self.processor_name=processor_name
    def show(self):
        print(f"The processer is {self.processor_name}")#2

class Laptop(Company,Processor): # If i swap both parameters then #2 will be printed in a.show function
    def __init__(self, name ,processer_name):
        self.name=name
        self.processor_name=processer_name

a=Laptop("Asus","Intel")
print(a.name)
print(a.processor_name)
a.show()
print(Laptop.mro())







#NOTE
'''
Multiple Inheritance in Python
Multiple inheritance is a powerful feature in object-oriented programming that allows a class to inherit attributes and methods from multiple parent classes. This can be useful in situations where a class needs to inherit functionality from multiple sources.

Syntax
In Python, multiple inheritance is implemented by specifying multiple parent classes in the class definition, separated by commas.

class ChildClass(ParentClass1, ParentClass2, ParentClass3):
    # class body
In this example, the ChildClass inherits attributes and methods from all three parent classes: ParentClass1, ParentClass2, and ParentClass3.

It's important to note that, in case of multiple inheritance, Python follows a method resolution order (MRO) to resolve conflicts between methods or attributes from different parent classes. The MRO determines the order in which parent classes are searched for attributes and methods.

Example
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")
        
class Mammal:
    def __init__(self, name, fur_color):
        self.name = name
        self.fur_color = fur_color
        
class Dog(Animal, Mammal):
    def __init__(self, name, breed, fur_color):
        Animal.__init__(self, name, species="Dog")
        Mammal.__init__(self, name, fur_color)
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")
In this example, the Dog class inherits from both the Animal and Mammal classes, so it can use attributes and methods from both parent classes.
'''