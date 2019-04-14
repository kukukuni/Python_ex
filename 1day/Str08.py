# Str08.py

# a1, a2, a3, a4
a1, a2, a3, a4 ='Java,C,SQL,Python'.split(',')
print(a1,a2,a3,a4)

b = ''.join(['H', 'e', 'l', 'l', 'o'])
print(b) #Hello
#''에대가 join을 사용

print('안녕하세요',sep=' ',end='\n')
#sep은 seperator은 구분자로 ,를 어떻게 표시할 것인가를 의미
print('안녕하세요',end='')
print('안녕하세요',end=' ')
print('안녕하세요')
print('안','녕','하','세','요',sep=' ')
print('안','녕','하','세','요',sep='/')
print('안','녕','하','세','요',sep=',',end='\t')
