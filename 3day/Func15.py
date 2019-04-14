# Func15.py

a = ['콜라','사이다','씨그램','우유','활명수']
b = [1000,900,600,700,800]
c = list(zip(a,b))  #zip이란 함수로 매칭 리스트 한쪽이 더 길면 그건 잘라서
print(c)            #나머지만 나옴
d = dict(zip(a,b))
print(d)

e = '1001'
print(e,type(e))
f = int(e,base=10)  #1001을 10진수로 생각
print(f,type(f))

g = int(e,base=2)   #1001을 2진수로 생각
print(g,type(g))

from functools import partial
DecFromBin = partial(int,base=2) #DecFromBin은 임의로 함수를 바꾼것
print(DecFromBin('1001'))
