# Func03.py

# 숫자를 입력받아서 그 숫자만큼 * 를 출력하는 함수를 만드세요

def pStar1(num):
    for i in range(num): print('*',end='')
    print()

pStar1(5) #==>  *****
pStar1(3) #==>  ***

# 숫자와 문양을 입력받아서 그 숫자만큼 문양을 출력하는 함수를 만드세요

def pStar2(num=5,shape='$'):
    for i in range(num): print(shape,end='')
    print()
    
pStar2(5,'*') #==>  *****
pStar2(3,'@') #==>  @@@
pStar2(4) #==> $$$$
pStar2()  #==> $$$$$





























