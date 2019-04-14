# Func01.py

# 함수(메소드) --> 입fur,반환,처리,이름

def Hi(name):               #Hi라는 이름은 주소임 주소로 이해
    print(name+"님, 안녕하세요")
#   return None은 함수에 기본적으로 숨겨져 있다.
    return 'Hello'
    
#Hi();

print(Hi('Tom'));
###############################

def 덧셈(a,b):
    return a+b

ans = 덧셈(20,10)
print(ans)
# 30


a = Hi
a("Kane") #주소를 던진거라서 가능

b = 덧셈
print(b(300,200))


















































