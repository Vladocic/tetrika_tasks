import html
import requests
from bs4 import BeautifulSoup

alphabet = ["A", ""]
letter = "A"
url = f"https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту&from=%3Cb%3EA%3C%2Fb%3E"



header = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url=url)
if response.status_code != 200:
    raise Exception(f"Ошибка при запросе к {url}: статус {response.status_code}")
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
table = soup.select("div.mw-category a")

print(table)


<a href="/wiki/%D0%90%D0%B7%D0%B8%D0%B0%D1%82%D1%81%D0%BA%D0%B8%D0%B5_%D1%81%D1%83%D1%85%D0%BE%D0%BF%D1%83%D1%82%D0%BD%D1%8B%D0%B5_%D1%87%D0%B5%D1%80%D0%B5%D0%BF%D0%B0%D1%85%D0%B8" 
title="Азиатские сухопутные черепахи">Азиатские сухопутные черепахи</a>