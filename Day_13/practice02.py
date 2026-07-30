class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def details(self):
        print("Employee Name:",self.name)
        print("Employee salary:",self.salary)
        print("---------\n")

        
Employee1 = Employee("Shivam",250000)
Employee2 = Employee("Rahul",30000)

Employee1.details()
Employee2.details()
