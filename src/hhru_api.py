import json
from os import path

import requests
from src.parser import Parser


class HHruAPI(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self, file_worker):  # Класс для работы с файлами
        self._url = 'https://api.hh.ru/vacancies'
        self._headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 10}  # тег работы, страница, вакансий на странице
        self.vacancies = []
        super().__init__(file_worker)

    def load_vacancies(self, keyword):
        """Загружает с сайта api.hh.ru вакансии и складывает их в список vacancies"""
        self.params['text'] = keyword  # ['job']
        while self.params.get('page') != 10:
            response = requests.get(self._url, headers=self._headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
