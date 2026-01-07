# Hybrid 
class A:
    def get_A(self):
        print("this is class A")

class B(A):
    def get_B(self):
        print("this is class B")

class C(B):
    def get_C(self):
        print("this is class C")

class D(A):
    def get_D(self):
        print("this is class D")

class E(C,D):
    def get_E(self):
        print("this is class E")


e=E()
e.get_A()
e.get_B()
e.get_C()
e.get_D()
e.get_E()

print(E.mro())

# Flowchart Representation of Hybrid Inheritance:

#         A
#       /   \
#      B     D
#      |     |
#      C     |
#       \   /
#         E


#NOTE
'''
Hybrid inheritance in Python is a combination of two or more types of inheritance (single, multiple, multilevel, hierarchical) used together. 
It aims to leverage the benefits of these inheritance types while avoiding ambiguity, particularly in cases of multiple inheritance.

'''