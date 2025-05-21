import requests
from bs4 import BeautifulSoup


albhabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
animals = set()
url = f"https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту&from=%3Cb%3EA%3C%2Fb%3E"

url = "https://ru.wikipedia.org"
add_url = "w/index.php?title=Категория:Животные_по_алфавиту&from=%3Cb%3EA%3C%2Fb%3E"

while True:
    response = requests.get(url=url+add_url)
    if response.status_code != 200:
        raise Exception(f"Ошибка при запросе к {url}: статус {response.status_code}")
    # print(response.text)

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.select("div.mw-category a")

    for i in table:
        animals.add(i.text)

    next_link = soup.find('a', text='Следующая страница')
    print(next_link["href"])

    /w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%90%D0%B7%D0%B8%D0%B0%D1%82%D1%81%D0%BA%D0%B8%D0%B5+%D1%82%D0%BE%D0%BA%D0%B8&subcatfrom=%3Cb%3EA%3C%2Fb%3E&filefrom=%3Cb%3EA%3C%2Fb%3E
    /w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&filefrom=%D0%AF%D1%8E&subcatfrom=%D0%AF%D1%8E&pagefrom=Aaaaba#mw-pages
    #mw-pages
    https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту&pagefrom=Азиатские+токи&subcatfrom=%3Cb%3EА%3C%2Fb%3E&filefrom=%3Cb%3EА%3C%2Fb%3E#mw-pages

    # pagefrom=Aaaaba


