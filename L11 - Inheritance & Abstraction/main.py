class Teacher:
    def __init__(self, subject, iq):
        self.subject = subject
        self.iq = iq
    def show(self):
        print(f"My best subject is {self.subject} and my IQ is {self.iq}")

class Student(Teacher):
    def __init__(self, name, age, subject, iq):
        self.name = name
        self.age = age
        super().__init__(subject, iq)

student1 = Student("Moses", 17, "Coding", "150")
student2 = Student("Machala", 18, "Hacking", "200")
teacher1 = Teacher("Programming", "170")
student1.show()
student2.show()
teacher1.show()

from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def deposit():
        pass
    def withdraw():
        pass

class User(Bank):
    print("Success")

User.deposit()
User.loan()

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
