import os
# 1
if not os.path.exists("data"):
    os.mkdir("data")    #used to create folder named data

for i in range(0,100):
    os.mkdir(f"data/folder{i+1}")      #used to create folder from 1-100





# 2
# used to list folders name
folders=os.listdir("data")

for i in folders:
    print(i)
    print(os.listdir(f"data/{i}"))   #used to find what is inside the folder


#used to find location of current working directory
cwd = os.getcwd() 
print("Current working directory:", cwd) 








# 3
#used to change name of them all at a time
for i in range(0,100):
    os.rename(f"data/folder{i+1}",f"data/Folder {i+1}")  




#NOTE
'''
os Module in Python
The os module in Python is a built-in library that provides functions for interacting with the operating system. It allows you to perform a wide variety of tasks, such as reading and writing files, interacting with the file system, and running system commands.

Here are some common tasks you can perform with the os module:

Reading and writing files The os module provides functions for opening, reading, and writing files. For example, to open a file for reading, you can use the open function:

import os
# Open the file in read-only mode
f = os.open("myfile.txt", os.O_RDONLY)
# Read the contents of the file
contents = os.read(f, 1024)
# Close the file
os.close(f)
To open a file for writing, you can use the os.O_WRONLY flag:

import os
# Open the file in write-only mode
f = os.open("myfile.txt", os.O_WRONLY)
# Write to the file
os.write(f, b"Hello, world!")
# Close the file
os.close(f)
Interacting with the file system
The os module also provides functions for interacting with the file system. For example, you can use the os.listdir function to get a list of the files in a directory:

import os
# Get a list of the files in the current directory
files = os.listdir(".")
print(files)  # Output: ['myfile.txt', 'otherfile.txt']
You can also use the os.mkdir function to create a new directory:

import os
# Create a new directory
os.mkdir("newdir")
Running system commands
Finally, the os module provides functions for running system commands. For example, you can use the os.system function to run a command and get the output:

import os
# Run the "ls" command and print the output
output = os.system("ls")
print(output)  # Output: ['myfile.txt', 'otherfile.txt']
You can also use the os.popen function to run a command and get the output as a file-like object:

import os
# Run the "ls" command and get the output as a file-like object
f = os.popen("ls")
# Read the contents of the output
output = f.read()
print(output)  # Output: ['myfile.txt', 'otherfile.txt']
# Close the file-like object
f.close()
In summary, the os module in Python is a built-in library that provides a wide variety of functions for interacting with the operating system. It allows you to perform tasks such as reading and writing files, interacting with the file system, and running system commands.
'''