# Range01.py

# a = [0,1,2,3,4,5,6,7,8,9]
a = list(range(0,10,2))
print(a)
#0부터 10까지 2의 간격으로

a = list(range(0,10))
print(a)
#1이 기본값

a = list(range(10))
print(a)
#0이 Starting Point 기본값

b = list(range(1,11))
print(b)
#1~10

c = list(range(0,10,2))
print(c)

#10~1역순
d = list(range(10,0,-1))
print(d)

e = list(range(0,10,1))
print(e)

# f = e에서홀수만
# select 항목 form 대상 where 조건
# for 항목 in 대상 if 조건
f = [ i for i in e if(i%2)==1]
print(f)
#파이썬스럽게 코딩하는 법

# e에서 홀수만 제곱해서 g에 복사
g = [ i**2 for i in e if(i%2)]
*print(g)

# e에서 홀수만 원래 숫자: 제곱숫자 h에 복사
h = { i:i**2 for i in e if(i%2)==1}
print(h)

x = 'ereefaerwthrtehberewfcredfdfabc'
# y = [x에서 'abc' 가 아닌 문자] 중복 제거 후, 정렬
y = sorted(list(set([ s for s in x if s not in 'abc'])))
print(y)
#여기서 주요시 봐야 할 것은 not in과 in의 쓰임
























