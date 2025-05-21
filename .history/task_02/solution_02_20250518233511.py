import requests
from bs4 import BeautifulSoup
from collections import defaultdict

albhabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
animals = set()
animal_counter = defaultdict(int)

for

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
        animal_name = i.text
        if animal_name[0].upper() not in albhabet:
            break 
        if animal_name not in animals:
            animals.add(animal_name)
            animal_counter[animal_name[0].upper()] += 1  

    next_link = soup.find("a", string="Следующая страница")
    if not next_link:
        break
    add_url = next_link["href"]
    count = count+1
    print(f"Парсим страницу: {count}")


print(animals)
print(animal_counter)

afa = {'А': 1299, 'Б': 1779, 'В': 553, 'Г': 1059, 'П': 1884, 'Д': 810, 'Е': 107, 'Ё': 2, 'О': 845, 'Ж': 423, 'Я': 227, 'З': 674, 'И': 368, 'Й': 4, 'К': 2441, 'С': 1913, 'Л': 743, 'М': 1329, 'Н': 500, 'Р': 612, 'Т': 1058, 'У': 287, 'Ф': 203, 'Х': 299, 'Ц': 245, 'Ч': 734, 'Ш': 291, 'Щ': 162, 'Э': 238, 'Ю': 148}

afa.s
