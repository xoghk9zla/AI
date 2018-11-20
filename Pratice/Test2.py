import openpyxl
import csv, codecs

# 엑셀 파일 열기く --- (※1)
filename = "stats_104102.xlsx"
savename = "Test2.xlsx"
book = openpyxl.load_workbook(filename)

# 맨 앞의 시트 추출하기 --- (※2)
sheet = book.worksheets[0]

# 시트의 각 행을 순서대로 추출하기 --- (※3)
data = []
for row in sheet.rows:
    data.append([
        row[0].value,
        row[9].value
        ])

# 필요 없는 줄(헤더, 연도, 계) 제거하기
del data[0]
del data[1]
del data[2]

data.pop(0)

# 데이터를 인구 순서로 정렬합니다.
data = sorted(data, key=lambda x: x[1])

for i, a in enumerate(data):
    print(i + 1, a[0], int(a[1]))
    # 65번째 열에 작성
    # 21번째 22번째 행에 작성
    sheet[str(chr(i + 65)) + "21"] = a[0]
    sheet[str(chr(i + 65)) + "22"] = int(a[1])
    cell = sheet[str(chr(i + 65)) + "21"]
    cell = sheet[str(chr(i + 65)) + "22"]


with codecs.open(savename, "w", "euc_kr ") as fp:
    for i, a in enumerate(data):
        writer = csv.writer(fp, delimiter=",", quotechar='"')
        writer.writerow([i + 1, a[0], int(a[1])])
