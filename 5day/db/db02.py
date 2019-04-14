# db02.py

#커넥션 연결, 커서 연결, 처리, 커서해제, 커넥션 해제
import sqlite3
dbcon = sqlite3.connect('test01.db')    # 1. 커넥션 연결
cursor = dbcon.cursor()                 # 2. 커서 연결
###########################################
sql = '''insert into T1 values(50,'Yena')''' #commit을 안해서 저장안됨
cursor.execute(sql)
dbcon.commit()                           #TCL은 직접함
# cursor.execute('commit')               #이것도 가능
###########################################
cursor.close()                          # 4. 커서 해제
dbcon.close()                           # 5. 커넥션 해제


