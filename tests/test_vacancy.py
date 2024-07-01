import pytest


def test_vacancy_compare_pay_1(vacancy_developer90, vacancy_factory30):
    assert vacancy_developer90.compare_pay(vacancy_factory30) == 'На второй работе зарплата ниже на 60000 RUR'


def test_vacancy_compare_pay_2(vacancy_developer90, vacancy_factory30):
    assert (vacancy_factory30.compare_pay(vacancy_developer90) ==
            'На второй работе зарплата выше на 60000 Валюта не указана')


def test_vacancy_compare_pay_error(vacancy_factory30):
    with pytest.raises(TypeError) as e_info:
        vacancy_factory30.compare_pay(40_000)
