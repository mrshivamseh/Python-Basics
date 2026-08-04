class Person:

    def __init__(self,name):
        self.name = name

    def show_name(self):
        print("Name:",self.name)

class Student(Person):

    def __init__(self,name,course):
        super().__init__(name)
        self.course = course


    def details(self):
        print("Name:",self.name)
        print("Course:",self.course)

student1 = Student("Shivam","Python")
student1.details()

