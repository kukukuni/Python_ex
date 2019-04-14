# File02.py
# open(), 처리: write(), read(), close() --> 'Hong'
# users01은 ANSI, users02는 UTF-8파일이라 어떤건 읽히고 어떤건 안읽힘
# w : 신규, a : 추가(append)

user = 'Hong'
f1 = open('./Users/users01.txt',mode='a',encoding='cp949')  #상대주소
f1.write('\n'+user)      #그냥 쓰면 마지막의 옆에 그냥 써버림 따라서 \n
f1.close()
print('추가완료')

#######################################################

f2 = open('D:/Programming/Python/CODE/5day/Users/users02.txt',mode='a',encoding='utf-8')#절대주소
f2.write('\n'+user)                 #해킹을 당할 위험도 있고, 배포시에 위치가 다르므로 상대경로를 더 선호
f2.close()
print('추가완료')