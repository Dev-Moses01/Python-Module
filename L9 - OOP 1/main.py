class Student:
    def __init__(self, name, hobby, color):
        self.name = name
        self.hobby = hobby
        self.color = color
    def eating(self):
        print(self.name, "is eating")

student1 = Student("Moses", "dancing", "green")
student2 = Student("Keyla", "singing", "pink")
student3 = Student("Lisa", "playing", "orange")
print(student2.hobby)
print(student1.name)
print(student3.color)
student2.eating()