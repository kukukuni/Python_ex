# Dict03.py

a = {'사과':'apple',
     '포도':'grape',
     '바나나':'banana',
     '컵':'cup',
     '물':'water'}

print(a['포도'])
print(a.get('포도'))             #<-- key에서만 사용가능

print(a.get('grape'))            #None으로 표시됨
print(a.get('grape','없음'))     #없음으로 표시됨

# 강 river
a['강'] = 'river'
print(a)

b = {'불':'fire','집':'house'}
#print(a+b)
# Dict는 바로 붙이는 작업이 안됨
a.update(b)
print(a)

# 없으면 추가, 있으면 기존 data 호출
# 집 home, 책 book
# setdefault <-- 읽기, 추가 합성
print(a.setdefault('집','home'))
print(a.setdefault('책','book'))
print(a)

for z in a.items():
    print(z)

y = list(a.items())
print(y)























