1. Inheritance
Inheritance = Parent class ki properties aur methods ko Child class me use karna.
Syntax
class Child(Parent):
2. Parent Class
Jo class apni properties aur methods dusri class ko deti hai.
Example:
class Animal:
3. Child Class
Jo Parent class se properties aur methods leti hai.
Example:
class Dog(Animal):
4. Method Overriding
Child class Parent ke same method ko apne hisab se change kar sakti hai.
Example:
class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Dog Barks")
5. super()
Parent class ke constructor ya method ko call karne ke liye use hota hai.
Syntax:
super().__init__(name)