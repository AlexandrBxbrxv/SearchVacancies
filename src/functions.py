from src.hhru_api import HHruAPI
from src.vacancy import Vacancy
from src.file_worker_json import FileWorkerJson


hh = HHruAPI()
file_worker = FileWorkerJson()


def user_interaction():
    """Функция взаимодействия пользователя с программой."""
    stop = False
    while stop is not True:
        choice_msg = ('1 - Загрузка вакансий с сайта hh.ru\n'
                      '2 - Работа с вакансиями\n'
                      'Прекращение работы - stop\n')
        user_input = input(choice_msg)
        if user_input == 'stop':
            stop = True
        if user_input == '1':
            search_request = input('Введите название работы или интересующий вас критерий: ')
            hh.load_vacancies(search_request)
            vacancies = Vacancy.cast_to_object_list(hh.vacancies)
            for vacancy in vacancies:
                file_worker.add_vacancy(vacancy)
        if user_input == '2':
            pay_value = input('Введите сумму которую хотите получать: ')
            result = file_worker.find_vacancies_pay(int(pay_value))
            for i in result:
                print(i)
