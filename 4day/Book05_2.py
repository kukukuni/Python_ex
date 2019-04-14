# Book05_2.py

class Book :
    def __init__(self):
        self.title='무제'

b1 = Book()
b1.author = '미상'
print(b1.author)
Book.cate = '소설'
b2 = Book()
b2.author = '미상'
print(b2.cate,id(b2.author))
print(b1.cate,id(b1.author))
