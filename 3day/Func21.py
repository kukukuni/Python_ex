# Func21.py

def f1(x):
    return ((x > 5) and ((x%2)==1))

a = [8,3,2,10,15,7,1,9,0,11]
b = list(filter(f1,a))
print(b)

from functools import reduce

def f2(x,y):
    return x+y

c = [1,2,3,4,5]
d = reduce(f2,c)
print(d)
