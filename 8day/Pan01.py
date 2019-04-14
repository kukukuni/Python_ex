# Pan01.py
# Pandas 라이브러리 : Data 분석 라이브러리
# Data Frame (Series) <--List,Dict,Array
# Pandas <-- 코딩하는 엑셀

import pandas as pd

# Series
a = [3,5,-1,4]
s1 = pd.Series(a)
print(s1,type(s1)) #엑셀처럼 라벨이 붙는다.
print(s1.index)

b = ['A','B','C','D']
s2 = pd.Series(b)
print(s2,type(s2))
print(s2.index)

b2 = ['A',1,'C',2]
s2 = pd.Series(b2)
print(s2,type(s2))
print(s2.index)

c = {'Tom':90,'Jane':60,'Alice':70, 'John':80}
s3 = pd.Series(c)
print(s3,type(s3))                          #value에 대한 것이므로 dtype: int64
print(s3.index)                             #문자인덱스를 가지게 됨.
print(s3.values)

s3.name = 'StuPoint'
s3.index = ['제인','톰','앨리스','존']
s3.index.name = '이름 ' #'Name'
print(s3)

d = {'name':['Jane','Tom','Alice','John'],
     'age':[34,27,51,45],
     'point':[80,70,90,60]}

#s4 = pd.Series(d)
#print(s4)

df1 = pd.DataFrame(d)
print(df1)
print(df1.index)
print(df1.columns)
print(df1.values)

df1.index = ['학생1','학생2','학생3','학생4']
df1.index.name = ['학생이름']
df1.columns.name = ['정보']
print(df1)
print(df1.index)
print(df1.columns)

########################################
e = [['Jane',34,80],
     ['Tom',27,70],
     ['Alice',51,90],
     ['John',45,60]]
print(e)
df2 = pd.DataFrame(e,columns=['이름','나이','점수'],
                   index=['학생1','학생2','학생3','학생4'])
print(df2)

########################################
import numpy as np
f = np.random.randn(4,3) ; print(f)
df3 = pd.DataFrame(f) ; print(df3)
df3 = pd.DataFrame(f,columns=['A','B','C']) ; print(df3)

g = {'name':['Jane','Tom','Alice','John'],
     'age':[34,27,51,45],
     'point':[80,70,90,60]}
print(g)
df4 = pd.DataFrame(g,columns=['name','point','age','etc'],
                   index=['학생1','학생2','학생3','학생4'])
print(df4) # NaN : Not a Number (Null)

df5 = pd.Series([1,2,3,np.nan,5,6])
print(df5)




