# File06.py
# 1회성 읽기 : with ~~ as --> open() , close()

with open('./Users/users03.txt','r') as file: #디렉토리를 읽어서 file에 담으라는 뜻
    users = file.read()
    print(users)