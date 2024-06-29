import json
from os import path

import requests
from src.parser import Parser


path_to_project = path.abspath(__file__)[:-15]
file_name = r'data\loaded_data.json'
# Путь до файла loaded_data.json
file_path = f'{path_to_project}{file_name}'


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
        self.params['text'] = keyword  # ['job']
        while self.params.get('page') != 10:
            response = requests.get(self._url, headers=self._headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

        # with open(file=file_path, mode='wt', encoding='UTF-8') as file:
        #     file.write(json.dumps(self.vacancies))


# hh_api = HHruAPI('')
# hh_api.load_vacancies('Java')

# with open(file=file_path, mode='rt', encoding='UTF-8') as file:
#     data = json.loads(file.readline())
#
# index = 1
# for item in data:
#     print(f'{index}: {item.get('name')} {item.get('salary')}')
#     index += 1

