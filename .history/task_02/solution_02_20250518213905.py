import html
import requests
from bs4 import BeautifulSoup

alphabet = ["A", ""]
i = "A"
url = f"https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту&from=%3Cb%3E{i}%3C%2Fb%3E"
header = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url=url)
if response.status_code != 200:
    raise
# print(response.text)

soup = BeautifulSoup(html, "lxml")
table = soup.find('table', class_="mw-category-grou")

print(table)