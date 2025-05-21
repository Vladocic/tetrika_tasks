import pytest


def test_parse_animals():
    pass



def test_filter_by_letter():
    pass


from collections import defaultdict

def test_count_animals():
    pass


def test_wikipedia_response():
    url = "https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту"
    response = requests.get(url)
    assert response.status_code == 200