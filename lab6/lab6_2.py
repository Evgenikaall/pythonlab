import calendar

from lab6.input_utils import input_date


def get_weekday(incoming_date):
    split_date = list(map(int, incoming_date.split('-')))
    day_number = calendar.weekday(split_date[0], split_date[1], split_date[2])
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    return days[day_number]


if __name__ == '__main__':
    print(f"День недели {get_weekday(input_date())}.")
