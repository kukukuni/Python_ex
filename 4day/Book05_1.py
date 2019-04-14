# Book05_1.py

class Book :
    bList = [] # class 멤버
    def __init__(self,s1,s2):
        Book.bList.append(s1)
        self.aList = [] # instance 멤버
        self.aList.append(s2 )
        print(id(self.bList),id(Book.bList))
    def pBook(self):
        print(Book.bList,self.aList)
##############################################
b1 = Book('A',10)
b1.pBook()
b2 = Book('B',20)
b2.pBook()
