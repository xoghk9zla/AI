# 웹브라우저로 HTML 구조 확인하기 7단계를 활용하여 필요한 데이터 스크래핑하기
from bs4 import BeautifulSoup
import urllib.request as req

url = "https://finance.naver.com/marketindex/"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

# #mw-content-text 바로 아래에 있는
# ul 태그 바로 아래에 있는
# li 태그 아래에 있는
# a 태그를 모두 선택합니다.
a_list = soup.select("#content > div.section_news > div > ul > li:nth-of-type(2) > p > a")

for a in a_list:
    ExchangeRate = a.string

print("- 1달러 -> {0}원".format(ExchangeRate))

