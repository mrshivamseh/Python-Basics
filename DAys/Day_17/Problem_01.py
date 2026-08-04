from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car start with key.")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike starts with self-start.")

car = Car()
car.start_engine()

bike = Bike()
bike.start_engine()