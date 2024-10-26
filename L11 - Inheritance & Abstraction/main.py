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