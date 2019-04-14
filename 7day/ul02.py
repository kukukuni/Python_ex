# ul02.py
from bs4 import BeautifulSoup
from urllib.request import urlopen
url = urlopen("https://www.daum.net")
bs = BeautifulSoup(url,"html.parser")
print(bs.prettify())
