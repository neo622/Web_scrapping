import csv
import requests 
import re
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}

# filename = "잡코리아 공채 정보 데이터.csv"
# f = open(filename, "w", encoding="utf-8-sig", newline="")
# writer = csv.writer(f)
# title="회사명 채용내용 채용사이트 채용유형 학력사항 기한".split("\t")
# writer.writerow(title)

for i in range(1,2):
    url = f"https://www.jobkorea.co.kr/Starter/?JoinPossible_Stat=0&schOrderBy=0&LinkGubun=0&LinkNo=0&schType=0&schGid=0&Page={i}"
    res = requests.get(url, headers=headers) 
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
               
    data_rows = soup.find("ul",attrs={"class":"filterList"}).find_all("li")

    for row in data_rows:
        columns1 = row.find("div", attrs = {"class":"coTit"})
        columns2 = row.find("div", attrs = {"class": "info"})
        columns3 = row.find("div", attrs = {"class":"sDesc"})
        columns4 = row.find("span", attrs = {"class":re.compile("^day")})
        
        data1 = [columns1.a.get_text()]
        data2 = [columns2.a.get_text().strip()]
        data3 = ["https://www.jobkorea.co.kr/" + columns2.a["href"]]
        data4 = [columns3.strong.get_text().strip()]
        data5 = [columns3.span.get_text().strip()]
        data6 = [columns4.get_text().strip()]

        data = data1 + data2 + data3 + data4 + data5 + data6
        print(data)    

