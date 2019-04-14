# Set03.py

# add(),update(),remove()

a = {10,20,30}
# print(a[1])

a.add(40)
print(a)
a.add(50)
print(a)
a.add(40)
print(a)

a.update({60,70})
print(a)

a.update({80})
print(a)

a.update([11,22])
print(a)
#형이 달라도 update됨

a.update((111,222))
print(a)

a.update((4444,))
print(a)

#a.update((777))
#print(a)
#update는 복합데이터를 올리는데,
#(777)은 숫자라서 안올라감

a.update(('AA',True))
print(a)

a.remove(4444)
print(a)

a.discard(222)
print(a)

#a.remove({'AA', True, 70, 40, 10})
#print(a)
#remove, discard는 하나씩만 뺄수 있고 둘의 차이는
#Set에 원소가 없을때도 작동하느냐 마느냐의 차이다

a = a - {'AA', True, 70, 40, 10}
print(a)
#차집합 연산은 한번에 빠진다.


























