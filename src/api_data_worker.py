from os import path


class ApiDataWorker:
    """Работает с данными с сайта hh.ru API"""
    def __init__(self):
        self.__file_path = r'data\api_request.json'
        path_to_project = path.abspath(__file__)[:-22]
        self.full_file_path = f'{path_to_project}{self.__file_path}'

    def save(self, data):
        with open(self.full_file_path, 'w', encoding='UTF-8') as file:
            file.write(data)

    def load(self):
        with open(self.full_file_path, 'r', encoding='UTF-8') as file:
            data = file.read()
        return data
