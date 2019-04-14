# ul00.py

from urllib.request import urlopen

# url = 'https://www.naver.com/'
url = 'https://www.daum.net/'
html = urlopen(url)
status = html.getheaders()
# for s,p in status:
#     print(s+' '+p)  #튜플 형태이므로 Dic에 담을 수 있다.

print(html.read())