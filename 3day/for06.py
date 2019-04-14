# for06.py

# 0 ~ 10까지 가로방향 출력
for i in range(11):
    if(i>7) : break        #break는 for문 뒤로 빠지게 만듬
    if(i%2) == 1: continue #continue는 for문의 앞으로 빠져서 계속하게함
    print(i,end=' ')

for j in range(11): pass #코딩이 안된 부분은 내부구현을 안해도 지나가게 함
