# Book01.py

# 서점 : 책(제목,저자,가격)

class Book:
    def __init__(self):                     #멤버 생성자 <- 메모리 로드, 호출
                                            #Java는 this python은 self로 자기참조
        self.title = '무제'                  #self를 이용해서 Book의 주소에 title을 넣음
        self.author = '미상'                 #instance 멤버 속성
        self.price = 0

    def pBook(self):                        #instance 멤버 메소드
        print(self.title, self.author, self.price)
                            
                            
b1 = Book()                                 #Book b1 = New Book()에서 앞쪽 은닉됨. New와 type이 빠짐
b1.pBook()                                  #노트북, 핸드폰은 각자 씀 -> 인스턴스하다
b1.title='파이썬'; b1.author='Tom'; b1.price=30000        #정수기, 프로젝터는 같이 씀 -> 스테틱하다
b1.pBook()

b2 = Book()
b2.title='자바'; b2.author='Jane'; b2.price=20000
b2.pBook()

print(id(b1),id(b2))
# b1과 b2는 다른 개체 파이썬은 New가 숨겨져 있다.
