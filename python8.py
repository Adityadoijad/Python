# STRING METHODS

a="ADITYA"
print(a.upper())
# ADITYA
print(a.lower())
# aditya
print("\n")

b= "       this is an python program      "
print(b.strip())
# this is an python program
print(len(b))
# 38
print(len(b.strip()))
# 25
print("\n")

c="this is an python program~~~~~~~~~~~~~"
print(c.rstrip("~"))
# this is an python program
print("\n")

d="Hello my name is aditya"
print(d.replace("aditya","Kittu"))
# Hello my name is Kittu
print("\n")

e="we have to   split this   program"
print(e.split("   "))
# ['we have to', 'split this', 'program']
print("\n")

f="this is introduction to python"
print(f.capitalize())
# This is introduction to python
print("\n")

g="welcome to python"
print(g.capitalize().center(50))
                # Welcome to python
print(g.capitalize().center(50,"~"))
# ~~~~~~~~~~~~~~~~Welcome to python~~~~~~~~~~~~~~~~~
print("\n")

h="this string method is used to find number of words in a string for example my book is on the table that is also a book shelf"
print(h.count("is"))
# 4
print("\n")

i="true will be executed if the endinf word in the string is zero"
print(i.endswith("zero"))  # True
print(i.endswith("is"))  #False
print(i.endswith("string",3,13)) #False
print("\n")


j="this is to use find string method to find if there is anime word in the string"
print(j.find("anime")) #54
print("\n")

k="thIs COde is wRitTEN is diFFereNT CaSES "  
#  THiS coDE IS WrITten IS DIffEREnt cAses
print(k.swapcase())
print("\n")


l="this is my new book "
print(l.title())
# This Is My New Book
print("\n")

m="python is easy to understand"
print(m.startswith("python")) #True
print("\n")




















# NOTES
'''
String methods
Python provides a set of built-in methods that we can use to alter and modify the strings.
There are total 22 methods given below :-

1 .upper() :
The upper() method converts a string to upper case.

Example:
str1 = "AbcDEfghIJ"
print(str1.upper())

Output:
ABCDEFGHIJ





2 .lower()
The lower() method converts a string to lower case.

Example:
str1 = "AbcDEfghIJ"
print(str1.lower())

Output:
abcdefghij





3 .strip() :
The strip() method removes any white spaces before and after the string.

Example:
str2 = " Silver Spoon "
print(str2.strip)

Output:
Silver Spoon






4 .rstrip() :
the rstrip() removes any trailing characters. Example:

str3 = "Hello !!!"
print(str3.rstrip("!"))

Output:
Hello





5. replace() :
The replace() method replaces all occurences of a string with another string. Example:

str2 = "Silver Spoon"
print(str2.replace("Sp", "M"))

Output:
Silver Moon







6. split() :
The split() method splits the given string at the specified instance and returns the separated strings as list items.

Example:
str2 = "Silver Spoon"
print(str2.split(" "))      #Splits the string at the whitespace " ".

Output:
['Silver', 'Spoon']
There are various other string methods that we can use to modify our strings.






6. capitalize() :
The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.

Example:
str1 = "hello"
capStr1 = str1.capitalize()
print(capStr1)
str2 = "hello WorlD"
capStr2 = str2.capitalize()
print(capStr2)

Output:
Hello
Hello world






7. center() :
The center() method aligns the string to the center as per the parameters given by the user.

Example:
str1 = "Welcome to the Console!!!"
print(str1.center(50))

Output:
            Welcome to the Console!!!

We can also provide padding character. It will fill the rest of the fill characters provided by the user.

Example:
str1 = "Welcome to the Console!!!"
print(str1.center(50, "."))

Output:
............Welcome to the Console!!!.............






8. count() :
The count() method returns the number of times the given value has occurred within the given string.

Example:
str2 = "Abracadabra"
countStr = str2.count("a")
print(countStr)

Output:
4









9. endswith() :
The endswith() method checks if the string ends with a given value. If yes then return True, else return False.

Example :
str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))

Output:
True

We can even also check for a value in-between the string by providing start and end index positions.

Example:
str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

Output:
True










11. find() :
The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.

Example:
str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))

Output:
10

As we can see, this method is somewhat similar to the index() method. The major difference being that index() raises an exception if value is absent whereas find() does not.

Example:
str1 = "He's name is Dan. He is an honest man."
print(str1.find("Daniel"))

Output:
-1









12. index() :
The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.

Example:
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))

Output:
13

As we can see, this method is somewhat similar to the find() method. The major difference being that index() raises an exception if value is absent whereas find() does not.

Example:
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Daniel"))

Output:
ValueError: substring not found












13. isalnum() :
The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.

Example 1:
str1 = "WelcomeToTheConsole"
print(str1.isalnum())

Output:
True










14. isalpha() :
The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.

Example :
str1 = "Welcome"
print(str1.isalpha())

Output:
True











15. islower() :
The islower() method returns True if all the characters in the string are lower case, else it returns False.

Example:
str1 = "hello world"
print(str1.islower())

Output:
True


16. isprintable() :
The isprintable() method returns True if all the values within the given string are printable, if not, then return False.

Example :
str1 = "We wish you a Merry Christmas"
print(str1.isprintable())

Output:
True








17. isspace() :
The isspace() method returns True only and only if the string contains white spaces, else returns False.

Example:
str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())

Output:
True
True








18. istitle() :
The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.

Example:
str1 = "World Health Organization" 
print(str1.istitle())

Output:
True

Example:
str2 = "To kill a Mocking bird"
print(str2.istitle())

Output:
False











19. isupper() :
The isupper() method returns True if all the characters in the string are upper case, else it returns False.

Example :
str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())

Output:
True










20. startswith() :
The endswith() method checks if the string starts with a given value. If yes then return True, else return False.

Example :
str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

Output:
True








21. swapcase() :
The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.

Example:
str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

Output:
pYTHON IS A iNTERPRETED lANGUAGE







22. title() :
The title() method capitalizes each letter of the word within the string.

Example:
str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())

Output:
He'S Name Is Dan. Dan Is An Honest Man.


 
'''