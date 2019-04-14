# Str06.py

a1 = 'Welcome to Korea Education'
a2 = 'Welcome to Korea Education'

print(id(a1),id(a2))
print(a1 is a2)
print(a1 == a2)
#객체의 아이디가 같은가 is 값이 같은가는 ==

print('skhi 입력 바람')

b1 = 'skhi'
b2 = input()
b3 = 'skhi' # b1 동일
b4 = b1     # b1 동일
b5 = b1[:]  # b1 동일 


print(b1 is b2,b1 == b2)
print(id(b1), id(b2))
print(b1 is b5,b1 == b5)
print(id(b5), id(b5))

