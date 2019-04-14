# File03.py
# mode : a+
user = 'Ali'
f1 = open('./Users/users01.txt',mode='a+')  #,encoding='cp949'이건 기본값이지만 쓰는 버릇이 더 좋다.
f1.write('\n'+user)
f1.seek(0)         #따라서 위와 같이 커서를 올려서 읽기를 실행한다.
users1 = f1.read() #이렇게 하면 안되는 이유는 커서가 가장 아래로 내려가 있기 때문이다.
f1.close()
print(users1)
print(f1.closed)
