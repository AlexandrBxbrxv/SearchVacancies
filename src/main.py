from hhru_api import HHruAPI
from vacancy import Vacancy
from file_worker_json import FileWorkerJson

hh = HHruAPI('')
hh.load_vacancies('Python')

print([i['salary'] for i in hh.vacancies])

# vacancies = Vacancy.cast_to_object_list(hh.vacancies, hh.vacancies)
#
# print(vacancies)
