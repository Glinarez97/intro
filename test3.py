

def say_hello(name, age):
    print("Hi " + (name) + ", so you are " + str(age) + "years old")
    # F string
    print(f"Hi {name}, so you are {age} years old")

def formart_address(street, number, city, zip):
    print(f"Please return to street: {street} #{number}; city: {city}, zip: {zip}")

def list_1():
    names = ["Tyrell", "Gerardo", "Reheim", "Morris"]
    print(names)

    print(len(names)) # len = length

# add elements to list
    names.append("Gerardo")
    print(names)

# remove elements
    names.remove("Gerardo")
    print(names)

    # foor loop
    for name in names:
        print(name)

def get_total():
    prices = [123, 234, 45, 12, 84, 123, 672, 787, 173, 51, 687, 146, 613, 6, 135]



    total = 0
    for price in prices:
        print(price)
        total = total + price

    print(f"The total is: {total}")

def test_list_3():
    student_ages = [20, 29, 53, 65, 27, 35, 51, 45, 74, 46, 27, 20, 32, 47, 33, 27]

    print(len(student_ages))

    for age in student_ages:
        if age > 30:
            print(age)



say_hello("john", 25)
say_hello("jane", 31)

print("--------------")


formart_address("avergreen", 25, "Springfield", 92384)

print("-------------")
list_1()


print("-----------")
get_total()

print("---------")
test_list_3()