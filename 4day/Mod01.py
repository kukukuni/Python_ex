# Mod01.py
#<-- /MyCalc01 /Calc01.py를 참조
print('name : {}'.format(__name__))

# import MyCalc01.Calc01
# from MyCalc01 import Calc01
# from MyCalc01 import Calc01 as c
from MyCalc01.Calc01 import *   #from 폴더.파일 import *


x = 200; y = 100;
# MyCalc01.Calc01.Sum(x,y)
# Calc01.Sum(x,y)
# c.Sum(x,y)
Sum(200,100)