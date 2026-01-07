#Break Statement
''' break statement
The break statement enables a program to skip over a part of the code. 
A break statement terminates the very loop it lies within.'''

i=0
for i in range(20):
    print("5 X ",i+1," = ",5*(i+1))
    if(i==9):
     break
print("loop skipped")

print("\n")

#Continue Statement
''' Continue Statement
The continue statement skips the rest of the loop statements and causes 
the next iteration to occur.''' 

for i in range(15):
  if(i==9):
    print("itration skipped")
    continue
  print("5 X ",i+1," = ",5*(i+1))
   