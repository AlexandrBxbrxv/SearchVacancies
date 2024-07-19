import pytest

from src.vacancy import Vacancy


@pytest.fixture
def link():
    return 'https://somelink.com'


@pytest.fixture
def salary_none():
    return None


@pytest.fixture
def salary_currency_none():
    return {'currency': 'RUR', 'from': None}


@pytest.fixture
def salary_none_pay30():
    return {'currency': None, 'from': 30_000}


@pytest.fixture
def salary_currency_pay90():
    return {'currency': 'RUR', 'from': 90_000}


@pytest.fixture
def vacancy_factory30(salary_none_pay30, link):
    return Vacancy('Слесарь', salary_none_pay30, None, link)


@pytest.fixture
def vacancy_developer90(salary_currency_pay90, link):
    return Vacancy('Python Разработчик', salary_currency_pay90, 'ПН-ПТ', link)
