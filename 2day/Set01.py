# Set01.py
# 중복불가, 집합 개념 

a = {}      # dict
print(a,type(a))

b = {10,20,30} # set 
c = {10:'사과'}# dict
print(type(b),type(c))

과일 = "사과","배","토마토","배","토마토","포도"
print(type(과일))
fruits = set(과일)
#set은 중복이 허락이 안됨 

print(type(fruits),fruits)
과일 = list(fruits)
과일.sort()
print(type(과일),과일)
#Set은 순서가 없기때문에 list로 만들어서 순서를 맞추고
#정렬을 한다. tuple은 안됨 수정이 불가하니까.

과일2 = "사과","배","토마토","배","토마토","포도"
과일2 = list(set(과일2))
과일2.sort()
#과일2 = list(set(과일2)).sort()를 한다면 .sort()는 함수이고 반환형이 없다.
#따라서 sort가 되지만 반환이 없어 과일2에는 None이 들어가는 것이다.
#print(과일2.sort())도 안댐
print(과일2)

#그래서 보통 Set으로 중복을 제거하고
#List로 순서를 처리하고
#Tuple로 밀봉을 해버린다.










