# class Student:
#     def __init__(self, name, hobby, color):
#         self.name = name
#         self.hobby = hobby
#         self.color = color
#     def eating(self):
#         print(self.name, "is eating")

# student1 = Student("Moses", "dancing", "green")
# student2 = Student("Keyla", "singing", "pink")
# student3 = Student("Lisa", "playing", "orange")
# print(student2.hobby)
# print(student1.name)
# print(student3.color)
# student2.eating()

#After-class project
class Robot:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print("My name is ", self.name, "!!!")
    def greetings(self):
        print("Welcome ", self.name, ", How are you doing today?")
    
user1 = Robot("Moses")
user2 = Robot("Adam")
user3 = Robot("Eve")
user3.introduce()
user1.introduce()
user2.introduce()
user3.greetings()
user1.greetings()
user2.greetings()
