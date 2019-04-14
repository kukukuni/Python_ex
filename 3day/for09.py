# for09.py

a = []

# a 에 for문을 사용해서 1 ~ 10 까지 입력

# a[0] <- 1, a[9] <- 10

for i in range(10):
    # a[i] = i+1 이건 있는 데이터를 수정한다는 의미라서 안됨
      a = a + [i+1]  
##    a.append(i+1)


print(a)
