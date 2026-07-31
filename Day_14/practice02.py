class Vehicle:

    def __init__(self,brand):    #constructor
        self.brand = brand


    def show_brand(self):         #method:
        print("Brand:",self.brand)

class Bike(Vehicle):    #child class
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model = model

    def details(self):
        print("Brand:",self.brand)
        print("Model",self.model)


bike1 = Bike("RoyalEnfield","classic350")
bike1.details()



# 1. Parent class banao
# 2. Parent constructor (__init__)
# 3. Parent methods
# 4. Child class (Parent)
# 5. Child constructor
# 6. super().__init__()
# 7. Child variables
# 8. Child methods
# 9. Object banao
# 10. Method call