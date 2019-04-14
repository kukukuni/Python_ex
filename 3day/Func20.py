# Func20.py
# Closure
def Calc():
    def sum(i,j): return i+j
    def sub(i,j): return i-j
    def mul(i,j): return i*j
    def div(i,j): return i/j
    def ans(x,a,b):
        if x =='덧셈': return sum(a,b)
        elif x =='뺄셈': return sub(a,b)
        elif x =='곱셈': return mul(a,b)
        elif x =='나눗셈': return div(a,b)
                #안에 있는 구문을 가리고 쓸 수 있다.
    return ans #반환값이 주소이다.  

계산 = Calc()
print(계산('덧셈',30,12))
print(계산('뺄셈',30,12))
print(계산('곱셈',30,12))
print(계산('나눗셈',30,12))
