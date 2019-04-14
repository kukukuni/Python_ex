# Ani01_1.py
# Animal : name , cry(), shout()
#   --> Dog , Cat

class Animal(object) :
    aList = []
    def __init__(self):
        self.name = '이 름'
        self.aList.append(self.name)
    def cry(self): return '운 다'
    def shout(self): return '외친다'

c
class Dog(Animal) :
    def cry(self):  # 메소드 오버라이드
        self.aList.append(self.name)
        return '멍 멍'
class Cat(Animal) :
    def cry(self): return '야 옹' # 메소드 오버라이드

d1 = Dog()
d1.name = '해 피'
print(d1.name,d1.cry(),d1.shout(),Animal.aList)
c1 = Cat()
c1.name = '아 치'
print(c1.name,c1.cry(),c1.shout(),Animal.aList)
