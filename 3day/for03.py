# for03.py

# 7단 출력
# 7 * 1 = 7
# ~~~~~
# 7 * 10 = 70

print("몇 단을 출력할까요?")
#j = int(input())
#for i in range(1,11):print(str(j)+' * '+str(i)+' = '+str(i*j))


j = int(input())
for i in range(1,11):
    print('{} * {} = {}'.format(j,i,j*i))


