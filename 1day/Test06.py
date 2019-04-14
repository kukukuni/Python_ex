# Test06.py

c = b = a = 10;
print(a,id(a))
print(b,id(b))
print(c,id(c))

#e = 11; f = 12; g = 13;
e,f,g = 11,12,13;
print(e,f,g)

h = 33
print(h,id(h))
# 주소만을 끊어낼때
h = None
print(h,id(h))
# 변수명을 없앨때
del h
#print(h,id(h)) 호출이 안됨
