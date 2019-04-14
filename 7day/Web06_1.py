# Web01_1
# HTML_example3.html
from bs4 import BeautifulSoup
html = open('HTML/HTML_example3.html','r',encoding='utf-8')
bs_obj = BeautifulSoup(html,'html.parser')
# print(bs_obj)
html_find = bs_obj.findAll("h1")
print(html_find)
html_dot = bs_obj.html.body.h1
print(html_dot)
css_select = bs_obj.select("body h1") #css함수임.
print(css_select)