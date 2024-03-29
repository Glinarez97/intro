def products_test():
    products = [
        {
            "title": "Smartphone",
            "image": "smartphone.jpg",
            "price": 299.99,
            "category": "Electronics",
        },
        {
            "title": "Running Shoes",
            "image": "running_shoes.jpg",
            "price": 89.99,
            "category": "Footwear",
        },
        {
            "title": "Backpack",
            "image": "backpack.jpg",
            "price": 49.99,
            "category": "Accessories",
        },
        {
            "title": "Coffee Maker",
            "image": "coffee_maker.jpg",
            "price": 119.99,
            "category": "Home Appliances",
        },
{
            "title": "Wireless Headphones",
            "image": "wireless_headphones.jpg",
            "price": 159.99,
            "category": "Electronics",
        },
        {
            "title": "Fitness Tracker",
            "image": "fitness_tracker.jpg",
            "price": 59.99,
            "category": "Wearables",
        },
        {
            "title": "Digital Camera",
            "image": "digital_camera.jpg",
            "price": 349.99,
            "category": "Electronics",
        },
        {
            "title": "Yoga Mat",
            "image": "yoga_mat.jpg",
            "price": 25.99,
            "category": "Fitness",
        },
{
            "title": "Novel - 'Mystery of the Old Manor'",
            "image": "novel.jpg",
            "price": 14.99,
            "category": "Books",
        },
        {
            "title": "Portable Charger",
            "image": "portable_charger.jpg",
            "price": 39.99,
            "category": "Electronics",
        },
    ]



    total = 0
    totalA = 0
    for product in products:
        title = product["title"]
        price = product["price"]
        category = product["category"]

        if category == "Electronics":
            print(f"{title} {price}")
            total = total + price
            totalA += 1

    print(total)
    print(f"There is {totalA} electronics")




products_test()