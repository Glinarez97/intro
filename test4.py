
def about_me():
    # dectionary
    me = {
        "name": "Gerardo",
        "last": "Linarez",
        "age": 37
    }
    

    print(me)

    # read values
    print(me["name"])
    print(me["age"])

    #add new elements
    me["email"] = "glinarez97@gmail.com"
    print(me)


    # update exisiting
    me["age"] = 98


# check if key exist, before reading
    if "prefferd_color" in me:
        me["preffered_color"]


def test_address():
    location = {
        "street": "Evergreen",
        "number": 27,
        "city": "Springfield",
        "state": "CA",
        "zip": "92101"
    }


    print(location["street"])
    print(location["number"])
    print(location["city"])





about_me()
test_address()