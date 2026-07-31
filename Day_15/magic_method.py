class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name:{self.name},Age:{self.age}"

student1 = Student("Shivam",20)

print(student1)


#__str__() = Object ko readable format me print karne ke liye use hota hai.

