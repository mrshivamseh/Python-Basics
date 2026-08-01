from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):

    def make_sound(self):
        print("Dog barks")


dog = Dog()
dog.make_sound()




# Abstraction = Important cheezein dikhana, implementation hide karna.

# Abstract Class = ABC inherit karti hai.

# Abstract Method = @abstractmethod