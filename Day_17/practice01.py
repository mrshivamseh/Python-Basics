from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):      # side -> length of the square  llkn yeh constructor hn
        self.side = side

    def area(self):
        return self.side * self.side

square = Square(5)     #object of square class banaya
print(square.area())