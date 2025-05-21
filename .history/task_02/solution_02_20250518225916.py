import requests
from bs4 import BeautifulSoup


albhabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
animals = set()

url = "https://ru.wikipedia.org"
add_url = "/w/index.php?title=Категория:Животные_по_алфавиту&from=%3Cb%3EA%3C%2Fb%3E"



while True:
    response = requests.get(url=url+add_url)
    if response.status_code != 200:
        raise Exception(f"Ошибка при запросе к {url}: статус {response.status_code}")

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.select("div.mw-category-columns a")
    print(table[3].text)
    for i in table:
        if i.text[0].upper() not in albhabet:
            break 
        animals.add(i.text)

    next_link = soup.find('a', text='Следующая страница')
    add_url = next_link["href"]
    print(next_link["href"])

aba = "fff"
print(aba[0])
