from bs4 import BeautifulSoup
from collections import defaultdict

import requests


def test_parse_animals():
    html = '''
    <div lang="ru" dir="ltr" class="mw-content-ltr">
    <div class="mw-category mw-category-columns">
        <div class="mw-category-group">
        <h3>А</h3>
        <ul>
            <li>
            <a href="/wiki/Аардоникс" title="Аардоникс">Аардоникс</a>
            </li>
            <li>
            <a href="/wiki/Абботины" title="Абботины">Абботины</a>
            </li>
            <li>
            </li>
        </ul>
        </div>
    </div>
    </div>
    '''
    soup = BeautifulSoup(html, "html.parser")
    animal_list = soup.select("div.mw-category-columns a")
    animal_names = [ i.text for i in animal_list]
    assert animal_names == ["Аардоникс", "Абботины"]



def test_count_animals():
    name = ["Аардоникс","Абботины","Сова","Собака","анаконда"]
    counter = defaultdict(int)
    for i in name:
        counter[i[0].upper()]+=1
    assert counter["А"] == 3
    assert counter["С"] == 2


def test_wikipedia_response():
    url = "https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту"
    response = requests.get(url)
    assert response.status_code == 200