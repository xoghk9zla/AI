# 라이브러리 읽어 들이기
import urllib.request

# URL과 저장 경로 지정하기
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test1.png"

# 다운로드
urllib.request.urlretrieve(url, savename)
print("저장되었습니다...!")