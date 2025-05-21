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

animals = ()
for i in table:
    print(i.text)
    an

