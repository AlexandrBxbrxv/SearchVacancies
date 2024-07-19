class FindVacancyConstructor:
    """Содержит методы поиска по критериям"""
    def __init__(self, vacancies):
        self.vacancies = vacancies

    def find_vacancy(self, key, value):
        """Выбирает и запускает метод поиска, возвращает список объектов соответствующих value"""
        if key == 'Название':
            return self.__by_name(value)
        if key == 'Зарплата':
            return self.__by_pay(value)
        if key == 'Локация':
            return self.__by_area_name(value)

    def __by_name(self, value):
        """Записывает на возврат, если value найдено внутри названия вакансии"""
        result = []
        for item in self.vacancies:
            if value in item['name']:
                result.append(item)
        return result

    def __by_pay(self, value):
        """Записывает на возврат, если зарплата вакансии больше либо равна value"""
        result = []
        for item in self.vacancies:
            if item['salary']['from'] >= value:
                result.append(item)
        return result

    def __by_area_name(self, value):
        """Записывает на возврат, если название локации вакансии совпадает с value"""
        result = []
        for item in self.vacancies:
            if item['area']['name'] == value:
                result.append(item)
        return result
