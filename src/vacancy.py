class Vacancy:
    """Класс для работы с вакансиями"""
    name: str
    alternate_url: str
    pay: int
    currency: str
    working_days: str
    index: int

    index = -1

    def __init__(self, name, salary, working_days, alternate_url):
        if salary is None:
            salary = {}
        self.name = name if name else 'Название не указано'
        self.currency = salary.get('currency') if salary.get('currency') else 'Валюта не указана'
        self.pay = salary.get('from') if salary.get('from') else 0
        self.working_days = working_days if working_days else 'График не указан'
        self.alternate_url = alternate_url if alternate_url else 'Ссылка не указана'
        Vacancy.index += 1
        self.index = Vacancy.index

    def __repr__(self):
        """Представление для отладки"""
        return f"{self.__class__.__name__}('{self.name}', {self.pay}, '{self.working_days}', '{self.alternate_url}')"

    def __str__(self):
        """Представление для пользователя"""
        return f'{self.name}, {self.pay} {self.currency}, {self.working_days}, {self.alternate_url}'

    @classmethod
    def cast_to_object_list(cls, items):
        """Преобразование набора данных из JSON в список объектов"""
        object_list = []
        for item in items:
            vacancy = Vacancy(item.get('name'), item.get('salary'), item.get('working_days'), item.get('alternate_url'))
            if vacancy.pay == 0 or vacancy.currency == 'Валюта не указана':
                del vacancy
                Vacancy.index -= 1
            else:
                object_list.append(vacancy)
        return object_list

    def compare_pay(self, other):
        """Если буду работать с разными валютами понадобится проверка"""
        if isinstance(other, self.__class__):
            difference = self.pay - other.pay
            if self.pay < other.pay:
                return f'На второй работе зарплата выше на {abs(difference)} {self.currency}'
            else:
                return f'На второй работе зарплата ниже на {abs(difference)} {self.currency}'
        raise TypeError('Сравнивать можно только с экземплярами класса Vacancy')
