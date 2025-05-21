from bs4 import BeautifulSoup
import pytest
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
            <!-- Следующий элемент... -->
            </li>
        </ul>
        </div>
    </div>
    </div>
'''
    soup = BeautifulSoup(html, "html.parser")
    animal_list = soup.select("div.mw-category-columns a")
    for i in animal_list:
        animal_name = i.text
    assert



def test_filter_by_letter():
    pass



def test_count_animals():
    pass


def test_wikipedia_response():
    url = "https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту"
    response = requests.get(url)
    assert response.status_code == 200