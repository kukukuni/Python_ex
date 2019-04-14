# Mod02.py
#<-- /MyCalc02 / ~~~g
print('name : {}'.format(__name__))
# from MyCalc02 import Sum00
# from MyCalc02 import Sub00
from MyCalc02 import * #기본적으로 안되는데 init이 오버라이드 되어 __all__이 *로 됨
# 여러개 모듈을 한번에 받아오고 싶을때 init을 만들어서 __all__에 리스트형으로 만들어 놓으면 된다.

x = 2000; y = 1000
Sum00.Sum(x,y)
Sub00.Sub(x,y)
