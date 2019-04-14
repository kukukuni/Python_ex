# for07.py

a = [10,20,30,40,50]

for i in a : print(i)

for i in range(len(a)) : print(a[i])

######################

# 1 : 10

for i in a : print('{} : {}'.format(int(i/10),i))

for i in range(len(a)) : print('{} : {}'.format(i,a[i]))
#의외로 아래것이 쓰일 가능성이 있다.
