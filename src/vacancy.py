class Vacancy:
    """Класс для работы с вакансиями"""
    name: str
    alternate_url: str
    pay: int
    currency: str
    area_name: str
    index: str

    def __init__(self, index, name, salary, area, alternate_url):
        if salary is None:
            salary = {}
        if area is None:
            area = {}
        self.index = index
        self.name = name if name else 'Название -'
        self.currency = salary.get('currency') if salary.get('currency') else 'Валюта -'
        self.pay = salary.get('from') if salary.get('from') else 0
        self.area_name = area.get('name') if area.get('name') else 'Локация -'
        self.alternate_url = alternate_url if alternate_url else 'Ссылка -'

    def __repr__(self):
        """Представление для отладки"""
        return (f"{self.__class__.__name__}('{self.index}, {self.name}', {self.pay}, '{self.area_name}',"
                f" '{self.alternate_url}')")

    def __str__(self):
        """Представление для пользователя"""
        return f'id:{self.index}, {self.name}, {self.pay} {self.currency}, {self.area_name}, {self.alternate_url}'

    @classmethod
    def cast_to_object_list(cls, items):
        """Преобразование набора данных из JSON в список объектов"""
        object_list = []
        for item in items:
            vacancy = Vacancy(item.get('id'), item.get('name'),
                              item.get('salary'), item.get('area'), item.get('alternate_url'))
            if vacancy.pay == 0 or vacancy.currency == 'Валюта -':
                del vacancy
            else:
                object_list.append(vacancy)
        return object_list

    def convert_currency(self, currency):
        """Переводит зарплату в рубли по курсу валюты"""
        converted_pay = round(self.pay * (currency['Value'] / currency['Nominal']), 2)
        self.pay = converted_pay
        self.currency = "RUR"

    def compare_pay(self, other):
        """Сравнивает 2 вакансии по зарплате"""
        if isinstance(other, self.__class__):
            if self.currency == other.currency:
                difference = round(self.pay - other.pay, 2)
                if self.pay < other.pay:
                    return f'На второй работе зарплата выше на {abs(difference)} {self.currency}'
                else:
                    return f'На второй работе зарплата ниже на {abs(difference)} {self.currency}'
            else:
                return 'Не возможно сравнить разные валюты'
        raise TypeError('Сравнивать можно только с экземплярами класса Vacancy')
