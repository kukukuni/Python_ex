# db01.py

#커넥션 연결, 커서 연결, 처리, 커서해제, 커넥션 해제
import sqlite3
dbcon = sqlite3.connect('test01.db')    # 1. 커넥션 연결
cursor = dbcon.cursor()                 # 2. 커서 연결
###########################################
sql = '''select * from T1'''            # 3. 처리
# rows = cursor.execute(sql)
cursor.execute(sql)
rows = cursor.fetchmany(2)
#print(rows)로 rows가 str형이 아닌 것을 알 수있다.
for r in rows: print(r)     #결과로 Tuple형태의 List였다는 것을 알 수 있다.
###########################################
cursor.close()                          # 4. 커서 해제
dbcon.close()                           # 5. 커넥션 해제


