# for02.py

for i in range(0,10,1):
    print(i)

# 1 ~ 5 까지 가로방향 출력
# 1 2 3 4 5

for i in range(1,6,1): print(i,end=' ');
print()

# 0 ~ 10 까지 짝수만 출력 : 가로방향

for i in range(0,11,2): print(i,end=' ');
print()

for i in range(0,11,1):
    if(i%2==0): print(i,end=' ')
print()
#예스러운 방법
