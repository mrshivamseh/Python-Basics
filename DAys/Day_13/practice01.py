class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self .model = model

    def display(self):
        print("Brand",self.brand)
        print("Model",self.model)
        print("---------\n")

car1 = Car("Toyota","Fortuner")
car2 = Car("TATA","Nexon")


car1.display()
car2.display()


