# Str05.py


a1 = 'Welcome to '
a2 = 'Korea Education'

print((a1 + a2)[3:16])

#come to Korea
#붙이면 하나의 주소처럼 쓸 수 있다.

s1 = 4
b = 'I have %d apples' % s1
print(b)
b = 'I have {} apples'.format(s1)
print(b)

s1 = 'five'
b = 'I have %s apples' % s1
print(b)

s1 = 3.14
b = 'I have %f apples' % s1
print(b)

s2 = 4; s3 = 'five'
c = 'I have %d apples and %s bananas' % (s2, s3)
print(c)

d = 'I have {} apples and {} bananas'.format(s2,s3)
print(d)
#format은 타입을 안가림, 주소전달 방식이라서

############################################
e = 'hi'
print('안녕 %s 제인' % e)
print('안녕 %10s 제인' % e)
#hi 제외 앞8칸을 비운다 아래는 뒤 8칸
print('안녕 %-10s 제인' % e)

f = 12.345678
print('안녕 %d 제인' % f)
print('안녕 %f 제인' % f)

print('안녕 %10f 제인' % f)
print('안녕 %-10f 제인' % f)
print('안녕 %10.4f 제인' % f)
print('안녕 %-10.1f 제인' % f)

이름 = '홍길동'
print(이름)































