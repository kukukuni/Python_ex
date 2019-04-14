# Func06.py


a = {'사과':'apple',
     '포도':'grape',
     '바나나':'banana',
     '컵':'cup',
     '물':'water'}

def pDict(**d):  #*두개를 붙이면 key:value쌍이라서 주소가 두개짜리가 들어온다
    for i in d.items(): print(i)    #라고 이해 간편하게는 키와벨류가 쌍으로
                                    #들어오는 형태(Dict)이구나로 이해

pDict(**a)
pDict(사과='apple',포도='grape',바나나='banana')
                        #위에서 보면 사과 같은거는 변수로 인식되어서
                        #'사과'면 에러가 된다.
                        #마치 def sum(num=4)이럴때 num을 'num'안하는 것처럼
pDict(**{'컵':'cup','물':'water'})
