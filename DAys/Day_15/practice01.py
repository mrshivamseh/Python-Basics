class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name:{self.name}\nAge:{self.age}"



person1 = Person("Shivam",20)

print(person1)
