import pytest
from collections import defaultdict

import requests


def test_parse_animals():
    soup = BeautifulSoup(response.text, "html.parser")
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