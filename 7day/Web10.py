# Web10.py

import urllib.request
import bs4

url = "http://news.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")
newsnow_txarea = bs_obj.find("ul", {"class":"newsnow_txarea"})
lis = newsnow_txarea.findAll("li")

for li in lis:
    strong = li.find("strong")
    print(strong.text)
