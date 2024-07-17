import requests
from src.parser import Parser


class CurrencyRequest(Parser):
    """Класс для работы с json страницей курса валют"""
    link: str

    def __init__(self):
        self.link = 'https://www.cbr-xml-daily.ru/daily_json.js'
        super().__init__()

    def load(self):
        """Загружает данные о курсе валют"""
        response = requests.get(self.link)
        return response.json()['Valute']
