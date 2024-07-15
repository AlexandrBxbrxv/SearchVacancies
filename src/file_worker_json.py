import json
from os import path

from src.file_worker import FileWorker


class FileWorkerJson(FileWorker):
    """Класс для сохранения данных в файлы.json
    во время работы программы составляет список сохраняемых вакансий,
     перед прекращением программы сохраняет список в файл"""
    file_path: str
    vacancy_list: list

    def __init__(self, file_path=None):
        self.file_path = file_path if file_path else r'data\saved_vacancies.json'
        path_to_project = path.abspath(__file__)[:-23]
        self.__full_file_path = f'{path_to_project}{self.file_path}'
        self.vacancy_list = []
        super().__init__(file_path)

    def add_vacancy(self, vacancy):
        """Запись данных в список на сохранение"""
        vacancy_dict = {
         'id': vacancy.index,
         'name': vacancy.name,
         'salary': {'from': vacancy.pay, 'currency': vacancy.currency},
         'area': {'name': vacancy.area_name},
         'alternate_url': vacancy.alternate_url
        }

        self.vacancy_list.append(vacancy_dict)
        self.__save()

    def find_vacancies_pay(self, value):
        """Выдает список вакансий зарплата которых >= value"""
        result = []
        saved = self.load()
        for pos in saved:
            if pos['salary']['from'] >= value:
                result.append(pos)
        return result

    def delete_vacancy(self, vacancy_id):
        """Удаление вакансии из списка на сохранение"""
        for item in self.vacancy_list:
            if item['id'] == vacancy_id:
                self.vacancy_list.remove(item)

    def __save(self):
        """Записывает список в файл saved_vacancies.json"""
        with open(file=self.__full_file_path, mode='w', encoding='UTF-8') as file:
            file.write(json.dumps(self.vacancy_list, indent=2))

    def load(self):
        """Загружает список вакансий из файла saved_vacancies.json"""
        with open(file=self.__full_file_path, mode='r', encoding='UTF-8') as file:
            return json.loads(file.read())
