# Str03.py


a = '20190311Mon'

date = a[:8]
day = a[8:]

print(date,day)
print("일시 : "+date)
print("일시 : {0}".format(date))
print("일시 : {}".format(date))

print("날짜 : "+day)
print("날짜 : {0}".format(day))
print("날짜 : {}".format(day))

print("{0} {1} {2}".format('일시',':',date))
print("{2} {0} {1}".format(':',date,'일시'))
print("{} {} {}".format('일시',':',date))

b = 'Pithon'
b = '{}{}{}'.format(b[0],'y',b[2:])
#str의 경우는 tuple처럼 수정이 안됨. 따라서 b[1] = 'y'는 안댐
#그리고 str은 하나의 주소값을 가지는데, 위는 y는 사이에 새로운
#주소를 끼워넣는다는 의미라서 안댐
print(b)
