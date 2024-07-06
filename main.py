from src.hhru_api import HHruAPI
from src.vacancy import Vacancy
from src.file_worker_json import FileWorkerJson

hh = HHruAPI()
hh.load_vacancies('Python')


vacancies = Vacancy.cast_to_object_list(hh.vacancies)
print(len(vacancies))
print(vacancies)

file_worker = FileWorkerJson()
file_worker.add_vacancy(vacancies[0])

# # Создание экземпляра класса для работы с API сайтов с вакансиями
# hh_api = HeadHunterAPI()
#
# # Получение вакансий с hh.ru в формате JSON
# hh_vacancies = hh_api.get_vacancies("Python")
#
# # Преобразование набора данных из JSON в список объектов
# vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
#
# # Пример работы конструктора класса с одной вакансией
# vacancy = Vacancy("Python Developer", "", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")
#
# # Сохранение информации о вакансиях в файл
# json_saver = JSONSaver()
# json_saver.add_vacancy(vacancy)
# json_saver.delete_vacancy(vacancy)
