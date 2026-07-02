#problem-01 smart library 

class Book:
    def __init__(self, title, author, available_copies):
        self.title=title
        self.author=author
        self.available_copies=available_copies
        
class Library:
    def __init__(self):
        self.inventory={}

    def add_book(self, book_object):
        self.inventory[book_object.title]=book_object  

    def borrow_book(self,title):
        if title in self.inventory:
            book=self.inventory[title]

            if book.available_copies > 0:
                book.available_copies -= 1
                print("Book borrowed successfully.")
            else:
                print("No copies available.")
        else:
            print("Book not found.")


book1 = Book("Python Basics", "John", 3)
book2 = Book("Data Structures", "Alice", 2)

library = Library()

library.add_book(book1)
library.add_book(book2)

library.borrow_book("Python Basics")
library.borrow_book("Python Basics")
library.borrow_book("Python Basics")
library.borrow_book("Python Basics")






#problem-02 The Student Tracker

class Student:
    def __init__(self,name,student_id):
        self.profile=(name,student_id)
        self.grade=[] 

    def add_grade(self,subject,score):
        self.grade.append((subject,score))
    def get_average(self):
        if (len(self.grade)==0):
            return 0
        total=0
        for subject, score in self.grade:
            total+=score
        average=total/len(self.grade)
        return average

student1 = Student("Arshi", 123)
student1.add_grade("Maths", 90)
student1.add_grade("Python", 95)
student1.add_grade("english", 99)
print("profile:", student1.profile)
print("grades:", student1.grade)
print("average:" , student1.get_average(self ))


