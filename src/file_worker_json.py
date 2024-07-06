import json
from os import path

from src.file_worker import FileWorker


class FileWorkerJson(FileWorker):
    """Класс для сохранения данных в файлы.json"""

    def __init__(self, file_path=None):
        self.file_path = file_path if file_path else r'data\loaded_data.json'
        path_to_project = path.abspath(__file__)[:-23]
        self.full_file_path = f'{path_to_project}{self.file_path}'
        super().__init__(file_path)

    def add_vacancy(self, vacancy):
        """Запись данных в loaded_data.json"""

        with open(file=self.full_file_path, mode='a', encoding='UTF-8') as file:
            file.write(json.dumps(vacancy))

    def delete_vacancy(self, vacancy):
        with open(file=self.full_file_path, mode='w', encoding='UTF-8') as file:
            file.truncate(vacancy)


"""Определить абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл,
получения данных из файла по указанным критериям и удаления информации о вакансиях. Создать класс для сохранения
информации о вакансиях в JSON-файл. Дополнительно, по желанию, можно реализовать классы для работы с другими форматами,
например с CSV- или Excel-файлом, с TXT-файлом."""

"""Данный класс выступит в роли основы для коннектора, заменяя который (класс-коннектор),
можно использовать в качестве хранилища одну из баз данных или удаленное хранилище со своей
специфической системой обращений.
В случае если какие-то из методов выглядят не используемыми для работы с файлами,
то не стоит их удалять. Они пригодятся для интеграции к БД. Сделайте заглушку в коде."""


if __name__ == '__main__':
    file_worker_json = FileWorkerJson()

    with open(file='data.json', mode='w', encoding='UTF-8') as file:
        file.write('')

