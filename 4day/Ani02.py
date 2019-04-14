# Ani02.py
#자바 등 다른언어는 다중상속을 지원하지 않음 대체제가 abstract와 interface임
#하지만 파이썬은 가능...

class A:

    def test1(selfself):print('A')
    def testA(selfself): print('testA')

class B:
    def test1(selfself): print('B')
    def testB(selfself): print('testB')

class C:
    def test1(selfself): print('C')
    def testC(selfself): print('testC')

class D: pass

d1 = D()        #기본적으로 D는 Object를 상속받는 것이므로 init있다. 즉 인스턴스 생성가능해 에러 안남

class D(A,B,C): pass

d1 = D()        #다중상속가능
print(d1.test1())#해보면알겠지만, 겹치는 것만 맨앞의 것으로 함. 이것으로 다중상속의 위험을 대처
print(d1.testA())
print(d1.testB())
print(d1.testC())
