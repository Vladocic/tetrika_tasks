import requests


url = f"https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту&from=%3Cb%3E{i}%3C%2Fb%3E"
i = "A"
requests.get(url=url)