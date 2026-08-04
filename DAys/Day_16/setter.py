class Student:

    def __init__(self,name,marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self,marks):
        self.__marks = marks


student1 = Student("Shivam",98)

print("Old Marks:",student1.get_marks())     #getter se data read karta hain.

student1.set_marks(99)

print("New Marks:",student1.get_marks())    #setter se data update krta hain.





    # Setter Method = Private variavle ko safely update karne ke liye use hota hai.
