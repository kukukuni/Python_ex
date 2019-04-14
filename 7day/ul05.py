# ul05.py
# Test02.html
# --> body
from bs4 import BeautifulSoup
import re

f1 = open("web/Test02.html","r",encoding='utf-8')
bs = BeautifulSoup(f1,"html.parser")
tags = bs.find_all(re.compile("^p"))
tags = bs.find_all(align="center")
print(tags)
f1.close()