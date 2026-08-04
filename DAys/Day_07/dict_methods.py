student = {
    "name":"shivam",
    "age":20
}

#Add new item
student["course"] = "Python"
print("After add:",student)


#Update item
student["age"] = 21
print("After update:",student)

#Delete item
del student["age"]
print("After delete:",student)