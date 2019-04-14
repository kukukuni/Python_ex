# Tuple01.py

# data 수정불가

a = (1,2,3)
print(type(a),a)

#a[1] = 200 이런거 안됨

b = (10,)       ; print(type(b),b)
c = 10,         ; print(type(c),c)
d = 'A','B','C' ; print(type(d),d)
e = 'A',        ; print(type(e),e)
f = 10,20,30    ; print(type(f),f)
g = 10,20,      ; print(type(g),g)

x1 = (10)
x2 = 10,
x3 = (10,)
print(type(x1),type(x2),type(x3))
#데이터에 괄호 하나만 친다는 원형 그대로를 의미한다.

h = [10],
print(type(h))
#데이터를 볼때 제일 마지막 것을 유심히 봐야 한다. ,이랑 )이면 튜플
#인데 )안에 데이터가 하필이면 하나면 int이다.

m = (11,22,33,)
print(m[1],len(m))
# tuple은 공백을

#m = (11,,22,33,)은 안댐 ,에 빈칸이 들어가는 것은 끝처리임
m = (11,None,33,44)
print(m[1],len(m))

x = 11; y = 11,
print(x,type(x),y,type(y))










