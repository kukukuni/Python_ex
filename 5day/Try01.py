# Try01.py
# Try except else finally
print('숫자 입력')
x = input()

try:                        #위에서 일부러 0으로 나누는 등으로 에러 메세지 찾음
    print(10 / int(x))
except ZeroDivisionError as e:
    print('숫자를 입력하세요')
    print(e)
except ValueError as e:
    print('숫자를 입력하세요')
    print(e)
else:
    print('참잘했어요')      #정상적으로 실행되었을때
finally:
    print('어쨌든 완료')     #언제가 끝에 나오길 바랄때
