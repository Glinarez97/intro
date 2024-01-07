#import

# global vars
name = "Gerardo"

# functions 
def print_header():
    print("------------")
    print(" Test 2 ")
    print("------------")
    print("- by:" + name)
    print("------------")

def multiply(num1, num2):
    total = num1 * num2
    print("the result is:" + str(total))


def devide(num1, num2):
    if num2 == 0:
        print("Error: Zero division not allowed")
    else:
        total = num1 / num2 
        print("The total is: " + str(total))





#plane instructions 
# function calls


print_header()


multiply(8, 78)
multiply(873, 7224548)

devide(10, 2)
devide(2, 2)
devide(2, 0)