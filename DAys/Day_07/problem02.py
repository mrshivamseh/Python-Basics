product = {
    "name":"Laptop",
    "price":"50000",
    "Brand":"DEll",
    "stock":10
}

print("Product name:",product["name"])
print("Product price:",product["price"])

#updated price
product["price"] = 55000
print("New updated price:",product)


product["stock"] = 5
print("Product stock:",product)

#add catagory
product["category"] = "Electronic"
print("Categiry prduct:",product)

print("Final dictionary:",product)




        
        