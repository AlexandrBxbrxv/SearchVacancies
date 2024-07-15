from src.hhru_api import HHruAPI
from src.vacancy import Vacancy
from src.file_worker_json import FileWorkerJson


hh = HHruAPI()
file_worker = FileWorkerJson()


def user_interaction():
    """Функция взаимодействия пользователя с программой."""
    stop = False
    while stop is not True:
        choice_msg = ('-\n'
                      '1 - Загрузка вакансий с сайта hh.ru\n'
                      '2 - Работа с вакансиями\n'
                      'Прекращение работы - stop\n'
                      '-\n')
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
            choice_msg_2 = ('-\n'
                            '1 - Вывод вакансий от указанного уровня зарплаты\n'
                            '2 - Вывод топ n вакансий по зарплате\n'
                            '3 - Сравнить вакансии по зарплате\n'
                            'Назад - Любая клавиша\n'
                            '-\n')
            user_input_2 = input(choice_msg_2)

            if user_input_2 == '1':
                pay_value = input('Введите минимальную сумму которую хотите получать: \n')
                result = file_worker.find_vacancies_pay(int(pay_value))
                vacancies = Vacancy.cast_to_object_list(result)
                for i in vacancies:
                    print(i)

            if user_input_2 == '3':
                vacancy_id = input('Введите id двух интересующих вакансий через пробел: \n')
                vacancies = Vacancy.cast_to_object_list(file_worker.load())
                result = vacancies[int(vacancy_id[0])].compare_pay(vacancies[int(vacancy_id[2])])
                print(f'{vacancies[int(vacancy_id[0])]}\n{vacancies[int(vacancy_id[2])]}\n{result}')








if __name__ == '__main__':

    # with open(r'C:\Users\Alexsandr\PycharmProjects\SearchVacancies\data\saved_vacancies.json', 'w') as f:
    #     f.write('')

    user_interaction()

    # res = '1, 2'
    #
    # print(type(int(res[0])))
