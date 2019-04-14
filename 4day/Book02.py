# Book02.py

# 서점 : 책(제목,저자,가격)

class Book:
    def __init__(self,t= '무제',a= '미상',p= 0):  #입력이 없을것을 고려하여 초기값을 정해둠
        self.title = t  # instance 멤버 속성      #init은 무조건 처음 class실행시에 진행되는 함수라고 생각
        self.author = a
        self.price = p

    def pBook(self):  # instance 멤버 메소드
        print(self.title, self.author, self.price)

b1 = Book()
b2 = Book('파이썬')
b3 = Book('자바','이승엽')
b4 = Book('DB','김연아',30000)                   #heap공간에 생김
b1.pBook();b2.pBook();b3.pBook();b4.pBook()



