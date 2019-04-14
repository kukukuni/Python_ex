# Web24.py

import requests
from bs4 import BeautifulSoup

url = "http://music.naver.com/listen/history/index.nhn?type=DOMESTIC&year=2017&month=12&week=1&page=1"    
# url = "http://music.naver.com/listen/history/index.nhn?type=DOMESTIC&year=2017&month=12&week=1&page=2"
# url = "http://music.naver.com/listen/top100.nhn?domain=TOTAL&page=1"
    
html_music = requests.get(url).text
soup_music = BeautifulSoup(html_music, "lxml")

titles = soup_music.select('a._title span.ellipsis') 
artists = soup_music.select('td._artist a')

music_titles = [title.get_text() for title in titles]
music_artists = [artist.get_text().strip() for artist in artists]

for k in range(7):
    print("{0}: {1} / {2}".format(k+1, music_titles[k], music_artists[k]))

music_titles_artists={}
order = 0

for (music_title, music_artist) in zip(music_titles, music_artists):
    order = order + 1
    music_titles_artists[order] = [music_title, music_artist]

print(music_titles_artists[1])

print(music_titles_artists[2])

