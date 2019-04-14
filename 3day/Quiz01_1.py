# Quiz01_1.py
    
items = {"콜라":1000,"사이다":900,"씨그램":500,"우유":700,"활명수":800}

print("=== 음료 자판기 입니다 ====")
print("[콜라][사이다][씨그램][우유][활명수] 중 선택")
print("복수 선택 시 --> 예) 사이다,우유 ")

def pItems(*args1,**args2) :
    price = 0
    for i in args1:
        price = price + args2[i.strip()]
    return price

# 선택목록 item, 가격 price
item = input() # 사이다,우유
items2 = item.strip().split(',')

price = pItems(*items2,**items)
print("가격 : {0} 원".format(price) )