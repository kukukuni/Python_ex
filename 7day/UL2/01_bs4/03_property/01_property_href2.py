import bs4

html_str = """
<html>
    <body>
        <ul class="ko">
            <li>
                <a href="https://www.naver.com/">네이버</a>
            </li>
            <li>
                <a href="https://www.daum.net/">다음</a>
            </li>
        </ul>
        <ul class="sns">
            <li>
                <a href="https://www.google.com/">구글</a>
            </li>
            <li>
                <a href="https://www.facebook.com/">페이스북</a>
            </li>
        </ul>
    </body>
</html>
"""

bs_obj = bs4.BeautifulSoup(html_str, "html.parser")
atag = bs_obj.find("a")
print(atag['href']) #key값을 이용하여 value인 링크를 따옴. a.text면 네이버가 나왔을 것임

