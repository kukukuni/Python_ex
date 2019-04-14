# Set02.py

s1 = {1,2,3}
s2 = tuple(s1)
print(s2,type(s2))

s3 = set([1,2,3,2,1])
print(s1,type(s1))

s4 = 'Hello World'
s5 = set(s4)
print(s5)
#str도 중복제거가 가능하다.
##########################

a1 = {1,2,3,4,5}
a2 = {1,3,5,7,9}

# 교집합
print(a1 & a2)
print(a1.intersection(a2))

# 합집합
print(a1 | a2)
print(a1.union(a2))

# 차집합
print(a1 - a2)
print(a1.difference(a2))

# 교집합의 여집합
print((a1 | a2) - (a1 & a2))
print(a1 ^ a2)







