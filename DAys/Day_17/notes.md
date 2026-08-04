1. Abstraction
Sirf important cheezein dikhana.
Internal implementation ko hide karna.
2. Abstract Class
class Animal(ABC):
ABC inherit karti hai.
Iska direct object nahi ban sakta.
3. Abstract Method
@abstractmethod
def sound(self):
    pass
Sirf rule define karta hai.
Body child class me likhi jaati hai.
4. Child Class
class Dog(Animal):
Abstract method ko implement karna mandatory hai.
5. Difference
Encapsulation
Abstraction
Data ko hide karta hai
Implementation ko hide karta hai
__private variable use hota hai
ABC aur @abstractmethod use hote hain
 Revision ->
Yaad rakhna:
✅ ABC = Abstract Base Class
✅ @abstractmethod = Rule banata hai
✅ Child class ko implement karna hi padta hai
✅ Abstract class ka object nahi banta