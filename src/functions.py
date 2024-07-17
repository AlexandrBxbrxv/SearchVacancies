from src.hhru_api import HHruAPI
from src.vacancy import Vacancy
from src.file_worker_json import FileWorkerJson
from src.currency_request import CurrencyRequest


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
            # Загрузка вакансий с сайта hh.ru
            search_request = input('Введите название работы или интересующий вас критерий: ')
            print('Загружаем, подождите...')
            hh.load(search_request)
            vacancies = Vacancy.cast_to_object_list(hh.vacancies)
            print(f'Загружено {len(vacancies)} вакансий.')
            for vacancy in vacancies:
                file_worker.add_vacancy(vacancy)
            print('Сохранение завершено.')

        if user_input == '2':
            # Работа с вакансиями
            choice_msg_2 = ('-\n'
                            '1 - Перевести валюты всех вакансий в рубли\n'
                            '2 - Вывод вакансий от указанного уровня зарплаты\n'
                            '3 - Вывод топ n вакансий по зарплате\n'
                            '4 - Сравнить вакансии по зарплате\n'
                            'Назад - Любая клавиша\n'
                            '-\n')
            user_input_2 = input(choice_msg_2)

            if user_input_2 == '1':
                # Перевести валюты всех вакансий в рубли
                currency_request = CurrencyRequest()
                currency_dict = currency_request.load()
                vacancies = Vacancy.cast_to_object_list(file_worker.load())
                for vacancy in vacancies:
                    self_currency = vacancy.currency
                    if self_currency != 'RUR':
                        if self_currency == 'BYR':
                            currency = currency_dict['BYN']
                            vacancy.convert_currency(currency)
                        else:
                            currency = currency_dict.get(self_currency)
                            if currency is None:
                                print(f'Вакансию с id {vacancy.index} не возможно перевести в рубли,'
                                      f' в словаре валют нет {vacancy.currency}')
                            vacancy.convert_currency(currency)
                    file_worker.add_vacancy(vacancy)

            if user_input_2 == '2':
                # Вывод вакансий от указанного уровня зарплаты
                pay_value = input('Введите минимальную сумму которую хотите получать: \n')
                result = file_worker.find_vacancies_pay(int(pay_value))
                vacancies = Vacancy.cast_to_object_list(result)
                for i in vacancies:
                    print(i)

            if user_input_2 == '3':
                # Вывод топ n вакансий по зарплате
                top_num = int(input('Введите цифру топа(топ 5): \n'))
                vacancies = Vacancy.cast_to_object_list(file_worker.load())
                sorted_pay_vacancies = sorted([item.pay for item in vacancies], key=lambda x: x[1], reverse=True)
                print(sorted_pay_vacancies[top_num])

            if user_input_2 == '4':
                # Сравнить вакансии по зарплате
                vacancy_id = input('Введите id двух интересующих вакансий через пробел: \n')
                vacancies = Vacancy.cast_to_object_list(file_worker.load())
                result = vacancies[int(vacancy_id[0])].compare_pay(vacancies[int(vacancy_id[2])])
                print(f'{vacancies[int(vacancy_id[0])]}\n{vacancies[int(vacancy_id[2])]}\n{result}')


if __name__ == '__main__':

    user_interaction()
