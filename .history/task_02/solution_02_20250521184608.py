import requests
from bs4 import BeautifulSoup
import csv

alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
animals = set()
animal_counter = {letter: 0 for letter in alphabet}

url = "https://ru.wikipedia.org"
add_url = "/w/index.php?title=Категория:Животные_по_алфавиту&from=%3Cb%3EA%3C%2Fb%3E"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}
count = 0

while True:
    response = requests.get(url=url+add_url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Ошибка при запросе к {url}: статус {response.status_code}")
    
    soup = BeautifulSoup(response.text, "html.parser")
    animal_list = soup.select("div.mw-category-columns a")
    for i in animal_list:
        animal_name = i.text
        if not animal_name or animal_name[0].upper() not in alphabet:
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


with open("animals.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Letter", "Count"])
    for letter in alphabet:
        writer.writerow([letter, ])


