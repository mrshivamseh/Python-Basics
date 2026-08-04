employee = {
    "name":"Shivam",
    "salary":250000,
    "city":"Delhi"

}
print("Employee:",employee)

#updated salary
employee["salary"] = 300000
print("updated salary:",employee)

#add new key
employee["Department"] = "IT"
print("After Adding Department:",employee)

#Remove city
del employee["city"]
print("Final Dictionary:",employee)
