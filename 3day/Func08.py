# Func08.py

a = 7

def Sum(i,j):
    global a #글로벌로 댕겨옴
 #   a = 7 로컬
    r= i+j+a
    return r 

print(Sum(10,20))


b = 0
def test(a):
    global b #global b = a는 안됨
    b = a
    
test(200)
print(b) #200
