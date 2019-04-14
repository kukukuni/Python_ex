# Web22.py

import requests  
from bs4 import BeautifulSoup
# 데이터 분석 패키지 --> numpy(배열, 행렬연산), pandas(data frame)
import pandas as pd

url = "https://www.alexa.com/topsites/countries/KR"

html_website_ranking = requests.get(url).text
soup_website_ranking = BeautifulSoup(html_website_ranking, "lxml")

# p 태그의 요소 안에서 a 태그의 요소를 찾음
website_ranking = soup_website_ranking.select('p a')
website_ranking_address = [website_ranking_element.get_text() for website_ranking_element in website_ranking]

print("[Top Sites in South Korea]")
for k in range(6):
    print("{0}: {1}".format(k+1, website_ranking_address[k]))

website_ranking_dict = {'Website': website_ranking_address}
df = pd.DataFrame(website_ranking_dict, columns=['Website'], index=range(1,len(website_ranking_address)+1))
df[0:6]