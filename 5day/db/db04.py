# db04.py
import sqlite3
학생들 = {5:'Hong',6:'Sophia',7:'King'}
dbcon = sqlite3.connect('test01.db')
cursor = dbcon.cursor()
###########################################
for i in 학생들.keys():
    sql = '''insert into T1 values({},'{}')'''.format(i,학생들[i])
    cursor.execute(sql)                 # //내코드
# sql = '''insert into T1 calues (?,?)'''
# for i,j in 학생들.items():
#     cursor.execute(sql(i,j))        #python에서는 ?,?로 뒤에 오는 데이터를 받음

dbcon.commit()
###########################################
cursor.close()
dbcon.close()


