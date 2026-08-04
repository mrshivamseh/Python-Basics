class Dog:
    def speak(self):
        print("Dog barks")

class Cat:
    def speak(self):
        print("Cat meows")


def make_sound(animal):
    animal.speak()

dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)

#Duck Typing = Python object ka type nahi dekhta.
#bas required method hona chayie.
