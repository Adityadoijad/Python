#Dictonaries
info={'name':'Aditya','age':19,'branch':"AI",'eligible':True}
print(info)
print(info['age'])
print(info.get('name'))
print(info.keys())
print(info.values())

for keys in info.keys():
    print(keys)
print("\n")

for values in info.values():
    print(values)
print("\n")

for keys,values in info.items():
    print(f"The value corresponding to key {keys} is {values}")

print(info.get('unmatched_element')) # in get function if element is unmatched none is o/p
print(info('unmatched_element'))  # if only info index is used to find unmatched element error is thrown






#NOTE
'''
Accessing Dictionary items:
I. Accessing single values:
Values in a dictionary can be accessed using keys. We can access dictionary values by mentioning keys either in square brackets or by using get method.

Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])
print(info.get('eligible'))
Output:
Karan
True



II. Accessing multiple values:
We can print all the values in the dictionary using values() method.

Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())
Output:
dict_values(['Karan', 19, True])



III. Accessing keys:
We can print all the keys in the dictionary using keys() method.

Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())
Output:
dict_keys(['name', 'age', 'eligible'])



IV. Accessing key-value pairs:
We can print all the key-value pairs in the dictionary using items() method.

Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())
Output:
dict_items([('name', 'Karan'), ('age', 19), ('eligible', True)])
'''