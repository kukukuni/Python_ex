# Book05.py

class Book:
    category = '소설'                 #class 멤버 속성
    def __init__(self):              #intance는 반드시 self씀
        self.title = '무제'           #intance 멤버 속성 intance마다 가지고 있다.

    def pBook(self):
        print(self.title)            #instance 멤버 메소드

    @classmethod                     # 뭐가 들어가든 상관없는데, 보편적으로 class의 cls씀
    def pCate(cls):                  #class 멤버 메소드
        print(Book.category)

    @staticmethod
    def test():                      #static 멤버 메소드
        print('이것은 static멤버 메소드')
######################################################
b1 = Book();b2 = Book()
print(b1.title,b2.title)

print(Book.category);print(b1.category);print(b2.category)
Book.category = '수필'
print(Book.category);print(b1.category);print(b2.category)
Book.pCate()
Book.test()



