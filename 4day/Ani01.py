# Ani01.py
# --> 개 Dog, 고양이 Cat

class Animal:   #여기는 사실 Animal(object)가 숨겨져 있다. 모든 클래스는 object의 상속임.
    def __init__(self):
        self.name = '이 름'
    def cry(self): return '운 다'

    def shout(self): return '으르렁'

class Dog(Animal): #Animal에서 상속받았다는 뜻
    def __init__(self,a='이 름'):
        self.name = a
    def cry(self): return '멍 멍' #메소드 오버라이드 상속받은 것을 변경시킴

class Cat(Animal):
    def cry(self): return '야 옹' #메소드 오버라이드 상속받은 것을 변경시킴

d1 = Dog(); c1 = Cat()
d1.name = '아치';c1.name = '해피'
print(d1.name,d1.cry(),d1.shout())
print(c1.name,c1.cry(),c1.shout())

d2 = Dog("지니")
print(d2.name,d2.cry(),d2.shout())