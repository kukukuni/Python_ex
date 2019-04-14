# /MyCalc01 / Calc01.py
if __name__ == '__main__':
    print("직접 실행하지 마세요")            #직접실행을 하면 얘 자체 이름이 main이 되므로 이를 막음
else :                                    #main이 아니고 참조가 되도록
    print('name: {0}'.format(__name__))
    def Sum(a,b): print(a+b)
    def Sub(a,b): print(a-b)
    def Mul(a,b): print(a*b)
    def Div(a,b): print(a/b)

