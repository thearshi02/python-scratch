#problem-01 The smart home System(Composition)

class Engine:
    def start(self):
        return "vroom!"

class Wheels:
    def roll(self):
        return "wheels are spinning"

class Vehicle:
    def __init__(self):
        self.engine=Engine()
        self.wheels=Wheels() 

    def drive(self):
        print(self.engine.start())
        print(self.wheels.roll())

vehicle1=Vehicle()
vehicle1.drive()    


#PROBLEM-02 The custom books Portfolio(Magic Methods)

class Book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages

    def __str__(self):
        return f"{self.title} by {self.author}"  

    def __eq__(self,other):
        return self.title==other.title and self.author==other.author

class Library:
    def __init__(self, books):
        self.books=books

    def __len__(self):
        return len(self.books)

book1=Book("The Hobbit", "J.R.R", 310)  
book2=Book("The Hobbit", "J.R.R", 310) 
book3=Book("Harry Potter", "JK Rowling", 500)  

print(book1==book2)
print(book1)
my_library =Library([book1,book2,book3])
print(len(my_library))
