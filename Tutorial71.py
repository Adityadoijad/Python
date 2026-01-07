#Regular Expression
import re

text='''I'm having a fine coding experience with my asus s15 oled laptop\nI have done basic c language and curently completing python and this is tutorial 71 about regular expresssion'''

'''
re.match():
checks for a match only at the beginning of the string.
Returns a match object if it matches; otherwise, it returns None.'''

search="I'm"
# search="a" 
result=re.match(search,text)
print(result)
print("\n")




'''
re.search():
It scans the entire string and returns the first match it finds.'''

search="and"
# search="aditya"
result=re.search(search,text)
print(result)
print("\n")



'''
re.findall():
It returns all matches of a pattern in a string as a list.'''
search="and"
result=re.findall(search,text)
print(result)
print("\n")




'''
re.sub():
It replaces parts of the string that match the pattern.'''
search="asus s15 oled laptop"
replace="Hp victus"
result=re.sub(search,replace,text)
print(result)
print("\n")


'''
re.split():
It splits the string by the occurrences of a pattern.
'''
result=re.split(r"\s+","Hello My Name Is Aditya ")
print(result)
print("\n")




'''
This is best example of regular expression
'''
text = "My email is adityadoijad29@example.com and adityadoijad001@example.org"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
print(emails)  # Outputs: ['test@example.com', 'contact@example.org']




#NOTE
'''
In Python, regular expressions (regex) are used for pattern matching in strings. 
They allow you to search, match, and manipulate text based on specific patterns.

Regular Expression Syntax (Special Characters):
.: Matches any character except newline.
re.search(r"h.llo", "hello")  # Matches 'hello'

^: Matches the beginning of a string.
re.match(r"^Hello", "Hello world")  # Matches 'Hello'

$: Matches the end of a string.
re.search(r"world$", "Hello world")  # Matches 'world'

*: Matches 0 or more occurrences of the preceding character.
re.search(r"he.*o", "hello")  # Matches 'hello'

+: Matches 1 or more occurrences of the preceding character.
re.search(r"he.+o", "hello")  # Matches 'hello'

?: Matches 0 or 1 occurrence of the preceding character.
re.search(r"he.?o", "heo")  # Matches 'heo'

[]: Used to define a set of characters to match.
re.search(r"h[aeiou]llo", "hello")  # Matches 'hello'

\d: Matches any digit (equivalent to [0-9]).
re.search(r"\d", "123abc")  # Matches '1'

\w: Matches any alphanumeric character (letters and digits) and underscores.
re.search(r"\w+", "Hello_123")  # Matches 'Hello_123'

\s: Matches any whitespace (space, tab, newline).
re.search(r"\s", "Hello world")  # Matches the space

{n}: Matches exactly n occurrences of the preceding character.
re.search(r"\d{3}", "1234")  # Matches '123'

|: Acts as an OR operator.
re.search(r"cat|dog", "I have a dog")  # Matches 'dog'

(): Groups part of the pattern.
re.search(r"(he|she)llo", "hello")  # Matches 'hello'
'''
