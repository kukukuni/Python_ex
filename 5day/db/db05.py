# db05.py
import sqlite3
print("번호,이름을 입력하세요")
no, name = input('---> ').split()
dbcon = sqlite3.connect('test01.db')
cursor = dbcon.cursor()
###########################################
sql = '''update T1 set name = ? where no = ? '''
cursor.execute(sql,(name,int(no)))
dbcon.commit()
###########################################
cursor.close()
dbcon.close()
print("실행 완료")


