1. Magic Methods (Dunder Methods)
__init__() → Constructor
__str__() → Object ko print karne par readable output deta hai.
2. __str__() Rule
def __str__(self):
    return "..."
Hamesha return use hota hai.
print() nahi likhte.
3. Jab hum likhte hain:
print(obj)
Python automatically call karta hai:
obj.__str__()
4. f-string
f"{variable}"
Use hota hai variables ko string ke andar print karne ke liye.