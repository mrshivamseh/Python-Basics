class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance     #return


    def set_balance(self,balance):
        self.__balance = balance     #update


account1 = BankAccount("Shivam",5000)  #object create

print(account1.get_balance())  #first balance

account1.set_balance(8000)   #new balance

print(account1.get_balance())     #updated balance


