student = {
    "name":"Shivam",
    "age":20,
    "course":"Python",
    "marks":85
}

print("Student name:",student["name"])
print("Student course:",student["course"])

student["marks"] = 95

#add item
student["city"] = "Delhi"

#Remove item
del student["age"]

print("Final Dictionary:",student)