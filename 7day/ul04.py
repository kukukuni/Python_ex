# ul04.py
# Test02.html
# --> body
from bs4 import BeautifulSoup
f1 = open("web/Test02.html","r", encoding='utf-8')
bs = BeautifulSoup(f1,"html.parser")
body_tag = bs.find("body")
# print(body_tag)
tag_list = (body_tag.find_all(['p','img']))
for tag in tag_list : print(tag)
# print(tag_list)
f1.close()