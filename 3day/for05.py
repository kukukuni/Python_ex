# for05.py
'''
1: *
2: **
3: ***
4: ****
5: *****
'''

for i in range(1,6):
    print(i,end=': ')
    for j in range(1,i+1):
        print('*',end='')
    print()

for i in range(1,20,5):
    for j in range(i,i+5):
        print(j,end=' ')
    print()

for i in range(1,21):
    if not (i%5):
        print(i)
    else:
        print(i,end=' ')

