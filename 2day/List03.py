# List03.py

a = [65,12,98,43,35]
a.sort()
print(a)

b = [65,12,98,43,35]
b.reverse()
print(b)

c = [65,12,98,43,35]
# 98,65,43,35,12
c.sort(); c.reverse()
print(c)

d = [65,12,98,43,35]
d.sort(reverse =True)
print(d)

e = [65,12,98,43,35]
f = sorted(e)
print(e, f)

#.sort()는 인스턴스형이어서 원본을 건드리지만
#f = sorted(e)는 원본을 건드리지 않고 복사본을 f에 저장
#static이다.

##############################

g1 = 100; g2 = 100
g3 = g4 = g5 = 100
print(g1,g2,g3,g4,g5)
print(id(g1),id(g2),id(g3),id(g4),id(g5))

h1 = [65,12,98,43,35]
h2 = [65,12,98,43,35]
h3 = h1
#공간을 따로 만들어 놓고 안에를 채워놓는 것이라서 다르다.
#즉 공간을 먼저 만들고 채우느냐(ex.input()처럼)의 차이이다.
#단일값을 집어 넣는것과는 다르다.
# = 을 기준으로 숫자를 먼저 집어 넣느냐 주소를 먼저 집어넣느냐의 차이

print(id(h1),id(h2),id(h3))

h1[1] = 120
print(h1[1],h3[1],h2[1])

print(h1[:])

h4 = h1[:] # 복사 (주소전달이 아닌 복사라서 다른것으로 본다)
print(id(h1),id(h2),id(h3),id(h4))

#h3 = h1 은 원본을 건드릴 위험이 있을때 쓰면 안되고
#h4 = h1[:]은 공간낭비를 할 위험이 있다.

#######################################

print(g1,g2)

g1 = None
print(g1)

del g1
#print(g1)

x = [1,2,3]
y = [4,5,6]
print(id(x), id(y))
#z = x + y
x.extend(y)
print(id(x), id(y))#, id(z))

#z = x + y는 새 Z공간을 내는 것이므로 공간낭비가 있고
#x.extend(y)는 x뒤에 붙이는 것이라서 공간낭비가 적다.













