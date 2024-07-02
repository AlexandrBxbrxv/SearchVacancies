from abc import ABC, abstractmethod


class FileWorker(ABC):
    """Абстрактный класс для создания классов для работы с файлами"""
    def __init__(self, file_path):
        pass

    @abstractmethod
    def write_down(self, data):
        pass
