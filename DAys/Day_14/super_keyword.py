class Animal:

    def __init__(self,name):
        self.name = name

class Dog(Animal):

    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed

    def details(self):
        print("Name:",self.name)
        print("Breed:",self.breed)


dog = Dog("Tommy","Labradar")
dog.details()

#super()   ->  Child class se Parent class ke constructor ya methods ko call karne ke liye use hota hai.

