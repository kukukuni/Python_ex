# Quiz01.py
    
Items = {"콜라":1000,"사이다":900,"씨그램":500,"우유":700,"활명수":800}
def bm(a):
    global Items
    result = 0
    c = a.split(',')
    for i in c:
        if i in Items.keys():
             result += Items[i]
    return result


print("=== 음료 자판기 입니다 ====")
print("[콜라][사이다][씨그램][우유][활명수] 중 선택")
print("복수 선택 시 --> 예) 사이다,우유 ")
print(bm(input()))





# 가격: 1600 원









