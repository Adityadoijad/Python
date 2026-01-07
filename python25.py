# SET methods
'''
1) union()
>>>> creates a new set with the unique elements from both the sets'''
a= {1,3,5,3,0,True}
b={"adi",3,9.98,"location"}
c=a.union(b)
print(c,"\n")




'''
2)update()
>>>> applied on a set itself and it also adds unique elements from the both the sets into one of the sets'''
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.update(cities2)
print(cities,"\n")


'''
3)intersection()
>>>> creates a new set with the common elements from both the sets
'''
d=a.intersection(b)
print(d,"\n")



'''
4)intersection_update()
>>>> applied on a set itself and it also contains the common elements from both the sets
'''
cities3 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities4 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3.intersection_update(cities4)
print(cities3,"\n")



'''
5)symmetric_difference()
>>>>  creates a new set with the elements from the both the sets that are not common in between
'''
var={"a","b","c","d"}
var1={"a","c","e","f"}
var3=var.symmetric_difference(var1)
print(var3,"\n")



'''
6)symmetric_diffrence_update()
>>>> applied on a set itself and it contains elements from the sets that are not common in between
'''
cities5 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities6 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities5.symmetric_difference_update(cities6)
print(cities5,"\n")



'''
7)difference()
>>>> creates a new set with the elements from a single set that are not common 

8) difference_update()
>>>> applied on a set itself and contains elements of a set that are not common
'''
var4=var.difference(var1)
print(var4,"\n")

var1.difference_update(var)
print(var1,"\n")




'''
9)isdisjoint()
>>>> The isdisjoint() method checks if items of given set are present in another set. 
     This method returns False if items are present, else it returns True.
'''
print(var.isdisjoint(var1))
print(var.isdisjoint(a))
print("\n")



'''
10)issuperset():
>>>> The issuperset() method checks if all the items of a particular set are present in the original set. 
     It returns True if all the items are present, else it returns False.

11)issubset():
>>>> The issubset() method checks if all the items of the original set are present in the particular set. 
     It returns True if all the items are present, else it returns False.
'''
x={1,2,3,4,5,"tokyo","gadchiroli","nagpur"}
y={3,5,"tokyo"}
print(x.issuperset(y))
print(y.issubset(x),"\n")




'''
12)add()
>>>> If you want to add a single item to the set use the add() method.
'''
y.add("berlin")
print(y,"\n")




'''
13)remove()
>>>> It is used to remove an item from set
     If we try to remove an item absent in given set it throws error

14)discard()
>>>> It is same as remove but it don't throw error when we try to remove an item absent in given set
'''
x.remove("gadchiroli")
print(x)
print("\n")

x.discard("tokyo")
x.discard("man")     #not present in set
print(x,"\n")


'''
15)pop()
>>>> This method removes the last item of the set but the catch is that we don't know which item gets popped as sets are unordered. 
     However, you can access the popped item if you assign the pop() method to a variable.
'''
print(x.pop())


'''
16)del
>>>> del is not a method, rather it is a keyword which deletes the set entirely.

example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
print(cities)

output:
throws error
'''



'''
17)clear():
>>>> This method clears all items in the set and prints an empty set.
'''
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities,"\n")




'''
18)Check if item exists
'''
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")