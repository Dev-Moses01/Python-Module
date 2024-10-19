class Library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
    
    def displayBooks(self):
        print("We have the following books in our library: ", self.name)
        for book in self.booklist:
            print(book)

    def addBook(self, book):
        self.booklist.append(book)
        print(book, "is added successfully in: ", self.name)
    
    def __del__(self):
        print("Object deleted successfully")

library1 = Library(["Mathematics", "Physics", "Chemistry"], "Bookstore")
library2 = Library(["Legacies", "Originals", "Teen wolves"], "Novels")

del library1
library1.addBook("Biology")
library2.addBook("Van Helsing")

library1.displayBooks()
library2.displayBooks()