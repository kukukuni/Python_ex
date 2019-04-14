# Dict02.py

a = {'사과':'apple',
     '포도':'grape',
     '바나나':'banana',
     '컵':'cup',
     '물':'water'}

print(a['컵'])

# 강 river
a['강'] = 'river'
print(a)

# 자바 java
a['자바'] = 'java'
print(a)

a.pop('강')
print(a)

del a['자바']
print(a)

# key에서 바나나가 존재하는지 궁금
print('바나나' in a.keys())

# value에서 grape가 존재하는지 궁금
print('grape' in a.values())

# item에서 '사과':'apple' 존재
print(('사과','apple') in a.items())
# items()는 출력시에 튜플의 리스트형태이므로,
# 튜플로 물어봐야 한다.


























