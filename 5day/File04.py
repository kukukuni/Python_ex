# File04.py

# 1. open() read() ==> 한줄 str
file1 = open('./Users/users01.txt','r')
users1 = file1.read()  #원래는 \n까지 한줄의 str으로 받음. 그런데 콘솔에 나타내다보니 enter가 된것
print(type(users1))
print(users1)
file1.close()
# 2. open() readline() ==> 줄별 str
file2 = open('./Users/users01.txt','r')
while True:
    users2 = file2.readline()
    if not users2 : break   #<-- ''
    print(type(users2),users2)
file2.close()
# 3. open() readlines() ==> list
file3 = open('./Users/users01.txt','r')
users3 = file3.readlines()
print(type(users3))
print(users3)
for u in users3 : print(type(u),u)
file3.close()

#자신의 쓰임과 부합하는 함수가 있는지 확인하고 불러와라