# Func07.py
def pSum(ans,*num):
    Result = 0
    for i in num:
        Result += i
    return '{} {}'.format(ans,Result)

## def pSum(*num,ans): 이렇게 되는것은 다른 언어에서는 안되는데
## print(pSum(20,10, s='덧셈')) 이런식으로 지정하면 파이썬에서는 됨.

print(pSum('덧셈',20,10)) # 덧셈 30
print(pSum('덧셈',20,10,5)) # 덧셈 35
print(pSum('덧셈',20,10,5,2)) # 덧셈 37

a = [10,20,30,40,50]
print(pSum('덧셈',*a)) # 덧셈 150
