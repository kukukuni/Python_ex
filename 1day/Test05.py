# Test05.py

print("1 ~ 10 중 숫자 하나 입력")

### 10을 더해서, ==> 결과  : 13

a = input()
print("==> 결과 : "+str(int(a)+10))

b = int(input())
print("==> 결과 : "+ str(b + 10))
# 파이썬은 +기준으로 형이 다르면 무조건 에러라서 str을 앞에 붙여줘야 함

print("==> 결과 : ", b + 10)
# 이건 하나의 주소가 아닌 두개의 주소를 올리는 것이다.
