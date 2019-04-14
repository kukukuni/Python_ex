# Ani05.py
from abc import ABCMeta
from abc import abstractclassmethod
# 강제로 메소드를 쓰게 하고 싶다 ->abstract 메소드

class Animal(metaclass=ABCMeta):
    def cry(self): print("으 앙") # 일반 method
    @abstractclassmethod   #자식이 구현을 안해놓으면 에러를 냄
    def shout(self): pass # 추상(abstract) method

class Cat(Animal) :
    def shout(self): print('캬르릉')
    
c1 = Cat()
c1.cry()
c1.shout()