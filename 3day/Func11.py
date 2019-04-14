# Func11.py

def calc(i,j):
    return i+j,i-j,i*j,i/j

#다른 언어는 지원을 잘 안하지만
#파이썬은 복수의 데이터를 보낼 수 있음 

print(calc(20,10))
a,b,c,d = calc(20,10)   #Unpacking
print(a,b,c,d) #+,-,*,/

def swap(i,j):
    return j,i

x = 200
y = 100
x,y = swap(x,y)
print(x,y) #100, 200
