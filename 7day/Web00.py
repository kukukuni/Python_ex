# Web00.py

import webbrowser
# url = 'www.naver.com'
print("검색할 단어 입력")
search_word = input()
naver_search_url ='https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query='
# search_word = '파이썬'
# webbrowser.open(url)
webbrowser.open(naver_search_url + search_word)