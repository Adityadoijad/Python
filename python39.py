#readline() and writeline() function 


#writeline fucntion
f=open("Tutorial39.txt","w")
lines=("line 1\n","line 2\n","line 3\n")
f.writelines(lines)
f.close()





#readlines function
f = open("Tutorial39one.txt", "r")
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()



f=open("Tutorial39x.txt","r")
i=0
while True:
    i=i+1
    lines=f.readline()
    if not lines:
        break
    m1=int(lines.split(",")[0])
    m2=int(lines.split(",")[1])
    m3=int(lines.split(",")[2])
    
    print(f"The marks of {i} in english is {m1}")
    print(f"The marks of {i} in maths is {m2}")
    print(f"The marks of {i} in sst is {m3}")
    print()
f.close()





#NOTE
'''
readlines() method
The readline() method reads a single line from the file. If we want to read multiple lines, we can use a loop.

f = open('myfile.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)
The readlines() method reads all the lines of the file and returns them as a list of strings.

writelines() method
The writelines() method in Python writes a sequence of strings to a file. The sequence can be any iterable object, such as a list or a tuple.

Here's an example of how to use the writelines() method:

f = open('myfile.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()
This will write the strings in the lines list to the file myfile.txt. The \n characters are used to add newline characters to the end of each string.

Keep in mind that the writelines() method does not add newline characters between the strings in the sequence. If you want to add newlines between the strings, you can use a loop to write each string separately:

f = open('myfile.txt', 'w')
lines = ['line 1', 'line 2', 'line 3']
for line in lines:
    f.write(line + '\n')
f.close()
It is also a good practice to close the file after you are done with it.
'''
