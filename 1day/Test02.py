# Test02.py

a = 10
print(a,type(a),id(a))

#a에 주소가 담겨 있어서 형변환이 있어도 실행됨
a = 'Hi'
print(a,type(a),id(a))
a = 3.14
print(a,type(a),id(a))
a = True
print(a,type(a),id(a))
a = 3+4j
print(a,type(a),id(a))

b = 10
c= [10,20,30]
print(a,type(a),id(a))
print(id(b),id(c[0]))

b = None

d = (10,20,30); print(type(d))
e = {10,20,30}; print(type(e))
f = None
print(type(f))
