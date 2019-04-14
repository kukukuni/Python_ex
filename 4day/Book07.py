# Book07.py

class Book :
    def __init__(self,t,a,p):
        self.__title__ = t # public 변수앞에__두개면 권한을 주겠다는 의미 뒤에 두개는 public
        self.__author_ = a # private --> 메소드 우회접근 밖에서 외부접근 차단
        self.__price = p   # private --> 메소드 우회접근
        self.category = '' # 방치 (public)

    def pBook(self):
        print(self.__title__+','+self.__author_+','+str(self.__price))
    def setTitle(self,t): self.__title__ = t
    def setAuthor(self,a): self.__author_ = a #__author_를 접근할 수 있는 메소드를 만듬.
                                              # author를 보호하고 우회
    def getAuthor(self): print(self.__author_)
    def setPrice(self,p): self.__price =p

b1 = Book("파이썬","홍길동",30000)
b1.pBook()
b1.setAuthor("김연아"); b1.getAuthor()

