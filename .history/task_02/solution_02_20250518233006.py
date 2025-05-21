import requests
from bs4 import BeautifulSoup
from collections import defaultdict

albhabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
animals = set()
animal_counter = defaultdict(int)

url = "https://ru.wikipedia.org"
add_url = "/w/index.php?title=Категория:Животные_по_алфавиту&from=%3Cb%3EA%3C%2Fb%3E"
count = 0

while True:
    response = requests.get(url=url+add_url)
    if response.status_code != 200:
        raise Exception(f"Ошибка при запросе к {url}: статус {response.status_code}")

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.select("div.mw-category-columns a")
    for i in table:
        animal_name
        if i.text[0].upper() not in albhabet:
            break 
        if i.text not in animals:
            animals.add(i.text)
            animal_counter[i.text[0].upper()] += 1  

    next_link = soup.find("a", string="Следующая страница")
    if not next_link:
        break
    add_url = next_link["href"]
    count = count+1
    print(f"Парсим страницу: {count}")


print(animals)
print(animal_counter)



