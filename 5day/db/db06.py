# db06.py
import sqlite3
print("삭제할 번호를 입력하세요")
no = input('---> ')
dbcon = sqlite3.connect('test01.db')
cursor = dbcon.cursor()
###########################################
sql = '''delete from T1 where no = ? '''   #리스트 뽑았을때 튜플형인것을 알고 있기에
cursor.execute(sql,(int(no),))             #억지로 tuple형을 만들어줌
dbcon.commit()
###########################################
cursor.close()
dbcon.close()
print("실행 완료")


