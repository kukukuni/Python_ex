# Web20.py

import requests
from bs4 import BeautifulSoup

url = "https://www.alexa.com/topsites/countries/KR"

html_website_ranking = requests.get(url).text
soup_website_ranking = BeautifulSoup(html_website_ranking, "lxml")

# p 태그의 요소 안에서 a 태그의 요소를 찾음
website_ranking = soup_website_ranking.select('p a')

print(website_ranking[0:6])

print(website_ranking[0].get_text())
website_ranking_address = [website_ranking_element.get_text() for website_ranking_element in website_ranking]

print(website_ranking_address[0:6])