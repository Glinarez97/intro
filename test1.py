# these are variables 

name = "Gerardo"
last_name = "Linarez"
age = 37
price = 12.99
found = True 

print(name)
print(last_name)

# math 
total = 21 + 21
print(total)

# if
if  age  < 100:
    print("dont worry you are young!")
    print("inside the if")
    print("me too")

print("im outside")

# exc 1;
# create an if, if the age is lower than 21
# show a message like "you can not drink alcohol"

if age < 21:
    print("you can not drink alcohol")

if age >= 21:
    print("enjoy youre beer!")

# define function 
    
def say_hello():
    print("hello there!")

# call function
say_hello()
say_hello()
say_hello()

def salute(name):
    print("hi " + name)

salute("john")
salute("jane")
salute(name)

def sum(num1, num2):
    result = num1 + num2
    print("the result is " + str(result))

sum(21, 21)
sum(1243, 3532)