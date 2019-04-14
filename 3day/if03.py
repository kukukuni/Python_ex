# if03.py

# 숫자를 입력받으세요
# 입력숫자가 0 이면 '0은 안되요' 출력

import sys
print('숫자를 입력하세요')
i = int(input())
# i == 0 :

if i:
    print(10/i)
    sys.exit(0) #어디서나 종료

print('0은 안되요')



