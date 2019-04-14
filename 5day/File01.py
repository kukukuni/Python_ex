# File01.py
# open(), 처리: write(), read(), close()
# users01은 ANSI, users02는 UTF-8파일이라 어떤건 읽히고 어떤건 안읽힘


f1 = open('./Users/users01.txt',mode='r',encoding='cp949')  #상대주소
users1 = f1.read()              #읽어서 복사하고 닫기
f1.close()
print(users1)

#######################################################

f2 = open('D:/Programming/Python/CODE/5day/Users/users02.txt',mode='r',encoding='utf-8')#절대주소
users2 = f2.read()
f2.close()
print(users2)