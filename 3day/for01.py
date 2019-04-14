# for01.py
iArr = (10,20,30)

for i in iArr:
    print(i)

sArr = ['사과','배','바나나']

for s in sArr:
    print(s)

z = 'HPEducation'
for s in z:
    print(s)
#Str도 글자 하나씩 집어넣음

a = {'사과':'apple',
     '포도':'grape',
     '바나나':'banana',
     '컵':'cup',
     '물':'water'}

for k in a.keys():
    print(k)

for v in a.values():
    print(v)

for i,j in a.items():
    print(i,j)
#Unpacking을 이용함

for z in a.items():
    print(z)
#튜플로 그냥 받음




