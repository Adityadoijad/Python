# IF ELSE STATEMENTS
a=int(input("Enter your age : "))
print("your age is ",a)

if(a>18):
    print("you can vote")
else:
    print("you cannot vote")

# IF ELIF STATEMENT
b=int(input("enter the value of integer : "))

if(b>0):
    print("it is a positive number")
elif(b<0):
    print("it is a negative number")
else:
    print("the number is zero")


# NESTED IF STATEMENT
print(" RED = 1 \n YELLOW = 2 \n GREEN = 3\n")
c=int(input("Enter the colour : "))

if(4>c>0):
    if(c==1):
        print("Stop")
    elif(c==2):
        print("Wait")
    else:
        print("Go")
else:
    print("invalid number selected")



























#notes
'''
Conditional operators 
>, <, >=, <=, ==, !=
print(a>18)
print(a<=18)
print(a==18)
print(a!=18)







Based on this, the conditional statements are further classified into following types:

if
if-else
if-else-elif
nested if-else-elif. 

# if-else Statements
Sometimes the programmer needs to check the evaluation of certain expression(s), whether the expression(s) evaluate to True or False. If the expression evaluates to False, then the program execution follows a different path than it would have if the expression had evaluated to True.

An if……else statement evaluates like this:
if the expression evaluates True:
Execute the block of code inside if statement. After execution return to the code out of the if……else block.\

if the expression evaluates False:
Execute the block of code inside else statement. After execution return to the code out of the if……else block.

Example:
applePrice = 210
budget = 200
if (applePrice <= budget):
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")

Output:
Alexa, do not add Apples to the cart. 












#if elif
The if-elif statement is shortcut of if..else chain. While using if-elif statement at the end else block is added which is performed if none of the above if-elif statement is true.

num = int(input("Enter the value of num: "))
if (num < 0):
  print("Number is negative.")
elif (num == 0):
  print("Number is Zero.")
elif (num == 999):
  print("Number is Special.")
else:
  print("Number is positive.")

print("I am happy now")














#nested if
if statement can also be checked inside other if statement. This conditional statement is called a nested if statement. This means that inner if condition will be checked only if outer if condition is true and by this, we can see multiple conditions to be satisfied.


num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")










'''