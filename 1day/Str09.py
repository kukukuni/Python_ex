# Str09.py

'''
print('숫자 1번 입력'); n1 = int(input())
print('숫자 2번 입력'); n2 = int(input())
print(n1+n2)

print('숫자 2개 입력')
n1, n2 = input().split(',')
print(int(n1)+int(n2))

print('숫자 2개 입력')
n1, n2 = map(int,input().split(','))
print(n1+n2)
'''

n1, n2 = map(int,input('숫자 2개 입력\n').split(','))
print(n1+n2)
