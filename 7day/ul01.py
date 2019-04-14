# ul01.py
from bs4 import BeautifulSoup
f1 = open('HTML/Test00.html','r',encoding="utf-8")
# bs = BeautifulSoup(f1,"html.parser")
# fdata = f1.read()
# print(fdata)
bs = BeautifulSoup(f1,"html.parser") # html.parser, xml.parser html해석이 가능해짐
f1.close()
# print(type(bs))
print(bs)
print(bs.prettify())  #태그를 인덴트해서 정렬


