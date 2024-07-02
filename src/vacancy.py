class Vacancy:
    """Класс для работы с вакансиями"""
    name: str
    link: str
    pay: int
    currency: str
    working_days: str
    # description: str
    # employment: str
    # area: str

    def __init__(self, name, salary, working_days, link):
        self.name = name if name else 'Название не указано'
        self.currency = salary['currency'] if salary['currency'] else 'Валюта не указана'
        self.pay = salary['from'] if salary['from'] else 0
        self.working_days = working_days if working_days else 'График не указан'
        self.link = link if link else 'Ссылка не указана'

    def __repr__(self):
        """Представление для отладки"""
        return f"{self.__class__.__name__}('{self.name}', {self.pay}, '{self.working_days}', '{self.link}')"

    def __str__(self):
        """Представление для пользователя"""
        return f'{self.name}, {self.pay} {self.currency}, {self.working_days}, {self.link}'

    def cast_to_object_list(self, items):
        """Преобразование набора данных из JSON в список объектов"""
        for item in items:
            self.__init__(item['name'], item['salary'], item['working_days'], item['alternate_url'])

    def compare_pay(self, other):
        """Если буду работать с разными валютами понадобится проверка"""
        if isinstance(other, self.__class__):
            difference = self.pay - other.pay
            if self.pay < other.pay:
                return f'На второй работе зарплата выше на {abs(difference)} {self.currency}'
            else:
                return f'На второй работе зарплата ниже на {abs(difference)} {self.currency}'
        raise TypeError('Сравнивать можно только с экземплярами класса Vacancy')


if __name__ == '__main__':

    sal1 = {'currency': None, 'from': 5000}
    sal2 = {'currency': 'RUB', 'from': 7000}
    vac1 = Vacancy('pudge', sal1, 'ПН-ПТ', 'link//link231')
    vac2 = Vacancy('rudge', sal2, 'ПН-ПТ', 'link//link231')
    print(vac1)
    print(vac2)
    print(vac1.compare_pay(vac2))


"Создать класс для работы с вакансиями. В этом классе самостоятельно определить атрибуты,"
"такие как название вакансии, ссылка на вакансию, зарплата, краткое описание или требования и т. п."
"(всего не менее четырех атрибутов)."
"Класс должен поддерживать методы сравнения вакансий между собой по зарплате и валидировать данные,"
"которыми инициализируются его атрибуты.)"

"Способами валидации данных может быть проверка, указана или нет зарплата."
"В этом случае выставлять значение зарплаты 0 или «Зарплата не указана» в зависимости от структуры класса."
