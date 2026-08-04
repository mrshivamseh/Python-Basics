📝 Day 16 Notes (Notebook me likh lena)
1. Encapsulation
Data ko protect karna Encapsulation kehlata hai.
Data ko direct access karne ki jagah methods se access karte hain.
2. Private Variable
self.__balance
__ lagane se variable private ban jata hai.
Bahar se direct access nahi karna chahiye.
3. Getter
def get_balance(self):
    return self.__balance
Private data ko read (dekhne) ke liye use hota hai.
4. Setter
def set_balance(self, balance):
    self.__balance = balance
Private data ko update (change) karne ke liye use hota hai.
5. Flow
Object
   ↓
Getter → Read Data
Setter → Update Data



--------

__variable = private
__variable → Private
Getter → Data return karta hai.
Setter → Data update karta hai.
Encapsulation → Data ko secure aur controlled banata hai.