#MANIPULATING TUPLES

tup = ("Aditya","ankosh","doijad")
temp=list(tup)
temp.append("Hello")
temp.pop(1)
temp[1]="Doijad"
tup=tuple(temp)
print(tup)
tup1 = ("Asus","vivobook","s15")
combined_tuple=tup+tup1
print(combined_tuple)

print("\n")

#TUPLE METHODS
tup3=(1,2,3,0,3,4,5,3,6,7,3,1.2,9)
print(tup3.count(3))
print(tup3.index(3,3,8))





