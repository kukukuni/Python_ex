# File05.py
uList = ['Hong','James','Tom','Alice','Jane']
# /Users/users03.txt
# open(w), write(), close()
# 1: Hong\n , 2: James\n + 3: Tom\n + 4: Alice\n + 5: Jane\n
f1 = open('./Users/users03.txt','w')
for i in range(len(uList)):
    f1.write('{} : {}\n'.format(i+1,uList[i]))
f1.close()
if f1.closed : print("입력 완료")
