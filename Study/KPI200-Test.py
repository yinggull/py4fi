from bs4 import BeautifulSoup
from datetime import datetime 
from urllib.request import urlopen

index_cd = "KPI200"

page_n = 1

naver_index = "https://finance.naver.com/sise/sise_index_day.naver?code=KPI200&page=" + str(page_n)

source = urlopen(naver_index).read()

source = BeautifulSoup(source, "lxml")

# print(source.prettify())

td = source.find_all("td")

len(td)

d = source.find_all("td", class_="date")[0].text

print(d)

this_date = datetime.strptime(d, "%Y.%m.%d")

print(this_date)

this_close = source.find_all("tr")[2].find_all("td")[1].text
this_close = this_close.replace(",", "") # 쉼표 제거
this_close = float(this_close)
this_close

# /html/body/div/table[2]/tbody/tr/td[12]/a
total_page = source.find("td", class_="pgRR").find("a")["href"]
print(total_page)

total_page = total_page.split("=")[2]
print(total_page)

