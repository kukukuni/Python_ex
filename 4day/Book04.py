# Book04.py

class Book:             #모든 class는 우리가 재정의를 안해서 그렇지 __init__이란 생성자는 있다.
    category = '소설'    #Class 멤버


b1 = Book();print(b1.category)
b2 = Book();print(b2.category) #b1=b2로 하면 둘의id 같음
print(Book.category)

Book.category = '수필'
print(b1.category);print(b2.category);print(Book.category)
b2.category = 'IT'
print(b1.category);print(b2.category);print(Book.category)

