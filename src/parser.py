from abc import ABC, abstractmethod


class Parser(ABC):
    """
    Абстрактный класс шаблон для классов для работы с API
    """
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def load_vacancies(self, *args, **kwargs):
        pass
