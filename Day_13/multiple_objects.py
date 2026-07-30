class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("---------")

student1 = Student("Shivam",20)
student2 = Student("Rahul",19)
student3 = Student("abhinav",18)


student1.introduce()
student2.introduce()
student3.introduce()
