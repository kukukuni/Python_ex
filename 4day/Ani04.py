# Ani04.py

class Animal:
    def __init__(self):
        self.name = '무명'
        print("Animal 실행"+ self.name)
class Dog(Animal):
    def __init__(self):     # 생성자 메소드 오버라이드
        super().__init__()    # 자기는 self 자기의 부모는 super
        print("Dog 실행")

d1 = Dog()