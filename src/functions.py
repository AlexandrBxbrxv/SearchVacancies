from src.hhru_api import HHruAPI
from src.vacancy import Vacancy
from src.file_worker_json import FileWorkerJson
from src.currency_request import CurrencyRequest
from src.find_vacancy_constructor import FindVacancyConstructor

hh = HHruAPI()
file_worker = FileWorkerJson()


def user_interaction():
    """Функция взаимодействия пользователя с программой."""
    is_stop = False
    while is_stop is not True:
        choice_msg = ('-\n'
                      '0 - Загрузка вакансий с сайта hh.ru\n'
                      '1 - Перевести валюты всех вакансий в рубли\n'
                      '2 - Поиск вакансий по критериям\n'
                      '3 - Вывод топ n вакансий по зарплате\n'
                      '4 - Сравнить вакансии по зарплате\n'
                      '5 - Удалить вакансию\n'
                      'Завершение работы - stop\n'
                      '-\n')
        user_input = input(choice_msg)

        if user_input == '0':
            # Загрузка вакансий с сайта hh.ru
            search_request = input('Введите название работы или интересующий вас критерий: ')
            print('Загружаем, подождите...')
            hh.load(search_request)
            vacancies = Vacancy.cast_to_object_list(hh.vacancies)
            print(f'Загружено {len(vacancies)} вакансий.')
            file_worker.save(vacancies)
            print('Сохранение завершено.')

        if user_input == '1':
            # Перевести валюты всех вакансий в рубли
            print('Загружаем актуальный на сегодня курс валют...')
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
            file_worker.save(vacancies)
            print('Зарплаты вакансий были переведены в рубли.')

        if user_input == '2':
            # Поиск вакансий по критериям
            key = 'Зарплата'
            user_value = 0
            choice_msg_2 = ('Выберите критерий поиска:\n'
                            '1 - По названию\n'
                            '2 - По зарплате\n'
                            '3 - По локации\n')
            user_input_2 = input(choice_msg_2)
            if user_input_2 == '1':
                key = 'Название'
                user_value = input('Введите слово:\n')
            if user_input_2 == '2':
                try:
                    key = 'Зарплата'
                    user_value = int(input('Введите число:\n'))
                except ValueError:
                    print('Это не число')
                    continue
            if user_input_2 == '3':
                key = 'Локация'
                user_value = input('Введите слово:\n')

            if user_input_2 in ['1', '2', '3']:
                finder = FindVacancyConstructor(file_worker.load())
                found = Vacancy.cast_to_object_list(finder.find_vacancy(key, user_value))

                print(f'Найдено {len(found)} вакансий.')
                for item in found:
                    print(item)
            else:
                print('Ничего не выбрано, возвращаем в главное меню.')

        if user_input == '3':
            # Вывод топ n вакансий по зарплате
            try:
                top_num = int(input('Введите количество вакансий на вывод: \n'))
            except ValueError:
                print('Введено не верное значение, выставлен топ 5')
                top_num = 5
            vacancies = Vacancy.cast_to_object_list(file_worker.load())
            vacancies.sort(key=lambda vacancy: vacancy.pay, reverse=True)
            for vacancy in vacancies[:top_num]:
                print(vacancy)

        if user_input == '4':
            # Сравнить вакансии по зарплате
            indexes = input('Введите id двух интересующих вакансий через пробел: \n')
            try:
                ind_1, ind_2 = indexes.split(' ')
            except ValueError:
                print('Не верный формат ввода')
                ind_1 = 'ошибка формата ввода'
                ind_2 = 'ошибка формата ввода'

            if ind_1 != 'ошибка формата ввода':
                vacancies = Vacancy.cast_to_object_list(file_worker.load())
                try:
                    vac_1 = [item for item in vacancies if item.index == ind_1]
                    vac_2 = [item for item in vacancies if item.index == ind_2]
                    result = vac_1[0].compare_pay(vac_2[0])
                    print(f'{vac_1[0]}\n{vac_2[0]}\n{result}')
                except IndexError:
                    print('Не существующие индексы')

        if user_input == '5':
            try:
                vacancy_id = input('Введите id вакансии:\n')
                file_worker.delete_vacancy(vacancy_id)
                print('Вакансия удалена.')
            except IndexError:
                print('Не существующий индекс')

        if user_input == 'stop':
            is_stop = True
