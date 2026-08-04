from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):

    def make_sound(self):
        print("Dog barks")

class Cat(Animal):
    def make_sound(self):
        print("Cat meows")

dog = Dog()
dog.make_sound()

cat = Cat()
cat.make_sound()




# Abstract Class = Rules banati hai.

# Child Class = Un rules ko implement karti hai.

# Har Child Class ko Abstract Method implement karna zaroori hai.