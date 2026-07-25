person = {
    "name":"Shivam",
    "age":20,
    "city":"Delhi",
    "profession":"Developer"

}

print("Name of person:",person["name"])
print("City of person:",person["city"])
#updated age
person["age"] = 21

#add item
person["skils"] = "Python"

#update 
person["profession"] = "Python Developer"

#delete item
del person["city"]

print("Final dictionary:",person)