# Book04_1.py
class Book:
    category = '소설' # Class 멤버

b1 = Book(); print(b1.category)
b2 = b1; print(b2.category)
print(Book.category)

Book.category = '수필'
print(b2.category); print(b1.category) ; print(Book.category)

b2.category = 'IT'
print(b2.category); print(b1.category) ; print(Book.category)