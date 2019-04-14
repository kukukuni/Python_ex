# Ani03.py
class Animal(object):
    def __init__(self):
        self.name = '이 름'
    def __add__(self, other): #덧셈 연산자(사실은 연결 연산자) 메소드 오버라이드
        return self.name + ',' + other.name + '입니다.'

class Dog(Animal): pass
class Cat(Animal): pass

d1 = Dog()
c1 = Cat()
d1.name = '아 치'
c1.name = '해 피'
# print(d1.name+c1.name)
print(d1+c1)    #d1.__add__(self, c1)이런식으로 되는 것임