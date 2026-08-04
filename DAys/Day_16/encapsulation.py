class student:

    def __init__(self,name,marks):
        self.name = name
        self.__marks = marks     #yha isme 2 under score lge hue n  means marks ko private variavle bana diya 

    def show_marks(self):
        print("Marks:",self.__marks)

student1 = student("Shivam",95)

print(student1.name)

student1.show_marks()



# Encapsulation = Data ko protect krna mtlb hide karna.
# Private Variavle = __varivale
