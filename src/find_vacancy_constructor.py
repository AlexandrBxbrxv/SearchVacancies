class FindVacancyConstructor:
    """Содержит методы поиска по критериям"""
    def __init__(self, vacancies_dict):
        self.__vacancies_dict = vacancies_dict

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
        for item in self.__vacancies_dict:
            if value.lower() in item['name'].lower():
                result.append(item)
        return result

    def __by_pay(self, value):
        """Записывает на возврат, если зарплата вакансии больше либо равна value"""
        result = []
        for item in self.__vacancies_dict:
            if item['salary']['from'] >= value:
                result.append(item)
        return result

    def __by_area_name(self, value):
        """Записывает на возврат, если value найдено внутри названия локации"""
        result = []
        for item in self.__vacancies_dict:
            if value.lower() in item['area']['name'].lower():
                result.append(item)
        return result
