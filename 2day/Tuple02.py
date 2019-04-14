# Tuple02.py

a = (10,20,30,40,50)
b = 60,70
c = 80,

print(a+b+c)
print(type(a+b+c))
#좌우로는 같은 타입이어야 한다.

print((a+b+c)[1:-2])

d = (10,20,30),90,'A',(40,(50,[60,70],80),100),
print(d)
# d의 Type과 길이는?
print(type(d), len(d))
# d : 70 출력
print(d[3][1][1][1])

b = True,
print(type(b), len(b), b)

b = None,
print(type(b), len(b), b)

b = None,None
print(type(b), len(b), b)
