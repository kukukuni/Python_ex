# Tuple03.py

a = '사과','배','토마토';
#a[1] = '포도'; 안댐 튜플이라서

print(id(a))
b,c,d = a   #Tuple Unpacking
c = '포도'
a = b,c,d
print(a)    #Tuple Packing
print(id(a))
#튜플은 extend가 없다 +이 아예 새로운 것으로 바뀌는 것처럼
#a도 새로운 묶음이 되어 id가 달라진다.

z = 10,20,30
#z의 모든 숫자를 1씩 증가시키세요
a,b,c = z
z = a+1,b+1,c+1
print(z)    #11,21,31

z = z[0]+1,z[1]+1,z[2]+1
print(z)    #12,22,32

# z을 다음과 같이 변경하세요
z= str(z[0])+'a',str(z[1])+'b',str(z[2])+'c'
print(z) # '12a','22b','32c'

z1,z2,z3 = map(str,z)
z = z1+'A', z2+'B', z3+'C'
print(z) # '12aA','22bB','32cC'

y = '사과', '배', '토마토',;
x = list(y)
print(type(x),x)





