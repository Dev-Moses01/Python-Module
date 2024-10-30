class Bank:
    def __init__(self, name, location):
        self.name = name
        self.location = location
    def show(self):
        print("You have deposited successfully")

class POS:
    def __init__(self, name, location):
        self.name = name
        self.location = location
    def show(self):
        print("You have withdrawn successfully")

Uba = Bank("UBA", "Lagos")
Moses = POS("Moses", "Lagos")

for m in (Uba, Moses):
    m.show()

class Computer:
    def __init__(self):
        self.__price = 500

    def get_price(self):
        return self.__price
    def set_price(self, price):
        self.__price = price


comp1 = Computer()
comp1.set_price(800)
print(comp1.get_price())


#After-class project
import math

class Polygon:
    def area(self):
        raise NotImplementedError("This method should be overridden in subclasses")

class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

def main():
    # Create instances of each polygon
    triangle = Triangle(10, 5)
    rectangle = Rectangle(4, 6)
    circle = Circle(3)

    # Calculate and print areas
    print(f"Area of Triangle: {triangle.area()} square units")
    print(f"Area of Rectangle: {rectangle.area()} square units")
    print(f"Area of Circle: {circle.area()} square units")

if __name__ == "__main__":
    main()
