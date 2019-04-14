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
#Str도 하나씩 s에 들어가게 할 수 있다.

a = {'사과':'apple',
     '포도':'grape',
     '바나나':'banana',
     '컵':'cup',
     '물':'water'}

for k in a.keys():      #List
    print(k)

for v in a.values():    #List
    print(v)

for i,j in a.items():   #List[(tuple)]
    print(i,j)          #Tuple안에 있는 것을 unpacking할 때

for z in a.items():     #List[(tuple)]
    print(z)            #튜플은 하나로 받음





