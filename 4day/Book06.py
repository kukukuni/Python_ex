# Book06.py
class Book :
    b = 0 # class 멤버
    def __init__(self):
        Book.b += 1
        self.a = 0 # instance 멤버
        self.a += 1
    def pBook(self):
        print(self.b, self.a)
##########################################
b1 = Book()
b1.pBook()
b2 = Book()
b2.pBook()
b3 = Book()
b3.pBook()