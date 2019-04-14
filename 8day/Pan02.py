# Pan02.py
import pandas as pd
a = {'name':['Jane','Tom','Alice','John'],
     'age':[34,27,51,45],
     'point':[80,70,90,60]}
print(a)
df1 = pd.DataFrame(a,columns=['name','point','age','etc'],
                   index=['학생1','학생2','학생3','학생4'])
print(df1)
print(df1['name'])
print(df1.name)
print(df1[['age','point']]) # 열 이름 호출
print(df1[1:3]) # [숫자:숫자] 행 번호 호출
print(df1[1:2][['age','point']])
print(df1.loc['학생1']) # 행 이름 호출
print(df1.loc['학생2'][['age','point']]) # 행 이름, 열 이름 호출
print(df1.iloc[0]) # 행 번호 호출
print(df1['학생1':'학생3'])
print(df1.loc['학생1':'학생3'])

print(df1.loc['학생1':'학생2','point'])
print(df1.loc['학생2':'학생3','point':'etc'])
print(df1.loc[:,'point':'etc']) # == df1[['point','age','etc']]
####################################################
df1['etc'] = 1
df1.loc['학생5',:] = ['Sophia',100,17,9]
df1.loc['학생6',:] = ['James',77,21,7]
print(df1)

print(df1.iloc[1:4,1:4])
print(df1.loc['학생3':'학생5','point':'age'])
print(df1.iloc[2,2])
print(df1.loc['학생5','name'])

# Boolean Indexing
print(df1[df1['point']>75])
print(df1.loc[df1['age']>=30,:])
print(df1[(df1['point']>75)&(df1['age']>=30)])
print(df1.loc[df1['age']>=30,'name':'age'])

print(df1)
# point 가 70 이하인 학생들의 etc를 4 로 변경하세요
print(df1.loc[df1['point']<=70,'etc'])
df1.loc[df1['point']<=70,'etc'] = 4
print(df1)

print(df1['point'].mean())
print(df1['point'].sum())
print(df1['point'].var())
print(df1['point'].std())

print(df1.describe())

print(df1)
print(df1.drop('학생4'))
print(df1)


