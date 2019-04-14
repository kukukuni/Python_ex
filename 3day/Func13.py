# Func13.py

def sum(i,j): return i+j
def sub(i,j): return i-j
def mul(i,j): return i*j
def div(i,j): return i/j
def nmj(i,j): return i%j


a = sum
print(a(20,10)) #주소값을 a에 지정하는 거라서 가능


b = lambda i,j:i%j
print(b(32,5))


calcList = [sum,sub,mul,div,lambda i,j:i%j]  #변수, 함수아닌 주소로 보아야함
for c in calcList : print(c(200,100))


calcList2 = []
calcList2.append(sum)
calcList2.append(mul)
calcList2.append(sub)
for c in calcList2: print(c(1000,2000))
calcList2.remove(sub)
for c in calcList2: print(c(1000,2000))

사칙연산 = {'덧셈':sum, '뺄셈':sub}

print(사칙연산['뺄셈'](1000,2000))






















    

