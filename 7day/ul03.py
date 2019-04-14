# ul03.py
from bs4 import BeautifulSoup
f1 = open('web/Test01.html','r',encoding="utf-8")
bs = BeautifulSoup(f1,"html.parser") #html.parser를 이용해 태그로 읽는게 가능해짐

# bsList = bs.find_all("p")
# print(bsList)
# for bs in bsList : print(bs)
# print(bsList[1])
a = bs.find("head")
print(a.find("title"))


f1.close()