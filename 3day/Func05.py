# Func05.py
def pList(*x) :
    for i in x: print(i, end=' ')
    print()

a = [10,20,30,40,50]        #리스트
b = [11,22,33]              #리스트
c = (1,2,3,4)               #튜플
d = {12,23,34,45,56,67}     #셋     까지 모두 수용가능

pList(a) # 10 20 30 40 50   #주소로 하나로 받았느냐   
pList(*b)                   #끊어내서 받았느냐로 a와 b는 다른 결과
pList(*c)                   #*의 사용법을 모르면 쪼개 넣을수 밖에 없고
pList(11,22,33)             #그 말은 필요없는 unpacking을 한다 
pList(*[11,22,33])

def Calc(a,b,c):
    if a == 'Sum': print(b+c)
    elif a == 'Sub' : print(b-c)

Calc('Sum',20,10) # 30
Calc('Sub',60,15) # 45








