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
        self.name = name if name else 'Не указано'
        self.currency = salary['currency']
        if salary is None:
            self.currency = 'Не указано'
        self.pay = salary['from']
        if salary is None:
            self.pay = 0
        self.working_days = working_days if working_days else 'Не указано'
        self.link = link if link else 'Не указано'

    def __repr__(self):
        """Представление для отладки"""
        return f"{self.__class__.__name__}('{self.name}', {self.pay}, '{self.working_days}', '{self.link}')"

    def __str__(self):
        """Представление для пользователя"""
        return f'{self.name}, {self.pay} {self.currency}, {self.working_days}, {self.link}'

    def compare_pay(self, other):
        """Если буду работать с разными валютами понадобится проверка"""
        try:
            if isinstance(other, self.__class__):
                difference = self.pay - other.pay
                if self.pay < other.pay:
                    return f'На второй работе зарплата выше на {abs(difference)} {self.currency}'
                else:
                    return f'На второй работе зарплата ниже на {abs(difference)} {self.currency}'
        except TypeError('Можно сравнивать только экземпляры класса Vacancy'):
            return 'Ошибка сравнения'


sal1 = {'currency': None, 'from': 5000}
sal2 = {'currency': 'RUB', 'from': 7000}
vac1 = Vacancy('pudge', sal1, 'ПН-ПТ', 'link//link231')
vac2 = Vacancy('rudge', sal2, 'ПН-ПТ', 'link//link231')
print(vac1)
print(vac1.compare_pay(vac2))


"Создать класс для работы с вакансиями. В этом классе самостоятельно определить атрибуты,"
"такие как название вакансии, ссылка на вакансию, зарплата, краткое описание или требования и т. п."
"(всего не менее четырех атрибутов)."
"Класс должен поддерживать методы сравнения вакансий между собой по зарплате и валидировать данные,"
"которыми инициализируются его атрибуты.)"

"Способами валидации данных может быть проверка, указана или нет зарплата."
"В этом случае выставлять значение зарплаты 0 или «Зарплата не указана» в зависимости от структуры класса."
