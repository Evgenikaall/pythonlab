import datetime

from lab6.input_utils import input_date


def get_lived(date_of_birth):
    today = datetime.date.today()
    split_date = list(map(int, date_of_birth.split('-')))
    birth_date = datetime.date(split_date[0], split_date[1], split_date[2])
    days_lived = (today - birth_date).days
    return days_lived


if __name__ == '__main__':
    print(f"Вы прожили {get_lived(input_date())} дней.")
