import re

date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')


def input_date():
    incoming_date = input("Введите дату рождения в формате ГГГГ-ММ-ДД: ")

    while not date_pattern.match(incoming_date):
        print("Непривильная дата. Попробуйте еще раз.")
        incoming_date = input("Введите дату рождения в формате ГГГГ-ММ-ДД: ")

    return incoming_date
