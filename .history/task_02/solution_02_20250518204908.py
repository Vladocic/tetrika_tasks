import requests

i = "A"
url = f"https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту&from=%3Cb%3E{i}%3C%2Fb%3E"
header = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url=url)

print(response.tex)